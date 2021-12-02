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
        Story_Text("HAHAHAHA", 2)

    elif WantToPlay == "no":
        print("That's a shame. See you around!")
    else:
        print("I'm sorry. I'm not too sure what you mean. Please try again")

PlayGame()

