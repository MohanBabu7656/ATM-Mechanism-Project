# Class definition for Account
class Account:
    # Class variable for the bank name, obtained as user input
    bankName = input("Enter bank name : ")

    # Constructor to initialize account details
    def __init__(self):
        # Private attributes to store account information
        self.__accName = input("Enter account holder name : ")
        self.__accNo = int(input("Enter account no : "))
        self.__accType = input("Account type (savings/current) : ")
        self.__accBal = int(input("Enter initial balance : "))
        self.__ifscCode = input("Enter IFSC code : ")
        self.__cardNumber = int(input("Enter card number : "))
        self.__cvv = int(input("Enter CVV behind card : "))
        self.__expiryDate = input("Enter expiry date : ")
        self.__pin = int(input("Create pin : "))

    # Getter methods to retrieve private attributes
    def getAccName(self):
        return self.__accName

    def getAccNo(self):
        return self.__accNo

    def getAccType(self):
        return self.__accType

    def getAccBal(self):
        return self.__accBal

    # Method to deposit money into the account
    def deposit(self, amount):
        self.__accBal += amount
        print("Deposited Successfully")
        print("Updated Account Balance : ", self.getAccBal())

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.getAccBal():
            self.__accBal -= amount
        else:
            print('Insufficient Balance, Try again...')
        print("Updated Account Balance : ", self.getAccBal())

    # Method to display account details
    def display(self):
        print("\nAccount Details...")
        print("Account Holder :", self.getAccName())
        print("Account Number :", self.getAccNo())
        print("Account Type :", self.getAccType())
        print("Account Balance :", self.getAccBal())
        print("Bank Name :", self.bankName)

# Importing the Account class from the Bank module
from Bank import Account

# List to store multiple account objects
accounts = []

# Input for the number of accounts to create
n = int(input("Enter number of accounts : "))
for NoOfAccounts in range(n):
    # Creating an instance of the Account class and adding it to the accounts list
    account = Account()
    accounts.append(account)

# Menu for user interaction
print("Select any Option...")
print('Press 1 for Account Name')
print('Press 2 for Account Number')
print('Press 3 for Account Balance')
print('Press 4 for Account Deposit')
print('Press 5 for Account Withdraw')
print('Press 6 for Account Details')
print('Press 7 for Account Type')
print('Press 8 for Change PIN')
print('Press 0 for Exit')

# Function to check for a valid account based on card number and PIN
def checkAccount(accounts, cardNumber, pin):
    for account in accounts:
        if account._Account__cardNumber == cardNumber and account._Account__pin == pin:
            return account
    return None

# Menu loop for user interaction
while True:
    opt = int(input('\nEnter your Choice : '))

    # Option handling based on user input
    if opt == 1:
        # Retrieve account name for a valid card number and PIN
        cardNumber = int(input('Enter Card Number: '))
        pin = int(input('Enter PIN: '))
        account = checkAccount(accounts, cardNumber, pin)
        if account:
            print("Account Holder:", account.getAccName())
        else:
            print("Invalid Card Number or PIN")
    elif opt == 2:
        # Retrieve account number for a valid card number and PIN
        # (similar pattern for other options)
        # ...
    elif opt == 0:
        # Exit the program
        break
    else:
        # Handle invalid input
        print('Invalid Input, Try again !')

# Display a thank you message when the user exits the program
print('\nThank you, Visit again...')
