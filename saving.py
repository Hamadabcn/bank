# Define a class for the saving account

class SavingAccount:

    # Define a constructor with the account holder name and initial balance
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # Define a method to deposit money into the account
    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nYou deposited: {amount}")

    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nYou withdrew: {amount}")
        else:
            print("\nInsufficient balance")

    # Define a method to display the current balance in the account
    
    def display(self):
        print(f"\nThe account of {self.name} has a balance of {self.balance}")
        