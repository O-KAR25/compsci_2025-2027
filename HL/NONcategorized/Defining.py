user = int(input("lowkey say a big number"))
begining = 0
price = 1

def number(max): 
    for x in range(0, max):
        price += begining
        begining += 1 
    return price

print(number(user) - 1)