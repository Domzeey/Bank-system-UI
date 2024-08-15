from customer_account import CustomerAccount
from admin import Admin
from customer_account import AccountType

accounts_list = []
admins_list = []
customer_data_file_name = "customer_data.txt"

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
        
        
    def write_customer_data_to_file(self):
        customer_data_file = open(customer_data_file_name, "w")
        for c in self.accounts_list:
            customer_data_file.writelines(c.serialize_to_string())
        customer_data_file.close()
        
    
    def load_customer_data(self):
        self.accounts_list = []
        customer_data_file = open(customer_data_file_name, "r")
        line = customer_data_file.readline().strip()
        while line != '':
            data_arr = line.split(";")
            customer = CustomerAccount(data_arr[0], data_arr[1], [data_arr[2], data_arr[3], data_arr[4], 
                                                                  data_arr[5]], data_arr[6], data_arr[7], AccountType[data_arr[8]])
            self.accounts_list.append(customer)
            line = customer_data_file.readline().strip()
            
        customer_data_file.close()
        
        
        
    def load_bank_data(self):
        
        #create customers
        #account_no = 1234
        # customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00, AccountType.SAVINGS)
        # self.accounts_list.append(customer_1)
        
        # account_no+=1
        # customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00, AccountType.CURRENT)    
        # self.accounts_list.append(customer_2)

        # account_no+=1
        # customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00, AccountType.FIXED)
        # self.accounts_list.append(customer_3)

        # account_no+=1
        # customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00, AccountType.CURRENT)
        # self.accounts_list.append(customer_4)
        
        self.load_customer_data()
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)
        
        admin_3 = Admin("Admin",  "Dominion", ["47", "Test Street", "Luton", "LU2 0FY"], "admin", "admin", True)
        self.admins_list.append(admin_3)


    def search_admins_by_name(self, admin_username):
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
                
        return found_admin 
        
    def search_customers_by_name(self, customer_lname):
        found_customer = None
        for c in self.accounts_list:
            last_name = c.get_last_name()
            if(last_name == customer_lname):
                found_customer = c
                break
        if found_customer == None:
            print("\n The Customer %s does not exist! Try again...\n"%customer_lname)
            
        return found_customer
            

    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        sender_account = self.search_customers_by_name(sender_lname)
        if sender_account == None:
            return "Sender Account not found", False
        
        receiver_account = self.search_customers_by_name(receiver_lname)
        
        transfer_sucess = False
        msg = "Receiver Account not found"
        
        if receiver_account == None:
            return msg, transfer_sucess
        
        if str(receiver_account.get_account_no()) == str(receiver_account_no):
            msg, success = sender_account.withdraw(amount)
            if success == True:
                receiver_account.deposit(amount)
                transfer_sucess = True
                msg = "Transfer successful"
                self.write_customer_data_to_file()
        
        return msg, transfer_sucess
    
    
    def depositMoney(self, customer_account, amount):
        customer_account.deposit(amount)
        self.write_customer_data_to_file()
        
    def withdrawMoney(self, customer_account, amount):
        return customer_account.withdraw(amount)
        self.write_customer_data_to_file()
        
    def updateCustomerDetails(self, customer_account, fname, lname, address):
        customer_account.update_first_name(fname)
        customer_account.update_last_name(lname)
        customer_account.update_address(address)
        self.write_customer_data_to_file()


    def updateAdminDetails(self, admin_obj, fname, lname, address):
        admin_obj.update_first_name(fname)
        admin_obj.update_last_name(lname)
        admin_obj.update_address(address)
        
    def removeCustomer(self, customer_lname):
        customer_account = self.search_customers_by_name(customer_lname)
        msg = "Customer Removed Successfully"
        if customer_account != None:
            self.accounts_list.remove(customer_account)
            self.write_customer_data_to_file()
            
        else:
            msg = "Cannot find customer"
            
        return msg
            

                
    def admin_login(self, username, password):
        found_admin = self.search_admins_by_name(username) 
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
            else:
                msg = "\n Invaid username or password"
                found_admin = None
        return msg, found_admin

    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Available options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Sign out")
         print (" ")
         option = int(input ("Choose your option: "))
         return option


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                msg, success = self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)   
                print(msg)
                print(success)
                
            elif choice == 2:
                customer_name = input("\n Please input customer surname :\n") 
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    customer_account.run_account_options()
            
            elif choice == 3:
                customer_name = input("\n Please input customer surname :\n") 
                customer_account = self.search_customers_by_name(customer_name)
                self.accounts_list.remove(customer_account)
                self.print_all_accounts_details()
                
            
            elif choice == 4:
                self.print_all_accounts_details
            
            elif choice == 5:
                loop = 0
        print ("\n Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            details = ""
            i = 0
            for c in self.accounts_list:
                i+=1
                details += "\n " + str(i) + ". " + c.print_details() + "------------------------"
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")
            return details
        
    def get_management_report(self):
        total_customers= len(self.accounts_list)
        total_balance = 0.0
        total_overdraft = 0.0
        interest_payable = 0.0
        for c in self.accounts_list:
            if(c.get_balance() < 0.0):
                total_overdraft += c.get_balance()
            else:
                total_balance += c.get_balance()
                interest_payable += (c.get_interest_rate()/100) * c.get_balance()
                
        report = "Total Customers: %d\n Total Balance: %d\n Total Interest Payable: %d\nTotal Overdraft %d"  %(total_customers,
                                                                                                               total_balance, interest_payable, total_overdraft)
        
        return report
            
        


# app = BankSystem()
# app.run_main_options()
