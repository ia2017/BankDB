import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='arsenal98',
                                       auth_plugin='mysql_native_password',
                                       database='BankDB')

mycursor = mydb.cursor(buffered=True)

class Loan:
    def __init__(self):
        self.printMenu()

    def printMenu(self):
        print("     Please select options: ")
        print("1: New loan")
        print("2: Existing loan")
        print("3: Exit \n")
        option = input("Enter Option: ")

        if option == "1":
            self.NewLoan()
        elif option == "2":
            self.ExistingCard()
        elif option == "3":
            print("\nExit program")
        elif option == "init":
            self.init_table()

    def init_table(self):

        #mycursor.execute("DROP TABLE branch_info")

        mycursor.execute("CREATE TABLE loan_info (loan_type VARCHAR(40), loan_amount INT, interest INT, acc_no INT, FOREIGN KEY(acc_no) REFERENCES customerinfo(acc_no) ON DELETE SET NULL) ")
        mycursor.execute("describe loan_info")

        # Printing to check description
        for i in mycursor:
            print(i)

    def NewLoan(self):
        branch_code = input("Enter branch code: ")
        branch_city = input("Enter branch city: ")
        branch_name = input("Enter branch name: ")
        acc_no = input("Enter acc_no: ")

        loan_in = (branch_code, branch_city, branch_name, acc_no)
        qry = "INSERT INTO emp_info VALUES(%s,%s,%s,%s)"
        mycursor.execute(qry, branch_in)
        mydb.commit()



