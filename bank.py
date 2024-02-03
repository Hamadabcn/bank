balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

# global() allows us to modify the variable outside of the current scope
def deposit(n):
    global balance
    balance += n
    
def withdraw(n): 
    global balance
    balance -= n
    
if __name__ == "__main__":
    main()
    