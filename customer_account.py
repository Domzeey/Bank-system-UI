from enum import Enum

class AccountType(Enum):
    SAVINGS = {
        'interest_rate': 2.5,
        'overdraft_limit': 100
        }
    
    FIXED = {
        'interest_rate': 7.0,
        'overdraft_limit': 0.0
        }
    
    CURRENT = {
        'interest_rate': 0.0,
        'overdraft_limit': 500
        }
    
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance, account_type):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.account_type = account_type
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance+=amount
        
    def withdraw(self, amount):
        if (self.balance + self.get_overdraft_limit()) >= amount:
            self.balance -= amount
            return "Withdrawal Successful", True
        else:
            return "Insufficient Balance", False
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def get_account_type(self):
        return self.account_type
    
    def get_interest_rate(self):
        return self.account_type.value['interest_rate']
    
    def get_overdraft_limit(self):
        return self.account_type.value['overdraft_limit']
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        details = "First name: %s\nLast name: %s\nAccount No: %s\nAddress: %s %s %s %s\nAccount Type: %s\n" %(self.fname,self.lname, 
                                                                                                              self.account_no,self.address[0],self.address[1], self.address[2], self.address[3],self.account_type)
    
        
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Account No: %s" %self.account_no)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print("Account Type: %s" %self.account_type)
        print(" ")
        
        return details
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                amount = float(input("\n Please enter amount to be deposited: "))
                self.deposit(amount)
                self.print_balance()
            elif choice == 2:
                amount = float(input("\n Please enter amount to be withdrawn: "))
                self.withdraw(amount)
                self.print_balance()
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                fname = input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                sname = input("\nEnter new customer last name: ")
                self.update_last_name(sname)
                self.print_details()
            elif choice == 5:
                addr = input("\n Enter new customer address: ")
                self.update_address(addr)
                self.print_details()
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")
        
        
    def serialize_to_string(self):
        return "%s;%s;%s;%s;%s;%s;%s;%s;%s\n" %(self.fname, self.lname, self.address[0], self.address[1], self.address[2], self.address[3], 
                                              self.account_no, self.balance, self.account_type.name)
        
        
        
        