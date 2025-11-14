
import time


def Dave():
    Drink = None
    print(f"Welcome to D.A.V.E (Duolingo's Annual Vending Experience), here, you can buy yourself any drink you want, from the ones that we have. Our options are")
    print("A1 - Pepsi             A2 - Pepsi Light")
    print("B1 - Pepsi Lemon       B2 - Pepsi Oreo")
    print("C1 - Pepsi Black       C2 - Pepsi White")
    print("D1 - Pepsi Singapore   D2 - Pepsi Duolingo")

    print("What do you want to get?")
    Choice = input()
    while Drink == None:
        if Choice == "A1":
            Drink = "pepsi"
        elif Choice == "A2":
            Drink = "pepsi light"
        elif Choice == "B1":
            Drink = "pepsi lemon"
        elif Choice == "B2":
            Drink = "pepsi oreo"
        elif Choice == "C1":
            Drink = "pepsi black"
        elif Choice == "C2":
            Drink = "pepsi white"
        elif Choice == "D1":
            Drink = "pepsi singapore"
        elif Choice == "D2":
            Drink = "pepsi duolingo"
        else:
            print("Please choose an actual drink")
            Choice = input()

    time.sleep(2)

    print(f"Nice job, you chose {Drink}! It had the symbols {Choice}") 
    print("How do you want to pay now, as in you have one choice but i'll give you an illusion of it. Do you want to pay with card or cash")
    Money = input()
    while Money != "card":
        while Money == "cash":
            if Money == "cash":
                print("Sorry, we are not taking cash currently. Please choose another way of payment. cash or card")
                Money = input()
        if Money == "card":
            print("good choice but we only take SOULSSSSS")
            time.sleep(1)
            for x in range(1, 20):
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                time.sleep(0.1)
                print("*(@^#%(@^$!(^$!@(*$(^(@!#!@#!$!@$)")
                x += 1
        else:
            print("that is not a possible choice, please choose either cash or card")
            Money = input()

    return "here is your drink " + Drink + ", and death!"

print(Dave())