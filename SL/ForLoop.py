
the_input = int(input("Pick a number of loops"))
y = 0
number = 0
x = 1
other_number = 0
for i in range(1, the_input + 1):
    if i % 2 == 0:
        print("This number (" + str(i) + ") is divisible by zero")
    else:
        print("This number (" + str(i) + ") is not divisible by zero")
    i += 1


while y in range(0, the_input + 1):
    if y % 2 == 0:
        print(f"This number {(y)} is divisible by zero")
    else:
        print(y)
    y += 1

while x in range(0, the_input + 1):
    number += x
    x += 1
print(f"The final number is {number}")


for z in range(0, the_input + 1):
    other_number += z 
print(f"this is the same number but in a 'for' function ({(other_number)})")