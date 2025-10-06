class BankAccount:
    def __init__(self, name, balance=0):
        self.name=name
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print("Deposit:",amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Not enough balance")

    def check_balance(self):
        print("Balance:",self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest=self.balance * 0.05
        self.balance+=interest
        print("Interest:",interest)

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        fee = 10
        if amount+fee<=self.balance:
            self.balance-=(amount+fee)
            print(f"Withdrawn: {amount}, Fee: {fee}") 
        else:
            print("Not enough balance")


s=SavingsAccount("Ayesha",1000)
s.deposit(500)
s.add_interest()
s.check_balance()
c=CurrentAccount("Nina",2000)
c.withdraw(500)
c.check_balance()
