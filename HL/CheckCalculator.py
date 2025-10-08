
FullPrice = 10
FoodPriceCalc1 = 0 
FIL_list = ["Burger","hot Dog","chicken","kfc","Strips"]
Inp = "kfc"

def FoodPrice(FoodInput): 
    continueation = False
    while continueation == False:
        if FoodInput in FIL_list:
            continueation = True
        else:
            continueation = False
            FoodInput = input("Try again")


    if continueation == True:

        if FoodInput == "Burger":
            FoodPriceCalc = 20.99
            return FoodPriceCalc
        elif FoodInput == "hot Dog":
            FoodPriceCalc = 1.99 
            return FoodPriceCalc
        elif FoodInput == "chicken" or "kfc" or "Strips":
            FoodPriceCalc = 15.99
            return FoodPriceCalc
        else:
            continueation = False
            return continueation
        

def eating(now): 
        
    if now == "yes":
        FoodPrice (input("what else do you want to eat?"))
    else: 
        print("Your total is " + FoodPriceCalc1 + " dollars my friend")
        Inp = "BOOOOOOOMM"
        return Inp

    
while Inp in FIL_list:
        eating(input("wanna continue?"))
        
       

Inp = input(FoodPrice("What food you want"))
Food = FoodPrice(Inp)
FoodPriceCalc1 += Food


        