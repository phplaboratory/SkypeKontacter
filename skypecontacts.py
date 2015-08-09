
import Skype4Py
import sqlite3

db_conn = sqlite3.connect('skype_contacts.db')
db_cursor = db_conn.cursor()
db_cursor2 = db_conn.cursor()

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Obtain some information from the client and print it out.
print 'Your full name:', skype.CurrentUser.FullName
print 'Your contacts:'
for user in skype.Friends:
    try:
        db_cursor.execute('SELECT * FROM skype_contacts WHERE handle=?', (user.Handle,))
        if( db_cursor.fetchone()):
            print "contact ", user.Handle, " found in database"
            db_cursor2.execute("UPDATE skype_contacts SET status=1 WHERE handle=?", (user.Handle,))
            db_conn.commit()
        else:
            db_cursor.execute('INSERT INTO  skype_contacts (handle,status) VALUES (?,1)', (user.Handle,))
            db_conn.commit()
            print "contact ", user.Handle, " successfully added to database"
    except sqlite3.Error as e:
                    print "An error occurred in inserting into database contact ,",user.Handle,":", e.args[0]

