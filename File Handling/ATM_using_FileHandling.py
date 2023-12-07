# Function to create a new account and add it to the data
def create_account():
    # Open the file in append mode
    f = open("accounts.txt", "a")

    # Gather user input for account details
    accName = input("Enter account holder name : ")
    accNumber = input("Enter account holder number : ")
    accType = input("Enter Type of account : ")
    accBalance = input("Enter initial account balance : ")
    IFSCcode = input("Enter IFSC code : ")
    CreditCard = input("Enter Credit Card number : ")
    CVV = input("Enter CVV : ")
    EXPdate = input("Enter Expire Date : ")
    PIN = input("Enter pin : ")

    # Write the account information to the file
    f.write("accName : " + accName + " , " + "accNumber : " + accNumber + " , " + "accType : " + accType)
    f.write(" , accBalance : " + accBalance + " , IFSCcode : " + IFSCcode + " , CreditCard : " + CreditCard)
    f.write(" , CVV : " + CVV + " , EXPdate : " + EXPdate + " , Pin : " + PIN + '\n')

    print("Account created successfully.")
    f.close()


def check_account(CreditCard):
    # Open the file in read mode
    f = open("accounts.txt", "r")

    # Iterate through each line in the file
    for check in f:
        account_info = check.split(" , ")
        account = {}

        # Extract key-value pairs from the account information
        for item in account_info:
            key, value = item.split(" : ")
            account[key.strip()] = value.strip()

        # Check if the credit card number matches
        if account["CreditCard"] == CreditCard:
            # Prompt user for pin verification
            Pin = input("Enter credit card pin :")

            # Check if the pin is valid
            if account["Pin"] == Pin:
                return account
            else:
                print("Invalid pin")
    f.close()


def balance_enquiry(got_it):
    # Display the account balance
    print("Account balance:", got_it["accBalance"])


def display_details(got_it):
    # Display all details of the account
    for x, y in got_it.items():
        print(x + " : " + y)


def withdraw(got_it, amount):
    # Withdraw money from the account
    balance = float(got_it["accBalance"])

    if amount <= balance:
        got_it["accBalance"] = str(balance - amount)
        print("Withdrawn successfully")
        update(got_it)
    else:
        print("Insufficient Balance")


def deposit(got_it, amount):
    # Deposit money into the account
    amount = float(amount)

    if amount >= 0:
        balance = float(got_it["accBalance"])
        got_it["accBalance"] = str(balance + amount)
        print("Deposited successfully")
        update(got_it)
    else:
        print("Invalid amount")


def pin_change(got_it, new_pin):
    # Change the account PIN
    pin = got_it["Pin"]

    if pin == new_pin:
        print("Previous pin matched")
    else:
        got_it["Pin"] = new_pin
        print("Pin changed successfully")
        update(got_it)


def update(got_it):
    # Open the file in read mode
    f = open("accounts.txt", "r")
    accounts = []

    # Iterate through each line in the file
    for line in f:
        account_info = line.strip().split(" , ")
        account = {}

        # Extract key-value pairs from the account information
        for item in account_info:
            key, value = item.split(" : ")
            account[key.strip()] = value.strip()

        # Check if the current account matches the updated account
        if account["CreditCard"] == got_it["CreditCard"] and account["accNumber"] == got_it["accNumber"]:
            account_str = ""

            # Convert the updated account dictionary to a string
            for key, value in got_it.items():
                account_str += key + " : " + value + " , "

            account_str = account_str[:-3]
            accounts.append(account_str)
        else:
            accounts.append(line)

    f.close()

    # Open the file in write mode
    f = open("accounts.txt", "w")

    # Write the updated account list to the file
    for account in accounts:
        f.write(account)

    f.close()


# Menu Card
CreditCard = input("Enter credit card number :")
got_it = check_account(CreditCard)

# Check if the account exists
if got_it:
    def operation():
        print("1. Create Account")
        print("2. Balance Enquiry")
        print("3. Display Details")
        print("4. Withdraw")
        print("5. Deposit")
        print("6. Pin Change")
        print("7. Exit")

        opt = int(input("Choose option : "))
        print()

        if opt == 1:
            create_account()
        elif opt == 2:
            balance_enquiry(got_it)
        elif opt == 3:
            display_details(got_it)
        elif opt == 4:
            amount = float(input("Enter amount to withdraw :"))
            withdraw(got_it, amount)
        elif opt == 5:
            amount = float(input("Enter amount to deposit :"))
            deposit(got_it, amount)
        elif opt == 6:
            new_pin = input("Enter new pin :")
            pin_change(got_it, new_pin)

        print("Continue : 1\nStop : 2")
        choice = int(input("Choose choice: "))

        if choice == 1:
            operation()
        else:
            print('\nThank you, Visit again...')

            return


    operation()
else:
    print("Account not found")
