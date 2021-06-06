import sqlite3

# Connect to Database
conn = sqlite3.connect('customer.db')

# Create Cursor
c = conn.cursor()

# Create a Table
#c.execute("""CREATE TABLE customers(first_name text,last_name text,email text)""")

# Insert into the table
#c.execute("INSERT INTO customers VALUES ('Mr.', 'NoOne', 'mr.noone@gmail.com')")
#c.execute("INSERT INTO customers VALUES ('Mr.', 'somebody', 'mr.somebody@gmail.com')")
#c.execute("INSERT INTO customers VALUES ('Mr.', 'anybody', 'mr.anybody@gmail.com')")

# Query the DataBase
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)
data = c.fetchall()
print(data)

# Commit our command
conn.commit()

# Close our connection
conn.close()
