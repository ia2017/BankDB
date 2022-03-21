from CustomerInfo import Customer
from EmpInfo import Emp
from BranchInfo import Branch
from LoanInfo import Loan
from CardInfo import Card

class BankMenu:
    def __init__(self):
        self.printMenu()

    def printMenu(self):
        print("     Please select options: ")
        print("1: New customer")
        print("2: Existing customer")
        print("3: Exit \n")
        option=input("Enter Option: ")

        if option=="1":
            self.NewCustomer()
        elif option=="2":
            self.ExistingCustomer()
        elif option=="3":
            print("\nExit program")
        elif option == "admin":
            self.Admin()


    def NewCustomer(self):
        print(" ")

        # Basic Customer info
        acc_no = input("Enter account number: ")
        cust_name=input("Enter name: ")
        gender=input("Enter gender: ")
        age=input("Enter age: ")
        acc_type=input("Enter account type: ")
        init_deposit = input("Enter initial deposit: ")

        # Branch info

        # Card info - multiples

        # Loan info - optional

        cust=Customer()
        cust.NewCustomer(acc_no,cust_name,gender,age,init_deposit,acc_type)
        #balance=Balance(acc_no,init_deposit)
        #cust.init_table()



        print("\nAccount created successfully")


    def ExistingCustomer(self):
        print("\n ")
        acc_no=input("Please enter account number: ")
        print("     What would you like to do:")
        print("1. Withdraw cash")
        print("2. Deposit cash")
        print("3. Loan")
        option=input("Enter option: ")

        # Initiate class
        cust=Customer()

        if option=="1":

            cash=input("Please enter cash amount: ")
            cust.WithdrawCash(acc_no,cash)



        #cust=Acc(acc_no_ex,cash)
        #cust.init_table()


    def Admin(self):
        print("\n ")
        print("1: Employee information")
        print("2. Branch information")
        print("3. Loan information")
        print("4. Card information")
        option=input("Enter Option: ")

        if option=="1":
            employer=Emp()
        elif option=="2":
            branch=Branch()
        elif option=="3":
            loan=Loan()
        elif option=="4":
            card=Card()
