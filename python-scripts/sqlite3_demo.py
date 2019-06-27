import sqlite3

#conn = sqlite3.connect(':memory:') # In-memory database, useful for testing
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Next lines commented in order to avoid operational errors or duplicates once the table is created
#c.execute(""" CREATE TABLE employees (first text, last text, pay integer )""")
#c.execute(""" INSERT INTO employees VALUES ('Rodrigo', 'Ávila', 10)""")
#c.execute(""" INSERT INTO employees VALUES ('Pablo', 'Solís', 5)""")
#c.execute("INSERT INTO employees VALUES ( ?, ?, ?)", ("Rodrigo", "Solís", "15")) # in this way SQL injection is avoided
#c.execute("INSERT INTO employees VALUES ( :first, :last, :pay)", {"first":"Pablo", "last":"Ávila", "pay":20}) # another way to avoid SQL injection

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES ( :first, :last, :pay)", {"first":emp.first, "last":emp.last, "pay":emp.pay})

def get_emps_by_name(firstname):
    c.execute("SELECT *  FROM employees WHERE first = :first ", {'first':firstname})
    return c.fetchall()

#c.execute("SELECT *  FROM employees WHERE first = ? ", ('Rodrigo',))
c.execute("SELECT *  FROM employees WHERE first = :first ", {'first':'Pablo'})

#<print(c.fetchone()) # return a tuple
#print(c.fetchmany(5)) # return a list as well as fetchall
print(c.fetchall())

conn.commit()
conn.close()

