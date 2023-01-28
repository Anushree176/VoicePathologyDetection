import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        conn = sqlite3.connect('database.db')
        print("Open database successfully..")
        
        return conn 
    
    except Error:
        print(Error)

def sql_table(conn):
    #conn = conn.cursor()
    conn.execute('''CREATE TABLE users (
            Name TEXT Not Null,
            Phone INTEGER Not Null Unique,
            Email TEXT Not Null Unique,
            Password TEXT Not Null
            )''')
    conn.commit()
    print("Table created sucessfully..")


conn = sql_connection()

# sql_table(conn)

def sql_insert(conn, entities):

    conn.execute('INSERT INTO users( Name, Phone, Email, Password) VALUES(?, ?, ?, ?)', entities)
    
    conn.commit()

entities = ('Aditya', 9804138060,'borudeaditya@gmail.com','Aditya31')

sql_insert(conn, entities)