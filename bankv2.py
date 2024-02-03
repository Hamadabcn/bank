class Account:
    def __init__(self):
        self._balance = 0

# The @property decorator allows a function to be accessed like an attribute
    @ property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
        
    def withdraw(self, n):
        self._balance -= n
def main():
    account = Account()
    print("Balance", account.balance)
    account.deposit(500)
    account.withdraw(50)
    print("Balance", account.balance)
    
if __name__ == "__main__":
    main()