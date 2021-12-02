import time

UserStats = {
    "health": 10,
    "insanity": 0,
    "weapon": None
}

def Story_Text(text, delay):
    """
    Prints out a line of text for the story and delays
    the next line for a certain amount of time.
    """

    print(text)
    time.sleep(delay)

def Stats(healthNumber):
    """
    Increases or decreases the users health by a specified amount
    then displys the users with the new health score.
    """

    UserStats["health"] = UserStats["health"] + (healthNumber)

def PlayGame():
    """
    Function called at the end of the run.py file 
    The only function called on a global scale.
    """
    print('''\033[94m
    _______ ___   ___ ______
   |__   __|   | |   |    __|
      | |  |   |_|   |   |__
      | |  |    _    |    __|
      | |  |   | |   |   |__
      |_|  |___| |___|______|.\033[96m
   ___   ___ ___   ___ ____     __ _______
  |   | |   |   | |   |    \   |  |__   __|
  |   |_|   |   | |   |     \  |  |  | |
  |    _    |   |_|   |      \ |  |  | |
  |   | |   |         |   |\  \|  |  | |
  |___| |___|_________|___| \_____|  |_|
    \033[0m\n''')
    WantToPlay = input("Would you like to join us in The Hunt? (Yes/No): \n")
    if WantToPlay.lower().strip() == "yes":

        Story_Text("Brillant!! Lets start", 2)

        global name 
        name = input("What is your name? \n")
        Story_Text(f"Hello {name}... GOODLUCK!!!", 2)
        Story_Text("HAHAHAHA \n", 2)
        Opening()

    elif WantToPlay == "no":
        print("That's a shame. See you around!")
    else:
        print("I'm sorry. I'm not too sure what you mean. Please try again")

def Opening():
    Story_Text("You wake up... dazed!", 2)
    Story_Text("The gloomy forest sets in as you realise you are lost.", 2)
    Story_Text("The place has a sense of familarity but", 2)
    Story_Text("you aren't quite sure how.", 2)
    Story_Text("You stumble to your feet and frantically search", 2)
    Story_Text("for shelter as the moon slowly rises.", 2)
    Story_Text("In the distance you see the roof of a small building", 2)
    Story_Text("peering out behind the trees", 2)
    Story_Text("The fog has already began to set and you make your", 2)
    Story_Text("to the dainty, creepy shed", 2)
    Story_Text("When you approach the door you see a faint orange glow ", 2)
    Story_Text("appear in the gap of the doorway, which is slightly ajar \n", 2)

    OpenDoor = input("Do you open the door? (yes/no): \n")
    if OpenDoor.lower().strip() == "yes":
        Story_Text("The door slowly creeps open revealing an open room and in the middle", 0.5)
        Story_Text("of it stands a tall dark figure, a cloak covering the entity from head to toe", 2)
    

PlayGame()

