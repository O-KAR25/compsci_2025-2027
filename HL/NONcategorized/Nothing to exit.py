text = True

while text == True:
    word = input("Say a word")
    if isinstance(word, str):
        text = True
        print("You just said " + word + ", good for you my friend")
    else:
        text = False
