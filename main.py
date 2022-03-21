# Banking database personal project
# - Imran bin Ahmad Azhar
# - 08/03/2022

import mysql.connector
from BankMenu import BankMenu
from EmpInfo import Emp
from mysql.connector import Error

mydb=mysql.connector.connect(host='localhost',
                            user='root',
                            passwd='arsenal98',
                            auth_plugin='mysql_native_password',
                            database='BankDB')
#print(mydb)

mycursor=mydb.cursor(buffered=True)

# ------ Tutorials ------
#mycursor.execute('create database Prod')
#QRY='insert into product values(%s,%s,%s,%s,%s)'
#P1=('P2','Toothpaste','2020-02-01',100,200),('P3','Pencil','2020-02-11',10,500),('P4','Pen','2020-02-21',10,700)
#mycursor.execute('UPDATE product SET price=300 where PID="P2"')
#mycursor.executemany(QRY,P1)
#A='select * from product'
#mycursor.execute(A)
#B=mycursor.fetchmany(2)
#print(B)
#print("total no. of rows", mycursor.rowcount)
#mycursor.execute('ALTER TABLE product ADD PRIMARY KEY(PID)')
#mydb.commit()
#mycursor.execute('SELECT * FROM product WHERE price>5')

#for i in mycursor:
#    print(i)

# ------ Tutorials END ------

bank=BankMenu()

#employer=Emp()
