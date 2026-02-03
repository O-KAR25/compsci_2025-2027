paylist = []
paylist_year = []
hitory = []
hitory_year = []

def add_song(song_title, song_year):
    song_year = int(song_year)
    paylist.append(song_title)
    paylist_year.append(song_year)
    print(f"Added {song_title}, {song_year} to queue")

def play_next(): 
    if len(paylist) != 0:
        new_var = paylist[0]
        new_yar = paylist_year[0]
        paylist.pop(0)
        paylist_year.pop(0)
        hitory.insert(0, new_var)
        hitory_year.insert(0, new_yar)
        print(f"Now Playing: {new_var}")
    else: 
         print("No songs in queue.")
    
def view_song_year():
    if len(hitory) == 0:
         print("No song is playing.")
    else:
         new_yar = hitory_year[0]
         print(f"The song was released in {new_yar}.")


def play_previous():
    if len(hitory) == 0:
         print("No history available")
    else:
        new_var = hitory[0]
        new_yar = hitory_year[0]
        hitory_year.pop(0)
        hitory.pop(0)
        paylist.insert(0, new_var)
        paylist_year.insert(0, new_yar)
        print(f"Now Playing: {new_var}")

def view_status():
    yr = 0
    yr = int(yr)
    print("The Queue:")
    for songs in paylist:
        print(songs)
        print(paylist_year[yr])
        yr += 1
    if len(paylist) == 0:
        print("No songs played")
    print("")
    print("Recently played:")
    for songs in hitory:
        print(songs)
        print(hitory_year[yr])
        yr += 1
    if len(hitory) == 0:
        print("No songs played")



while True:
    print("Choose what you want to do")
    print("Input 1 if you want to add a song to the queue")
    print("Input 2 if you want to play next song")
    print("Input 3 if you want to see the year the song was made")
    print("Input 4 if you wanna play the previous song")
    print("Input 5 if you wanna a status report")
    print("Write break to end all")
    choice = input()
    if choice == "break":
            break
    elif choice == "1":
        print("Please choose a song you wanna add, input the year after it released (after a coma)")
        add_song(input(), input())
        print("")
    elif choice == "2": 
        play_next()
        print("")
    elif choice == "3":
        view_song_year()
        print("")
    elif choice == "4":
        play_previous()
        print("")
    elif choice == "5":
        view_status()
        print("")
    else:
         print("")
         print("Nuhuhuhhuuh, wrong command")
         print("")
