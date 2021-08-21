
import sqlite3
 
conn = sqlite3.connect('moyu_engine/config/data/constant.db') 

cursor = conn.cursor()
cursor.execute("CREATE TABLE constant \
       (ID INT PRIMARY KEY     NOT NULL,\
       Constant           TEXT    NOT NULL,\
       Value            INT     NOT NULL,")
cursor.execute("INSERT INTO constant (ID,Constant,Value) VALUES (1, 'Paul', 32);")
 
cursor.execute("INSERT INTO constant VALUES (2, 'Allen', 25);")
cursor.execute("INSERT INTO constant VALUES (3, 'Teddy', 23);")
cursor.execute("INSERT INTO constant VALUES (4, 'Mark', 25);")
cursor.execute("INSERT INTO constant VALUES (5, 'David', 27);")
cursor.execute("INSERT INTO constant VALUES (6, 'Kim', 22);")
cursor.execute("INSERT INTO constant VALUES (7, 'James', 24);")
cursor.execute("SELECT * FROM constant;")
 
results = cursor.fetchall()  
for row in results:  
    print(row)  
 
cursor.close()        # 关闭cursor
conn.commit()         # 提交事务
conn.close()          # 关闭连接