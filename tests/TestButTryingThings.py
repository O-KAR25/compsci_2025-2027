def Richness(): #one function to hold them all (lotr style)
    wallet_money = float(input("How much are you gonna spend? ")) #money to be used for it 
    total_funds = wallet_money #making a new variable that will work as the new money holder 
    moneyspent = float(0) #how much money spent
    item_list = [] #item list (empty as people will pit things in during the transaction)
    




    while True: #looping it all
        
        itemtobuy = input(f"What'u wanna buy? ").strip() #the items a person wants to buy
        if itemtobuy.lower() == "done": #ending function
            print(f"shopping complete. you spent {(moneyspent)}. you bought {(listing_the_item(item_list))}. you have {(total_funds)} left") 
            break

        try:
            price_of_item = float(input("How much does it cost lad? ")) #taking the price of the item
        except ValueError:
            price_of_item = input("put actual value") #giving a user a chance to repent (only one though in case of misspeling or typo)
            

       #the transaction or lack of it because of the money owned
        if total_funds - price_of_item < 0:
            print("too brokey, try again")
        else: 
            total_funds -= price_of_item #money left
            moneyspent += price_of_item  #how much money spent
            item_list.append(itemtobuy) #adding things to the list of items bought
            print(f"you have {(total_funds)} left") #informing of money left

        def listing_the_item():
            for item in item_list:
                print(f"{(item)}, ")
#running the whole thing
Richness()