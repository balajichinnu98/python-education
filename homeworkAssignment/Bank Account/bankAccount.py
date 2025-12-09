class BankAccount:
    
    def __init__(self,owner,balance):
       self.owner = owner
       self.balance = balance

    def deposit(self,amount):
      self.balance = self.balance + amount
      return self.balance 
        

    def withdraw(self,amount): 
        if self.balance < amount:
            return "Insufficient funds"
        else:
         self.balance = self.balance - amount
         return self.balance
        

userAccount = BankAccount("Alice", 1000)
print("Account owner is {} and their deposit is {}".format(userAccount.owner, userAccount.deposit(500)))
print("Account owner is {} and their deposit is {}".format(userAccount.owner, userAccount.withdraw(600)))
print("Account owner is {} and their deposit is {}".format(userAccount.owner, userAccount.deposit(3000)))
print("Account owner is {} and their deposit is {}".format(userAccount.owner, userAccount.withdraw(500)))