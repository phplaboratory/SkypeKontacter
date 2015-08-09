__author__ = 'taras'

import Skype4Py
import sqlite3
import time

db_conn = sqlite3.connect('skype_contacts.db')
db_cursor = db_conn.cursor()
db_cursor2 = db_conn.cursor()

skype = Skype4Py.Skype()

db_cursor.execute('SELECT handle FROM skype_contacts WHERE status=0')

new_contacts = db_cursor.fetchall()

for row in new_contacts:
        handle = row[0]
        r = skype.SearchForUsers(handle)
        found = 0
        for u in r:
            if( u.Handle == handle):
                found = 1
                print "Request to ",handle
                u.SetBuddyStatusPendingAuthorization("MLM".decode("utf-8"))
                db_cursor2.execute("UPDATE skype_contacts SET status=2 WHERE handle=?", (handle,))
                db_conn.commit()
                time.sleep(5)
                skype.SendMessage(handle,"hi")
            else:
                print "Search: ",handle ," found: ",u.Handle
        if(found == 0) :
            print "Search: ",handle ," not found !"
            db_cursor2.execute("UPDATE skype_contacts SET status=3 WHERE handle=?", (handle,))
            db_conn.commit()

        time.sleep(5)
