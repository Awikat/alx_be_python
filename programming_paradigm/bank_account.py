#Banking operations

class BankAccount:
    def __init__(self, account_balance):


        self.account_balance = account_balance

    def deposit(self, amount):
        self.amount = amount
        #self.amount = input()
        self.account_balance == 0
        return self.account_balance + self.amount

    def withdraw(self, amount):
        self.amount = amount
        return self.account_balance - self.amount
        if self.account_balance < self.amount:
            return "Insufficient funds."
    def display_balance(self):
        return f"Current Balance: {self.account_balance}"
