import time



def TheSortingHat(person,interestwol,interestssub1,interestssub2,interestssub3):

   
    Scifi = ["math", "compsci"]
    Human = ["geo", "buisness", "tok", "advisory", "english", "psychology"]
    HumanChoice = 0
    ScifiChoice = 0 
    if interestssub1 in Scifi:
        ScifiChoice += 1
    elif interestssub1 in Human:
        HumanChoice += 1
    if interestssub2 in Scifi:
        ScifiChoice += 1
    elif interestssub2 in Human:
        HumanChoice += 1
    if interestssub3 in Scifi:
        ScifiChoice += 1
    elif interestssub3 in Human:
        HumanChoice += 1
    if HumanChoice > ScifiChoice and interestwol == "visual":
        House = "Gryffindor"
    elif HumanChoice > ScifiChoice and interestwol == "kinesthetic":
        House = "Slytherin"
    elif HumanChoice < ScifiChoice and interestwol == "visual":
        House = "Hufflepuff"
    elif HumanChoice < ScifiChoice and interestwol == "kinesthetic":
        House = "Ravenclaw"
    

    print(f"Ah yes, {person}, who are you?")    
    print("What kind of person are you?")
    print("Good or evil? Dorky or not?")    
    print(f"I see you like {interestssub1}, {interestssub2} and {interestssub3}")
    print(f"You also like to learn using {interestwol}")
    print("Let me think who you should be now")
    time.sleep(10)
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print( House + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

TheSortingHat(input("Please input your name").strip, input("Input whether you like Visual or Kinesthetic learning").strip, input("Your favourite 1 subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci )").strip, input("Your favourite second subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci )").strip, input("Your favourite 1 subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci").strip)