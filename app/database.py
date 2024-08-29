import sqlite3

def init_db():
    conn = sqlite3.connect('wedding_rsvp.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rsvps 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  phone TEXT, 
                  name TEXT, 
                  attendance TEXT, 
                  arrival_date TEXT, 
                  departure_date TEXT, 
                  guests INTEGER)''')
    conn.commit()
    conn.close()
