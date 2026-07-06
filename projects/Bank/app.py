

# User table
users = {
    1234:{'name':"Honey","Email":'honeyyaddanapudi@gmail.com','balance':5000,'password':'1234'},
    1235:{'name':"Hansini","Email":'hansini8121@gmail.com','balance':5000,'password':'1235'}
    }


# services
def register(name:str,email:str,initial_deposit:int,password:str):
    pass

def login(account:int,password:str)->bool:
    if account in users:
        if password==users[account]["password"]:
            return True
        return False
    return False

# balance function defination
def balance(account:int)->int:
    curr_amount = users[account]['balance']
    return curr_amount

# withdraw function defination
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount = users[account]['balance']
    # check amount
    if curr_amount >= withdraw_amount:
        users[account]['balance']-= withdraw_amount
        return f"{withdraw_amount} withdrawal successful and \
                    current Balance is {user[account]['balance]}']}"

# Deposit Function Defination
def Deposite(account:int, deposite_amount:int):
    users[account]['balance']-= deposit_amount
    return f"{deposit_amount} Deposit successful and \
                current Balance is {user[account]['balance]}']}"
    

# Transfer Function Defination
def transfer(sender:int, receiver:int, transfer_amount:int):
    if receiver in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transfer_amount:
            users[sender]['balance'] -= transfer_amount
            users[receiver]['balance'] += transfer_amount
            return f"{transfer_amount} Transfer successfu and \
                    Current Balance is{users[sender]['balance']}"
        return "Insufficient Balance"
    return "Receiver account not Found"

# Ministatement Function Defination
def ministatement(account:int):
     print("Your in Ministatement page")


# Logout Function Defination
def logout():
    return "Thank you using small scale bank service, Bye Bye..."


# main
if __name__=="__main__":

    print("Welcome to the small scale bank")
    print("1. Register \n 2.Login")
    choice = int(input("Select your choice:"))
    
    # Calling register function
    if(choice == 1):
        print("Registration Page Under development process....")

    #Calling login function
    elif choice == 2:
        account = int(input("Enter Your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)

        while login_val:
            print("The small scale Bank providing services")
            print("1. Balance \n 2. Withdraw \n 3.Deposite \n \
                  4. Transfer \n 5.Ministatement \n 6. Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                # Call Balance functiion
                current_balance = balance(account = account)
                print(f"Current Balance is:{current_balance}")
            elif choice == 2:
                amount = int(input("Enter your withdraw amount:"))
                # call with draw Function
                res = withdraw(account = account, withdraw_amount = amount)
                print(res)
                # Call Deposit function
                res = deposite(account = account, deposit_amount = amount)
                print(res)


            elif choice == 3:
                amount = int(input("Enter deposit amount: "))
                # call deposit function
                res = deposite(account=account, deposite_amount=amount)
                print(res)

            elif choice == 4:
                receiver = int(input("Enter receiver account number: "))
                amount = int(input("Enter transfer amount: "))
                # call transfer function
                res = transfer(
                    sender=account,
                    receiver=receiver,
                    transfer_amount=amount
                )
                print(res)

            elif choice == 5:
                # call mini statement function
                res = ministatement(account=account)
                print(res)

            elif choice == 6:
                # call logout function
                logout()
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 6.")

    else:
        print("Invalid option! Please select either 1 or 2.")