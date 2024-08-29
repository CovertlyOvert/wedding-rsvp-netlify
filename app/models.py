import sqlite3

def save_rsvp(phone, name, attendance, arrival_date, departure_date, guests):
    conn = sqlite3.connect('wedding_rsvp.db')
    c = conn.cursor()
    c.execute("INSERT INTO rsvps (phone, name, attendance, arrival_date, departure_date, guests) VALUES (?, ?, ?, ?, ?, ?)", 
              (phone, name, attendance, arrival_date, departure_date, guests))
    conn.commit()
    conn.close()
