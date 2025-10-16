Random1 = 1
Random2 = 0
number = 1

def Loop():
    while True:
        if Random1 > Random2:
            number = Random2 + Random1
            Random2 = number
            print(Random2)
            if Random2 > 100:
                print("too many numbers")
                break
        if Random2 > Random1:
            number = Random1 + Random2
            Random1 = number
            print(Random1)
            if Random1 > 100:
                print("too many numbers")
                break
        
 

print(Loop())