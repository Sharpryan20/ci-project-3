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
    WantToPlay = input("Are you ready to join us in The Hunt? (Yes/No): \n")
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
    Story_Text("appear in the doorway, which is slightly ajar \n", 2)

    OpenDoor = input("Do you open the door? (yes/no): \n")
    if OpenDoor.lower().strip() == "yes":
        Story_Text("The door slowly creeps open revealing an open room,", 2)
        Story_Text("and in the middle of it stands a tall dark figure,", 2)
        Story_Text("a cloak covering the entity from head to toe.", 2)
    elif OpenDoor == "no":
        Story_Text("You walk around and peer through a window", 2)
        Story_Text("for a better look when suddenly a dark figure", 2)
        Story_Text("jumps at the window. Startled, you take a step back.", 2)
        Story_Text("The man gesutres you to come inside.", 2)
        Story_Text("You make your way back around to the door and enter.", 2)
        Story_Text("Your insanity level has increased \n", 2)
        InsanityStats(+1)
        CheckStats()
    else:
        print("Invalid input. Try again")

    Story_Text("The man lifts his hood and points to a chair.", 2)
    Story_Text("You catch on and sit down in the worn chair", 2)
    Story_Text("He throws more wood on the fire and just stands there", 2)
    Story_Text("watching it roar as the flames warm up the room.", 2)
    Story_Text("You begin to feel uneasy as he scurries closer to you.", 2)
    Story_Text(f"So {name}, I see you are finally awake!", 2)
    Story_Text("Do you want to know why you are here? \n", 2)

    AnswerBack = input("Do you answer back? (yes/no) \n")
    if AnswerBack.lower().strip() == "yes":
        Story_Text("You nod and say;'Wait how do you know my name?'", 2)
        Story_Text("'Where am I?'", 2)
    elif AnswerBack == "no":
        Story_Text("You questioned how he knew your name", 2)
        Story_Text("but decided not to say anything.", 2)
    else:
        print("Invalid input. Try again")

    Story_Text("The man paces back and forth, almost to say something", 2)
    Story_Text("'It doesn't matter how I know your name!'", 2)
    Story_Text("He snapped as he twisted his head almost 180 degrees", 2)
    Story_Text("'All that matters is The Hunt can now begin.'", 2)
    Story_Text("he lifted his hands up just as a clap of thunder bellowed", 2)
    Story_Text("almost as if the man had summoned the phenomenon. \n", 2)
    Story_Text("'The Hunt?' You question, your hands shake with fear \n", 2)
    Story_Text("'The hunt is a matter of life and death. Unfortunately", 2)
    Story_Text("you have been assigned the role of prey.", 2)
    Story_Text("You have 8 hours to survive the forest and make it to", 2)
    Story_Text("THE CITADEL!!", 2)
    Story_Text("You will have a weapon of your choosing.", 2)
    Story_Text("The man makes his way over to a locked door.", 2)
    Story_Text("He opens it and reveals a variety of weapons.", 2)
    Story_Text("Axes...", 0)
    Story_Text("Knives...", 0)
    Story_Text("Swords...", 0)
    Story_Text("Pool cue...", 0)

    global item
    item = input("Which weapon do you pick? (Sword, Axe, Knife, Cue, Nothing)")
    Story_Text(f"I see you picked {item}. Good choice", 2)
    Story_Text(f"You pick up {item}. ", 2)
    Story_Text("You turn to ask who the predator is but the man is gone.", 2)
    Story_Text("Any indication that he was here is the cloak bundled up.", 2)
    Story_Text("You bend down and run the cloak through your fingers \n", 2)

    PickUp = input("Do you pick it up? (yes/no) \n")
    if PickUp.lower().strip() == "yes":
        Story_Text("You place the cloak over your shoulders and leave.", 2)
    elif PickUp == "no":
        Story_Text("You stand back up and head to the door.", 2)
    else:
        print("you can't type that")

    Story_Text("As you leave you notice a drawer cracked open slightly. \n", 2)

    OpenDrawer = input("Do you open it? (yes/no) \n")
    if OpenDrawer.lower().strip() == "yes":
        Story_Text("you see a note inside and a photo. It's of you.", 2)
        Story_Text("You unfold the note and it reads; 'I'm sorry.", 2)
        Story_Text("They made me do it, Please forgive me!'\n", 2)
        Story_Text("You put the note in your pocket and walk out the door.", 2)
    elif OpenDrawer == "no":
        Story_Text("You decide not to open it and leave the house. \n", 2)
    else:
        print("Invalid input. Try again.")
    Story_Text("You notice a hanging latern the porch.", 2)
    Story_Text("You take it off the wall and start your journey. \n", 2)

    TheWalk()


def TheWalk():
    Story_Text("It feels like hours have passed since you started.", 2)
    Story_Text("The path strecthed out for ages, you've had nothing", 2)
    Story_Text("to keep you company expect the whistling winds as", 2)
    Story_Text("they raced through the trees.", 2)
    Story_Text("The thunder had stopped but the rain was still hard.\n", 2)
    Story_Text("FINALLY!!! \n", 2)
    Story_Text("The path splits into two.", 2)

    PickDirection = input("Do you go straight or right? (straight/right) \n")
    if PickDirection.lower().strip() == "straight":
        Story_Text("You continue and suddenly hear a rustle.", 2) 

        Story_Text("You turn to see a bush", 2) 

        WalkScenarioOne()       

    elif PickDirection == "right": 

        Story_Text("You walk down the path", 2)  

    else: 

        print("Invalid input. Please try again.") 
    


def WalkScenarioOne():
    FightOne = input("What do you do? (1 Use weapon/2 Carry on walking) (Pick a number) \n")
    if FightOne.lower().strip() == "1":
        Story_Text("You pooke the bush and the rustling stops", 2)
        Story_Text("but a few seconds later a badger jumps at you", 2)
        Story_Text("and scratches you.", 1)
        Story_Text("You lose 1 health and your insanity increases.", 2)
        HealthStats(-1)
        InsanityStats(1)
        CheckStats()
    elif FightOne == "2":
        Story_Text("you quickly scurry past and continue your walk.", 2)
    else:
        print("Invalid input. Please try again.")




PlayGame()

