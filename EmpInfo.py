import mysql.connector
mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='arsenal98',
                                       auth_plugin='mysql_native_password',
                                       database='BankDB')

mycursor = mydb.cursor(buffered=True)

class Emp:
    def __init__(self):
        self.printMenu()

    def printMenu(self):
        print("     Please select options: ")
        print("1: New employee")
        print("2: Existing employee")
        print("3: Exit \n")
        option = input("Enter Option: ")

        if option == "1":
            self.NewEmployee()
        elif option == "2":
            self.ExistingEmployee()
        elif option == "3":
            print("\nExit program")
        elif option == "init":
            self.init_table()

    def init_table(self):

        #mycursor.execute("DROP TABLE emp_info")

        mycursor.execute("CREATE TABLE emp_info (emp_id INT PRIMARY KEY, emp_name VARCHAR(40), branch VARCHAR(40), status VARCHAR(40), salary INT, branch_code INT, FOREIGN KEY(branch_code) REFERENCES branch_info(branch_code) ON DELETE SET NULL )")
        mycursor.execute("describe emp_info")

        # Printing to check description
        for i in mycursor:
            print(i)

    def NewEmployee(self):
        emp_id = input("Enter employer id: ")
        emp_name = input("Enter name: ")
        gender = input("Enter gender: ")
        age = input("Enter age: ")
        branch = input("Enter branch: ")
        salary = input("Enter salary: ")
        branch_code = input("Enter branch code: ")

        cust = (emp_id, emp_name, branch, salary, branch_code)
        qry = "INSERT INTO emp_info VALUES(%s,%s,%s,%s,%s)"
        mycursor.execute(qry, cust)
        mydb.commit()



