
# IB DP CompSci - First Class Exercise: Data Types

# For each variable below, write a comment with what kind of thing it is (int, float, str, or bool)
number = 7  #int
decimal = 3.5 #float
word = "hello" #str
is_sunny = True #bool
print(type(number))
print(type(decimal))
print(type(word))
print(type(is_sunny))
print("joe")
# Change the values to the type shown in the comment?
age = 15      # Change to int
score = "High"      # Change to str
rain = False  # Change to bool
height = 1.75 # Change to float
print(type(age))
print(type(score))
print(type(rain))
print(type(height))

# What will be printed?
print(type(2 + 2))   #int
print(type("5" + "5")) # string
print(type(3.0 + 1)) #float
print(type(True)) #bool
# Write your guesses as comments, then run and check


print("5" + "5")

num1 = 12
number2 = num1 % 2 
number3 = num1 % 3 

nothing = number2 and number3 == 0 
if nothing == 0:
    print("true")
else:
    print("false")

