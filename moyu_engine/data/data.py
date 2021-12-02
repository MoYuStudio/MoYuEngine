
import sqlite3

conn = sqlite3.connect('moyu_engine\data\tile.db')

print("Opened database successfully")

c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")
conn.commit()
conn.close()

if __name__ == "__main__":
    pass
