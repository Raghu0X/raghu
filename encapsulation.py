class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Current balance: ${self.__balance}")

account1 = BankAccount(1000)  

account1.deposit(500)       
account1.withdraw(200)     
account1.withdraw(1500)     
account1.display_balance()  
