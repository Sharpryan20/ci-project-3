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

def HealthStats(healthNumber):
    """
    Increases or decreases the users health by a specified amount
    then displys the users with the new health score.
    """

    UserStats["health"] = UserStats["health"] + (healthNumber)
    Story_Text("Your new health is: " + str(UserStats['health']), 2)

def InsanityStats(insanityNumber):
    """
    Increases or decreases the users insanity by a specific amount 
    then displays the users with the new insanity score.
    """
    UserStats["insanity"] = UserStats["insanity"] + (insanityNumber)
    Story_Text("Your insanity level is: " + str(UserStats['insanity']), 2)

def NoHealth():
    """
    This function is called within the CheckStats function.
    If the user has of 0 or below, the player will die and the game 
    will be over.
    """
    Story_Text("You have been severly injured.", 2)
    Story_Text("You are too tired to continue.", 2)
    Story_Text("You can rest now.", 2)
    Story_Text("The Hunt is Over", 2)

def MaxInsanity():
    """
    This function will be called within the Checkstats function.
    If the users inasity level reaches above 5, the player will halluncinate
    and the game will be over.
    """

    Story_Text("You start to see things, things that aren't really there.", 2)
    Story_Text("There is no going back now.", 2)
    Story_Text("You lose all control over your body and you run off...", 2)
    Story_Text("Never to be seen again", 2)

def CheckStats():
    """
    Will be called any time the users stats are affected.
    If health drops below 0 or insanity is higher than 5, then
    the correct function will be called and it will be 
    game over.
    """

    if UserStats["health"] <= 0:
        NoHealth()
    
    if UserStats["insanity"] >= 5:
        MaxInsanity()


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
        Story_Text("The door slowly creeps open revealing an open room," 1)
        Story_Text("and in the middle of it stands a tall dark figure,", 1)
        Story_Text("a cloak covering the entity from head to toe.", 2)
    elif OpenDoor == "no":
        Story_Text("You walk around and peer through a window", 1)
        Story_Text("for a better look when suddenly a dark figure", 1)
        Story_Text("jumps at the window. Startled, you take a step back.", 1)
        Story_Text("The man brings his hand to the window and gesutres you to come inside.", 1)
        Story_Text("You make your way back around to the door and enter.", 1)
        Story_Text("Your insanity level has increased", 2)
    else:
        print("Invalid input. Try again")
    

PlayGame()

