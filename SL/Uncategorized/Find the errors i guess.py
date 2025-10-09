def deposit(ammount):
    x = balance
    x += ammount
    print("Deposited", ammount, "New balance:", x)
    return x

def withdraw(ammount):
    x = balance
    if x >= ammount:
        x -= ammount
        print("Withdrew", ammount, "New balance:", balance)
    else:
        print("Insufficient funds!")
        return ammount
def bank_app(balance):
    print("Welcome to your bank account!")
    balance = deposit(200)
    balance = withdraw(150)
    balance = withdraw(1200)
    print("Final balance:", balance)

bank_app(1000)    