import time

UserStats = {
    "health": 10,
    "insanity": 0,
    "weapon": None
}


def S_T(text, delay):
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
    S_T("Your new health is: " + str(UserStats['health']), 2)


def InsanityStats(insanityNumber):
    """
    Increases or decreases the users insanity by a specific amount 
    then displays the users with the new insanity score.
    """
    UserStats["insanity"] = UserStats["insanity"] + (insanityNumber)
    S_T("Your insanity level is: " + str(UserStats['insanity']), 2)


def NoHealth():
    """
    This function is called within the CheckStats function.
    If the user has of 0 or below, the player will die and the game 
    will be over.
    """
    S_T("You have been severly injured.", 2)
    S_T("You are too tired to continue.", 2)
    S_T("You can rest now.", 2)
    S_T("The Hunt is Over", 2)


def MaxInsanity():
    """
    This function will be called within the Checkstats function.
    If the users inasity level reaches above 5, the player will halluncinate
    and the game will be over.
    """

    S_T("You start to see things, things that aren't really there.", 2)
    S_T("There is no going back now.", 2)
    S_T("You lose all control over your body and you run off...", 2)
    S_T("Never to be seen again", 2)


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

        S_T("Brillant!! Lets start", 2)

        global name 
        name = input("What is your name? \n")
        S_T(f"Hello {name}... GOODLUCK!!!", 2)
        S_T("HAHAHAHA \n", 2)
        Opening()

    elif WantToPlay == "no":
        print("That's a shame. See you around!")
    else:
        print("I'm sorry. I'm not too sure what you mean. Please try again")


def Opening():
    S_T("You wake up... dazed!", 2)
    S_T("The gloomy forest sets in as you realise you are lost.", 2)
    S_T("The place has a sense of familarity but", 2)
    S_T("you aren't quite sure how.", 2)
    S_T("You stumble to your feet and frantically search", 2)
    S_T("for shelter as the moon slowly rises.", 2)
    S_T("In the distance you see the roof of a small building", 2)
    S_T("peering out behind the trees", 2)
    S_T("The fog has already began to set and you make your", 2)
    S_T("to the dainty, creepy shed", 2)
    S_T("When you approach the door you see a faint orange glow ", 2)
    S_T("appear in the doorway, which is slightly ajar \n", 2)

    OpenDoor = input("Do you open the door? (yes/no): \n")
    if OpenDoor.lower().strip() == "yes":
        S_T("The door slowly creeps open revealing an open room,", 2)
        S_T("and in the middle of it stands a tall dark figure,", 2)
        S_T("a cloak covering the entity from head to toe.", 2)
    elif OpenDoor == "no":
        S_T("You walk around and peer through a window", 2)
        S_T("for a better look when suddenly a dark figure", 2)
        S_T("jumps at the window. Startled, you take a step back.", 2)
        S_T("The man gesutres you to come inside.", 2)
        S_T("You make your way back around to the door and enter.", 2)
        S_T("Your insanity level has increased \n", 2)
        InsanityStats(+1)
        CheckStats()
    else:
        print("Invalid input. Try again")

    S_T("The man lifts his hood and points to a chair.", 2)
    S_T("You catch on and sit down in the worn chair", 2)
    S_T("He throws more wood on the fire and just stands there", 2)
    S_T("watching it roar as the flames warm up the room.", 2)
    S_T("You begin to feel uneasy as he scurries closer to you.", 2)
    S_T(f"So {name}, I see you are finally awake!", 2)
    S_T("Do you want to know why you are here? \n", 2)

    AnswerBack = input("Do you answer back? (yes/no) \n")
    if AnswerBack.lower().strip() == "yes":
        S_T("You nod and say;'Wait how do you know my name?'", 2)
        S_T("'Where am I?'", 2)
    elif AnswerBack == "no":
        S_T("You questioned how he knew your name", 2)
        S_T("but decided not to say anything.", 2)
    else:
        print("Invalid input. Try again")

    S_T("The man paces back and forth, almost to say something", 2)
    S_T("'It doesn't matter how I know your name!'", 2)
    S_T("He snapped as he twisted his head almost 180 degrees", 2)
    S_T("'All that matters is The Hunt can now begin.'", 2)
    S_T("he lifted his hands up just as a clap of thunder bellowed", 2)
    S_T("almost as if the man had summoned the phenomenon. \n", 2)
    S_T("'The Hunt?' You question, your hands shake with fear \n", 2)
    S_T("'The hunt is a matter of life and death. Unfortunately", 2)
    S_T("you have been assigned the role of prey.", 2)
    S_T("You have 8 hours to survive the forest and make it to", 2)
    S_T("THE CITADEL!!", 2)
    S_T("You will have a weapon of your choosing.", 2)
    S_T("The man makes his way over to a locked door.", 2)
    S_T("He opens it and reveals a variety of weapons.", 2)
    S_T("Axes...", 0)
    S_T("Knives...", 0)
    S_T("Swords...", 0)
    S_T("Pool cue...", 0)

    global item
    item = input("Which weapon do you pick? (Sword, Axe, Knife, Cue, Nothing)")
    S_T(f"I see you picked {item}. Good choice", 2)
    S_T(f"You pick up {item}. ", 2)
    S_T("You turn to ask who the predator is but the man is gone.", 2)
    S_T("Any indication that he was here is the cloak bundled up.", 2)
    S_T("You bend down and run the cloak through your fingers \n", 2)

    PickUp = input("Do you pick it up? (yes/no) \n")
    if PickUp.lower().strip() == "yes":
        S_T("You place the cloak over your shoulders and leave.", 2)
    elif PickUp == "no":
        S_T("You stand back up and head to the door.", 2)
    else:
        print("you can't type that")

    S_T("As you leave you notice a drawer cracked open slightly. \n", 2)

    OpenDrawer = input("Do you open it? (yes/no) \n")
    if OpenDrawer.lower().strip() == "yes":
        S_T("you see a note inside and a photo. It's of you.", 2)
        S_T("You unfold the note and it reads; 'I'm sorry.", 2)
        S_T("They made me do it, Please forgive me!'\n", 2)
        S_T("You put the note in your pocket and walk out the door.", 2)
    elif OpenDrawer == "no":
        S_T("You decide not to open it and leave the house. \n", 2)
    else:
        print("Invalid input. Try again.")
    S_T("You notice a hanging latern the porch.", 2)
    S_T("You take it off the wall and start your journey. \n", 2)

    TheWalk()


def TheWalk():
    """
    This function is the second part of the Game where the
    player has just left the house.
    There will consist nested if/else statements as the player progresses."
    """
    S_T("It feels like hours have passed since you started.", 2)
    S_T("The path strecthed out for ages, you've had nothing", 2)
    S_T("to keep you company expect the whistling winds as", 2)
    S_T("they raced through the trees.", 2)
    S_T("The thunder had stopped but the rain was still hard.\n", 2)
    S_T("FINALLY!!! \n", 2)
    S_T("The path splits into two.", 2)

    PickDirection = input("Do you go straight or right? (straight/right) \n")
    if PickDirection.lower().strip() == "straight":
        S_T("You continue and suddenly hear a rustle.", 2) 

        S_T("You turn to see a bush", 2) 

        WalkScenarioOne()       

    elif PickDirection == "right": 

        S_T("You turn right and you start walking.", 2)
        S_T("You start hearing things, like screeches.", 2)
        S_T("The noises get louder and louder, becoming", 2)
        S_T("near impossible to even hear your thoughts.", 2)
        WalkScenarioTwo()  

    else: 
        print("Invalid input. Please try again.") 
    

def WalkScenarioOne():
    """
    This is the first scenario for TheWalk() function
    Will only be called if player continues straight in
    the PickDirection if/else statement.
    """
    FightOne = input("What do you do? (1 Use weapon/2 Carry on walking) (Pick a number) \n")
    if FightOne.lower().strip() == "1":
        S_T("You pooke the bush and the rustling stops", 2)
        S_T("but a few seconds later a badger jumps at you", 2)
        S_T("and scratches you.", 1)
        S_T("You lose 1 health and your insanity increases.", 2)
        HealthStats(-1)
        InsanityStats(1)
        CheckStats()
    elif FightOne == "2":
        S_T("you quickly scurry past and continue your walk.", 2)
    else:
        print("Invalid input. Please try again.")


def WalkScenarioTwo():
    """
    This function will only be called if the player
     turns right from the PickDirection question.
    """
    FightTwo = input("What do you do? (1 Stand still/ 2 Run!) \n")
    if FightTwo.lower().strip() == "1":
        S_T("The ground starts rumbling as you stand frozen.", 2)
        S_T("Then out of nowhere, a herd of deers come stampeding", 2)
        S_T("towards you. You crouch down to avoid a blow.", 2)
        S_T("However that wasn't wise. The deers trampled you as", 2)
        S_T("you laid hopeless. You lose 3 health.", 2)
        HealthStats(-3)
        CheckStats()
    elif FightTwo == "2":
        S_T("You bolt in the opposite direction of the sounds,", 2)
        S_T("trying your best to out run the predators.", 2)
        S_T("However it wasn't a predator but a herd of deer.", 2)
        S_T("They were sprinting at full spped and almost", 2)
        S_T("immediately ran past you. One wasn't quite as fast", 2)
        S_T("and was beginning to trail behind. You wait for it", 2)
        S_T("to get closer to you and as it apporaches you grab his", 2)
        S_T("antlers and hop on the back.", 2)
        S_T("Now startled, the deer speeds up and within time", 2)
        S_T("has caught back up to the herd.", 2)
        S_T("'What was they running from?'", 2)
        S_T("You hop off the deer and head back, realising you", 2)
        S_T("had dropped your weapon.", 2)
    else:
        print("Invalid input. Please try again")


PlayGame()

