def Fibs(number):
    if number == 1:
        return 0
    if number == 2: 
        return 1
    return Fibs(number - 1) + Fibs(number - 2)
    

print(Fibs(int(input("What number do chu went? "))))