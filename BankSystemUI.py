# 

from bank_system import BankSystem
import tkinter
    


class AdminLogin:
    
    def __init__(self):
    
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.title("Admin Login")
        
        self.mw.geometry("400x400")
        self.admin_username_label = tkinter.Label(self.mw, text = "Enter Admin Username")
        self.admin_username_entry = tkinter.Entry(self.mw, width = 20)
        
        self.admin_username_label.pack(side="top")
        self.admin_username_entry.pack(side="top")
        
        
        self.admin_pwd_label = tkinter.Label(self.mw, text = "Enter Admin Password")
        self.admin_pwd_entry = tkinter.Entry(self.mw, show="*", width = 20)
        
        self.admin_pwd_label.pack(side="top")
        self.admin_pwd_entry.pack(side="top")
        
        self.login_btn = tkinter.Button(self.mw, text ="Login", command =lambda: self.login(self.admin_username_entry.get(), self.admin_pwd_entry.get()))
        self.login_btn.pack(side = "top")
        
        
        tkinter.mainloop()
        
        
    def login(self, username, password):
        msg, admin_obj = bank_system_obj.admin_login(username, password)
        if admin_obj != None:
            self.mw.destroy()
            AdminOptions(admin_obj)
        else:
            tkinter.messagebox.showerror("Error", msg)

class AdminOptions:
    def __init__(self, admin_obj):
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("400x400")
        self.mw.title("Admin Options")
        
        self.admin_obj = admin_obj
        
        welcome_text = "Welcome Admin: %s %s" %(admin_obj.get_first_name(), admin_obj.get_last_name())
        welcome_label = tkinter.Label(self.mw, text = welcome_text)
        welcome_label.pack()
        
        
        self.transfer_btn = tkinter.Button(self.mw, text ="Transfer Money", command =lambda: self.doTransfer()).pack()
        
        self.customer_account_ops_btn = tkinter.Button(self.mw, text ="Customer account operations & profie settings", command =lambda: self.customerAccountOps()).pack()
        
        self.delete_customer_btn = tkinter.Button(self.mw, text ="Delete Customer", command =lambda: self.deleteCustomer()).pack()
        
        self.show_all_cust_btn = tkinter.Button(self.mw, text ="Show all customers detail", command =lambda: self.printAllCustomerDetails()).pack()
        
        self.mgmt_report_btn = tkinter.Button(self.mw, text ="Management Report", command =lambda: self.showManagementReport()).pack()
        
        self.update_admin_details_btn = tkinter.Button(self.mw, text ="Update Admin Details", command =lambda: self.updateAdminDetails()).pack()
        
        self.sign_out_btn = tkinter.Button(self.mw, text ="Sign Out", command =lambda: self.sign_out()).pack()
        
        
    
    def doTransfer(self):
        TransferMoney()
        
    def customerAccountOps(self):
        CustomerAccountOps()
        
    def deleteCustomer(self):
        customer_lname = tkinter.simpledialog.askstring("Customer Name", "Please enter customer last name:")
        msg = bank_system_obj.removeCustomer(customer_lname)
        tkinter.messagebox.showinfo("Message", msg)
        
    def printAllCustomerDetails(self):
        tkinter.messagebox.showinfo("Customer Details", bank_system_obj.print_all_accounts_details())
        
    def showManagementReport(self):
        tkinter.messagebox.showinfo("Management Report", bank_system_obj.get_management_report())
        
    def updateAdminDetails(self):
        AdminDetails(self.admin_obj)
    
    
    
    def sign_out(self):
        self.mw.destroy()
        AdminLogin()


class TransferMoney:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("400x400")
        
        self.sender_label = tkinter.Label(self.mw, text = "Enter Sender Surname:").pack()
        self.sender_entry = tkinter.Entry(self.mw, width=20)
        self.sender_entry.pack()
        
        self.amount_label = tkinter.Label(self.mw, text = "Enter Amount to be transferred:").pack()
        self.amount_entry = tkinter.Entry(self.mw, width=20)
        self.amount_entry.pack()
        
        self.receiver_label = tkinter.Label(self.mw, text = "Enter Receiver Surname:").pack()
        self.receiver_entry = tkinter.Entry(self.mw, width=20)
        self.receiver_entry.pack()
        
        self.receiver_account_label = tkinter.Label(self.mw, text = "Enter Receiver Account:").pack()
        self.receiver_account_entry = tkinter.Entry(self.mw, width=20)
        self.receiver_account_entry.pack()
        
        
        self.transfer_btn = tkinter.Button(self.mw, text ="Do Transfer", command =lambda: self.transfer_money(self.sender_entry.get(), self.receiver_entry.get(), 
                                                                                                              self.receiver_account_entry.get(), self.amount_entry.get())).pack()
        
        
    def transfer_money(self, sender_lname, receiver_lname, receiver_account_no, amount):
        msg, transfer_success = bank_system_obj.transferMoney(sender_lname, receiver_lname, receiver_account_no, float(amount))
        if transfer_success:
            tkinter.messagebox.showinfo("Success", msg)
            self.mw.destroy()
        else:
            tkinter.messagebox.showerror("Error", msg)
            
        


class CustomerAccountOps:
    def __init__(self):
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("800x400")
        
        self.surname_label = tkinter.Label(self.mw, text = "Enter Customer Surname:")
        self.surname_label.grid(row = 0, column=0)
        
        self.surname_entry = tkinter.Entry(self.mw, width=20)
        self.surname_entry.grid(row = 0, column=1)
        self.surname_entry.bind("<KeyPress>", self.on_entry_focus)
        
        self.search_btn = tkinter.Button(self.mw, text ="Search", command =lambda: self.search(self.surname_entry.get()))
        self.search_btn.grid(row = 0, column=2)
        
        self.deposit_btn = tkinter.Button(self.mw, text ="Deposit Money", command =lambda: self.depositMoney())
        self.withdraw_btn = tkinter.Button(self.mw, text ="Withdraw Money", command =lambda: self.withdrawMoney())
        self.balance_btn = tkinter.Button(self.mw, text ="Check Balance", command =lambda: self.checkBalance())
        self.check_details_btn = tkinter.Button(self.mw, text = "Check/Update Customer Details", command = lambda: self.checkCustomerDetails())
        
    
    def on_entry_focus(self, event):
        self.clearButtonsFromGrid()
        
    def search(self, customer_lname):
        self.customer_account = bank_system_obj.search_customers_by_name(customer_lname)
        if self.customer_account != None:
            self.deposit_btn.grid(row = 1, column=0, columnspan=3)
            self.withdraw_btn.grid(row = 2, column=0, columnspan=3)
            self.balance_btn.grid(row = 3, column=0, columnspan=3)
            self.check_details_btn.grid(row = 4, column = 0, columnspan=3)
            
        else:
            self.clearButtonsFromGrid()
            tkinter.messagebox.showerror("Error", "Customer not found")
            
    
    def clearButtonsFromGrid(self):
        self.deposit_btn.grid_forget()
        self.withdraw_btn.grid_forget()
        self.balance_btn.grid_forget()
        self.check_details_btn.grid_forget()
    
    def depositMoney(self):
        amount = tkinter.simpledialog.askfloat("Amount", "Please enter amount to be deposited:")
        bank_system_obj.depositMoney(self.customer_account, amount)
        msg = "Deposit Successful\nBalance: %s" %(self.customer_account.get_balance())
        tkinter.messagebox.showinfo("Success", msg)
        
        
    def withdrawMoney(self):
        amount = tkinter.simpledialog.askfloat("Amount", "Please enter amount to withdraw:")
        msg, success = bank_system_obj.withdrawMoney(self.customer_account, amount)
        if success == True:
            msg = "Withdrawal Successful\nBalance : %s" %(self.customer_account.get_balance())
            tkinter.messagebox.showinfo("Success", msg)
        else:
            tkinter.messagebox.showerror("Error", msg)
        
        
    def checkBalance(self):
        balance = self.customer_account.get_balance()
        tkinter.messagebox.showinfo("Balance", balance)
        
    def checkCustomerDetails(self):
        CustomerDetails(self.customer_account)
    
    

class CustomerDetails:
    def __init__(self, customer_account):
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("800x400")
        self.mw.title("Customer Details "+customer_account.get_first_name() + " " + customer_account.get_last_name())
        
        account_text = "Account No: " + str(customer_account.get_account_no())
        balance_text = "Balance: " + str(customer_account.get_balance())
        
        
        account_type_text = "Account Type: %s, Interest Rate: %s, Overdraft Limit: %s" %(customer_account.get_account_type(), customer_account.get_interest_rate(), customer_account.get_overdraft_limit())
        
        tkinter.Label(self.mw, text = account_text, font=("Helvetica", 18, "bold")).grid(row=0, column=2)
        tkinter.Label(self.mw, text = balance_text, font=("Helvetica", 18, "bold")).grid(row=1, column=2)
        tkinter.Label(self.mw, text = account_type_text, font=("Helvetica", 14, "bold")).grid(row=2, column=2)
        
        tkinter.Label(self.mw, text = "Firstname:").grid(row=3, column=1)
        self.fname_entry = tkinter.Entry(self.mw, width=20)
        self.fname_entry.insert(0, customer_account.get_first_name())
        self.fname_entry.grid(row=3, column=2)
        
        tkinter.Label(self.mw, text = "Lastname:").grid(row=4, column=1)
        self.lname_entry = tkinter.Entry(self.mw, width=20)
        self.lname_entry.insert(0, customer_account.get_last_name())
        self.lname_entry.grid(row=4, column=2)
        
        tkinter.Label(self.mw, text = "Address:").grid(row=5, column=1)
        
        address = customer_account.get_address();
        
        tkinter.Label(self.mw, text = "House No:").grid(row=6, column=1)
        
        self.house_no_entry = tkinter.Entry(self.mw, width=20)
        self.house_no_entry.insert(0, address[0])
        self.house_no_entry.grid(row=6, column=2)
        
        tkinter.Label(self.mw, text = "Street:").grid(row=7, column=1)
        self.street_entry = tkinter.Entry(self.mw, width=20)
        self.street_entry.insert(0, address[1])
        self.street_entry.grid(row=7, column=2)
        
        
        tkinter.Label(self.mw, text = "City:").grid(row=8, column=1)
        self.city_entry = tkinter.Entry(self.mw, width=20)
        self.city_entry.insert(0, address[2])
        self.city_entry.grid(row=8, column=2)
        
        tkinter.Label(self.mw, text = "Postcode:").grid(row=9, column=1)
        self.postcode_entry = tkinter.Entry(self.mw, width=20)
        self.postcode_entry.insert(0, address[3])
        self.postcode_entry.grid(row=9, column=2)
        
        
        self.update_btn = tkinter.Button(self.mw, text ="Update Details", command =lambda: 
                                         self.saveCustomerDetails(customer_account, self.fname_entry.get(), self.lname_entry.get(),
                                                                  [self.house_no_entry.get(), self.street_entry.get(), self.city_entry.get(),
                                                                   self.postcode_entry.get()]))
        self.update_btn.grid(row=10, column=2)
        
        
    def saveCustomerDetails(self, customer_account, fname, lname, address):
        bank_system_obj.updateCustomerDetails(customer_account, fname, lname, address)
        tkinter.messagebox.showinfo("Success", "Customer details updated successfully")
        self.mw.destroy()
        
        
        
class AdminDetails:
    def __init__(self, admin_obj):
        self.mw = tkinter.Tk()
        self.mw.eval('tk::PlaceWindow . center')
        self.mw.geometry("800x400")
        self.mw.title("Admin Details "+admin_obj.get_first_name() + " " + admin_obj.get_last_name())
        
        
        
        tkinter.Label(self.mw, text = "Firstname:").grid(row=3, column=1)
        self.fname_entry = tkinter.Entry(self.mw, width=20)
        self.fname_entry.insert(0, admin_obj.get_first_name())
        self.fname_entry.grid(row=3, column=2)
        
        tkinter.Label(self.mw, text = "Lastname:").grid(row=4, column=1)
        self.lname_entry = tkinter.Entry(self.mw, width=20)
        self.lname_entry.insert(0, admin_obj.get_last_name())
        self.lname_entry.grid(row=4, column=2)
        
        tkinter.Label(self.mw, text = "Address:").grid(row=5, column=1)
        
        address = admin_obj.get_address();
        
        tkinter.Label(self.mw, text = "House No:").grid(row=6, column=1)
        
        self.house_no_entry = tkinter.Entry(self.mw, width=20)
        self.house_no_entry.insert(0, address[0])
        self.house_no_entry.grid(row=6, column=2)
        
        tkinter.Label(self.mw, text = "Street:").grid(row=7, column=1)
        self.street_entry = tkinter.Entry(self.mw, width=20)
        self.street_entry.insert(0, address[1])
        self.street_entry.grid(row=7, column=2)
        
        
        tkinter.Label(self.mw, text = "City:").grid(row=8, column=1)
        self.city_entry = tkinter.Entry(self.mw, width=20)
        self.city_entry.insert(0, address[2])
        self.city_entry.grid(row=8, column=2)
        
        tkinter.Label(self.mw, text = "Postcode:").grid(row=9, column=1)
        self.postcode_entry = tkinter.Entry(self.mw, width=20)
        self.postcode_entry.insert(0, address[3])
        self.postcode_entry.grid(row=9, column=2)
        
        
        self.update_btn = tkinter.Button(self.mw, text ="Update Details", command =lambda: 
                                         self.saveAdminDetails(admin_obj, self.fname_entry.get(), self.lname_entry.get(),
                                                                  [self.house_no_entry.get(), self.street_entry.get(), self.city_entry.get(),
                                                                   self.postcode_entry.get()]))
        self.update_btn.grid(row=10, column=2)
        
        
    def saveAdminDetails(self, admin_obj, fname, lname, address):
        bank_system_obj.updateAdminDetails(admin_obj, fname, lname, address)
        tkinter.messagebox.showinfo("Success", "Admin details updated successfully")
        self.mw.destroy()
        
        
            
        
        

bank_system_obj = BankSystem()
AdminLogin()











