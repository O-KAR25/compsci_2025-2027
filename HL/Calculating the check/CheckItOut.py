#Variables

Cycle = True
Option_list = ["chicken", "oatmeal", "pizza", "hot dog"]
pricetotal = 0
chickenprice = 10
oatmealprice = 5 
pizzaprice = 20
hotdogprice = 4
maybe = True

#Function for the prize

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
             print(f"Your final price to pay is {(pricetotal)}")
             return "False"   
    else:
        foodchosen = input("Choose actual food that you have a choice to get")

#Function for continuation 


def Reuse(maybe):
    if maybe == "yes":
        maybe = True
        return maybe
    else:
        maybe = False
        print(f"Your final price to pay is {(pricetotal)}")
        return maybe    


#the loop

while Cycle == True:
    
    Cont1 = food(input("What food you want?"))
    if Cont1 == None:
        Cont1 = int(0)
    pricetotal += int(Cont1)
    Cont = Reuse(input("Do you wanna continue?"))
    if Cont == Reuse(maybe==False) or Cont1 == food("False"):
        break
        
