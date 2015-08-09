__author__ = 'taras'
import httplib
import re
from lxml import html
import sqlite3
db_conn = sqlite3.connect('skype_contacts.db')
db_cursor = db_conn.cursor()


expr = re.compile('^skype:(.*)\\?add$')
conn = httplib.HTTPConnection("takefriend.ru")
conn.request("GET", "/ru/etc/skype")
response = conn.getresponse()
if (response.status ==200):
    data = response.read()
    tree = html.fromstring(data)
    contacts = tree.xpath("//tr/td/noindex/a/@href")
    number_of_contacts = 0
    number_of_new_contacts = 0
    if contacts :
        for c in contacts:
            m = expr.match(c)
            if(m):
                number_of_contacts=number_of_contacts+1
                handle = m.group(1)
                handle = handle.lower()
                try:
                    db_cursor.execute('SELECT * FROM skype_contacts WHERE handle=?', (handle,))
                    if( db_cursor.fetchone()):
                        print "contact ", handle, " found in database"
                    else:
                        db_cursor.execute('INSERT INTO  skype_contacts (handle) VALUES (?)', (handle,))
                        db_conn.commit()
                        number_of_new_contacts = number_of_new_contacts + 1
                        print "contact ", handle, " successfully added to database"
                except sqlite3.Error as e:
                    print "An error occurred in inserting into database contact ,",handle,":", e.args[0]
    print "On page http://takefriend.ru/ru/etc/skype found ", number_of_contacts, " of contacts , new from them ", number_of_new_contacts
else:
    print "Error get page http://takefriend.ru/ru/etc/skype ",response.status ,response.reason



