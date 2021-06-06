import sqlite3
import random

#----------------------------------------------------------------------------------------------
# Connect to Database
# conn = sqlite3.connect('customer.db')

# Create Cursor
# c = conn.cursor()

# Create a Table
#c.execute("""CREATE TABLE customers(first_name text,last_name text,email text)""")

# Insert into the table
#c.execute("INSERT INTO customers VALUES ('Mr.', 'NoOne', 'mr.noone@gmail.com')")
#c.execute("INSERT INTO customers VALUES ('Mr.', 'somebody', 'mr.somebody@gmail.com')")
#c.execute("INSERT INTO customers VALUES ('Mr.', 'anybody', 'mr.anybody@gmail.com')")

# Query the DataBase
# c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)
# data = c.fetchall()
# print(data)
#----------------------------------------------------------------------------------------------

def create_table():
    # Connect to Database
    conn = sqlite3.connect('customer.db')
    # Create Cursor
    c = conn.cursor()
    apiKey = ''
    for i in range(24):
        key = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123546879')
        apiKey += key
    f = open('tables.txt', 'a')
    f.write(f'{apiKey}\n')
    f.close()
    c.execute(f"CREATE TABLE {apiKey} (first_name text,last_name text,email text)")
    # Commit our command
    conn.commit()
    conn.close()
    return apiKey

def insert_Data(apiKey, data):
    # Connect to Database
    conn = sqlite3.connect('customer.db')
    # Create Cursor
    c = conn.cursor()
    c.execute(f"INSERT INTO {apiKey} VALUES (?,?,?)",(data[0], data[1], data[2]))
    # Commit our command
    conn.commit()
    conn.close()

def see_data(apiKey):
    # Connect to Database
    conn = sqlite3.connect('customer.db')
    # Create Cursor
    c = conn.cursor()
    c.execute(f"SELECT * FROM {apiKey}")
    data = c.fetchall()
    print(data)
    # Commit our command
    conn.commit()
    conn.close()

def main():
    ask = str(input('Do u want to make new table [Y/n] : ')).lower()
    if ask == 'y':
        apiKey = create_table()
    else:
        dataentry = str(input('Do u want to enter data [Y/n] : ')).lower()
        if dataentry == 'y':
            apiKey = str(input('Enter ur apiKey : '))
            data = str(input('Enter data : '))
            data = data.split()
            insert_Data(apiKey, data)
            see_data(apiKey)
        else:
            apiKey = str(input('Enter ur apiKey : '))
            see_data(apiKey)
main()
#----------------------------------------------------------------------------------------------
