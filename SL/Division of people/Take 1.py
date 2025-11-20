import time



def TheSortingHat():
   
    Scifi = ["math", "compsci"]
    Human = ["geo", "buisness", "tok", "advisory", "english", "psychology"]
    HumanChoice = 0
    ScifiChoice = 0 
    House = "Not accepted, get outha hea"

    print("Please input your name")
    person = input()
    print("Input whether you like Visual or Kinesthetic learning")
    interestwol = input()
    while True:
        if interestwol == "visual" or "kinesthetic":
            break
        else:
            print("Choose either visual or kinesthetic")
            interestwol = input()

    print("Your favourite 1 subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci )")
    interestssub1 = input()
    while True: 
        if interestssub1 in Scifi:
            ScifiChoice += 1
            break
        elif interestssub1 in Human:
            HumanChoice += 1
            break
        else:
            print("choose an actual subject that you can choose")
            interestssub1 = input()
            

    print("Your favourite second subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci )")
    interestssub2 = input()
    while True:
        if interestssub2 in Scifi:
            ScifiChoice += 1
            break

        elif interestssub2 in Human:
            HumanChoice += 1
            break

        else:
            print("choose an actual subject that you can choose")
            interestssub2 = input()

    print("Your favourite 3rd subject (subjects to choose from geo, buisness, tok, advisory, english, psychology, math and compsci")
    interestssub3 = input()
    while True:

        if interestssub3 in Scifi:
            ScifiChoice += 1
            break

        elif interestssub3 in Human:
            HumanChoice += 1
            break 
        else:
            print("choose an actual subject that you can choose")
            interestssub3 = input()

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
    print("")
    time.sleep(5)
    print("")    
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("")
    time.sleep(0.1)
    print("intense music starts playing")
    time.sleep(2)
    print( House + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

TheSortingHat()