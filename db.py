import sqlite3

conn = sqlite3.connect(r'd:/temp/orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT,
    age INT);
    """)
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_id INT PRIMARY KEY,
    date TEXT,
    user_id TEXT,
    total TEXT);
    """)
conn.commit()
cur.execute("""INSERT INTO users(user_id, fname, lname, gender, age) 
    VALUES('', 'Alex', 'Smith', 'male', 25);""")
conn.commit()

