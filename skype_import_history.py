__author__ = 'taras'
import Skype4Py
import sqlite3

db_conn = sqlite3.connect('skype_contacts.db')
db_cursor = db_conn.cursor()

skype = Skype4Py.Skype()
skype.Attach()


