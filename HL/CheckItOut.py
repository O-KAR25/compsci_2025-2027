Cycle = True
Option_list = ["chicken", "oatmeal", "pizza", "hot dog"]
pricetotal = 0
chickenprice = 10
oatmealprice = 5 
pizzaprice = 20
hotdogprice = 4
maybe = True
def food(foodchosen):
    if foodchosen in Option_list:
        confirmation = input(f"You want {(foodchosen)}?")
        if confirmation == "yes":
            if foodchosen == "chicken":
                price = chickenprice
                return price
            elif foodchosen == "oatmeal":
                price = oatmealprice
                return price
            elif foodchosen == "pizza":
                price = pizzaprice
                return price
            elif foodchosen == "chicken":
                price = hotdogprice
                return price
        else: 
             print(f"Your final price to pay is {(pricetotal)}")
             return "False"   
    else:
        foodchosen = input("Choose actual food that you have a choice to get")

            
def Reuse(maybe):
    if maybe == "yes":
        maybe = True
        return maybe
    else:
        maybe = False
        print(f"Your final price to pay is {(pricetotal)}")
        return maybe    






while Cycle == True:
    
    Cont1 = food(input("What food you want?"))
    pricetotal += Cont1
    Cont = Reuse(input("Do you wanna continue?"))
    if Cont == Reuse(maybe=False) and Cont1 == food("False"):
        Cycle = False
