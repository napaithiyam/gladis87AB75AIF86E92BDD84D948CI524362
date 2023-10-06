'''Impement a class called BankAccount that represents a banck account. The class should have private
attributes for account number,account holder name,and account balance.Include methods to
deposit money,withdraw money,and display the account balance.Ensure that the account balance
cannot be accessed directly from outside the class. write a program to create an instance of the
BankAccount class and test the deposit and withdrawal functionlaity.'''


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Creating an instance of the BankAccount class
account = BankAccount("1234567890","John Doe",1000.0)

# Testing deposit and withdrawal functionality
account.display_balance()  # Display initial balance
account.deposit(500.0)     # Deposit $500
account.withdraw(200.0)    # Withdraw $200
account.display_balance()  # Display updated balance