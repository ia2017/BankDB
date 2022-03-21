import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='arsenal98',
                                       auth_plugin='mysql_native_password',
                                       database='BankDB')

mycursor = mydb.cursor(buffered=True)

class Branch:
    def __init__(self):
        self.printMenu()

    def printMenu(self):
        print("     Please select options: ")
        print("1: New branch")
        print("2: Existing branch")
        print("3: Exit \n")
        option = input("Enter Option: ")

        if option == "1":
            self.NewBranch()
        elif option == "2":
            self.ExistingBranch()
        elif option == "3":
            print("\nExit program")
        elif option == "init":
            self.init_table()

    def init_table(self):

        #mycursor.execute("DROP TABLE branch_info")

        mycursor.execute("CREATE TABLE branch_info (branch_code INT PRIMARY KEY, branch_city VARCHAR(40), branch_name VARCHAR(40), acc_no INT, FOREIGN KEY(acc_no) REFERENCES customerinfo(acc_no) ON DELETE SET NULL) ")
        mycursor.execute("describe branch_info")

        # Printing to check description
        for i in mycursor:
            print(i)

    def NewBranch(self):
        branch_code = input("Enter branch code: ")
        branch_city = input("Enter branch city: ")
        branch_name = input("Enter branch name: ")
        acc_no = input("Enter acc_no: ")

        branch_in = (branch_code, branch_city, branch_name, acc_no)
        qry = "INSERT INTO emp_info VALUES(%s,%s,%s,%s)"
        mycursor.execute(qry, branch_in)
        mydb.commit()



