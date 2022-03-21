import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='arsenal98',
                                       auth_plugin='mysql_native_password',
                                       database='BankDB')

mycursor = mydb.cursor(buffered=True)

class Customer:

    def init_table(self):

        #mycursor.execute("DROP TABLE customerinfo")

        mycursor.execute("CREATE TABLE customerinfo (acc_no INT PRIMARY KEY, name VARCHAR(40),gender VARCHAR(1),age INT(2), balance INT, acc_type VARCHAR(40))")
        mycursor.execute("describe customerinfo")

        # Printing to check description
        for i in mycursor:
            print(i)

    def NewCustomer(self,acc_no,name,gender,age,init_deposit,acc_type):

        cust=(acc_no,name,gender,age,init_deposit,acc_type)
        qry="INSERT INTO customerinfo VALUES(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(qry,cust)
        mydb.commit()

    def WithdrawCash(self,acc_no,cash):

        # Getting balance
        qry = "SELECT balance FROM customerinfo WHERE acc_no=" + acc_no
        mycursor.execute(qry)
        old_balance=mycursor.fetchone()
        cash=int(cash)  # Cash into int
        new_balance=old_balance[0]-cash # Subtracting

        # Inserting new balance back into database
        qry1= "UPDATE customerinfo SET balance="+ str(new_balance) +" WHERE acc_no=" + acc_no
        mycursor.execute(qry1)
        mydb.commit()

    def DepositCash(self,acc_no,cash):

        # Getting balance
        qry = "SELECT balance FROM customerinfo WHERE acc_no=" + acc_no
        mycursor.execute(qry)
        old_balance=mycursor.fetchone()
        cash=int(cash)  # Cash into int
        new_balance=old_balance[0]+cash # Subtracting

        # Inserting new balance back into database
        qry1= "UPDATE customerinfo SET balance="+ str(new_balance) +" WHERE acc_no=" + acc_no
        mycursor.execute(qry1)
        mydb.commit()













