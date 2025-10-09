
FIL = ["Burger","hot Dog","chicken","kfc","Strips"]
Cycle = "kfc"

while Cycle in FIL:


    def FoodPrice(FoodInput): 
        continueation = False
        while continueation == False:
            if FoodInput in FIL:
                continueation = True
            else:
                continueation = False
                FoodInput = input("Try again ")


        if continueation == True:

            if FoodInput == "Burger":
                FoodPriceCalc = 20.99
                FoodPriceCsalc1 += FoodPriceCalc
                eating(input("Wann keep eating?"))
                return FoodPriceCalc
            elif FoodInput == "hot Dog":
                FoodPriceCalc = 1.99 
                FoodPriceCalc1 += FoodPriceCalc
                eating(input("Wann keep eating?"))
                return FoodPriceCalc
            elif FoodInput == "chicken" or "kfc" or "Strips":
                FoodPriceCalc = 15.99
                FoodPriceCalc1 += FoodPriceCalc
                eating(input("Wann keep eating? "))
                return FoodPriceCalc
            else:
                continueation = False
                return continueation

    def eating(keep_eating): 
            
        if keep_eating == "yes":
            FoodPrice (input("what else do you want to eat? "))
        else: 
            print("Your total is " + FoodPriceCalc1 + " dollars my friend")
            Cycle = "BOOOOOOOMM"
            return Cycle 

    FoodPrice(input("Yo what food you want"))

        

    


        