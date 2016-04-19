# program to create and manipulate a personal bank ccount
class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name 
    def __repr__(self):    
        return "The name is %s, the balance is $%.2f" % (self.name, self.balance)  
    def show_balance(self):
        print "The balance is $%.2f" % (self.balance)
    def deposit(self, amount):
        self.amount = amount
        if amount <= 0:
            print "The amount being entered with error"
            return
        else:
            print "The amount is $%.2f" % (self.amount)  
            self.balance += amount 
            self.show_balance
    def withdraw(self, amount):
        if amount > self.balance:
            print "The error amont was trying to be withdrawn"
        else:
            print "The amount is $%.2f" % (self.amount)
            self.balance -= amount
            self.show_balance
            
            
my_account= BankAccount("Tatyana")   
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
#print my_account
