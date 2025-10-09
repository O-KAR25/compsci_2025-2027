person_age = 10
parents =  False
height = 2

batman = (person_age > 12 and person_age < 60 and height > 1.35) or (person_age < 13 and parents == True and height > 1.35)

if batman == True:
    print("you can go")
else:
    print("no parents?")

