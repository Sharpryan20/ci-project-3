import time

UserStats = {
    
    "health": 10,
    "insanity": 0,
    "weapon": None
}

ANSWER = " "
cower = ("cower")
run = ("run", "2")
yes = ("yes")
no = ("no")
stand = ("stand", "1")
straight = ("straight")
right = ("right")
use_weapon = ("weapon", "1")
carry_walking = ("walk", "2")
chanting = ("chanting", "1")
fire = ("fire", "2")
potion_health = ("health", "1")
potion_insanity = ("insanity", "2")
north = ("north", "n")
east = ("east", "e")
south = ("south", "s")
west = ("west", "w")
wriggle = ("wriggle", "1")
attack = ("attack", "2")


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
    S_T("Your health is: " + str(UserStats['health']), 2)


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
    
    print("Are you ready to join us in The Hunt? (yes/no)")

    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        S_T("Invalid input Please try again.", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        S_T("Brillant!! Lets start", 2)

        global name 
        name = input("What is your name? \n")
        S_T(f"Hello {name}... GOODLUCK!!!", 2)
        S_T("HAHAHAHA \n", 2)
        Opening()
    elif ANSWER in no:
        print("That's a shame. See you around!")


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

    print("Do you open the door? (yes/no?)")

    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        S_T(f"Invalid input Please try again {name}", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        S_T("The door slowly creeps open revealing an open room,", 2)
        S_T("and in the middle of it stands a tall dark figure,", 2)
        S_T("a cloak covering the entity from head to toe.", 2)
    elif ANSWER in no:
        S_T("You walk around and peer through a window", 2)
        S_T("for a better look when suddenly a dark figure", 2)
        S_T("jumps at the window. Startled, you take a step back.", 2)
        S_T("The man gesutres you to come inside.", 2)
        S_T("You make your way back around to the door and enter.", 2)
        S_T("Your insanity level has increased \n", 2)
        InsanityStats(+2)
        CheckStats()

    S_T("The man lifts his hood and points to a chair.", 2)
    S_T("You catch on and sit down in the worn chair", 2)
    S_T("He throws more wood on the fire and just stands there", 2)
    S_T("watching it roar as the flames warm up the room.", 2)
    S_T("You begin to feel uneasy as he scurries closer to you.", 2)
    S_T(f"So {name}, I see you are finally awake!", 2)
    S_T("Do you want to know why you are here? \n", 2)

    print("Do you answer back? (yes/no)")
    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        S_T(f"Invalid input Please try again {name}.", 2)
        ANSWER = input("").lower().strip()
    if ANSWER in yes:
        S_T("You nod and say;'Wait how do you know my name?'", 2)
        S_T("'Where am I?'", 2)
    
    elif ANSWER in no:
        S_T("You questioned how he knew your name", 2)
        S_T("but decided not to say anything.", 2)

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
    item = input("Which weapon do you pick? (Sword, Axe, Knife, Cue, Nothing) \n")
    S_T(f"I see you picked {item}. Good choice", 2)
    S_T(f"You pick up {item}. ", 2)
    S_T("You turn to ask who the predator is but the man is gone.", 2)
    S_T("Any indication that he was here is the cloak bundled up.", 2)
    S_T("You bend down and run the cloak through your fingers \n", 2)
    
    print("Do you pick it up? (yes/no)")
    ANSWER = input("").lower().strip() 
    while ANSWER not in yes and ANSWER not in no: 
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 
    if ANSWER in yes: 
        S_T("You place the cloak over your shoulders and leave.", 2)
    elif ANSWER in no:
        S_T("You stand back up and head to the door.", 2)

    S_T("As you leave you notice a drawer cracked open slightly. \n", 2)

    print("Do you open it? (yes/no)")
    ANSWER = input("").lower().strip() 
    while ANSWER not in yes and ANSWER not in no: 
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 
    if ANSWER in yes:
        S_T("you see a note inside and a photo. It's of you.", 2)
        S_T("You unfold the note and it reads; 'I'm sorry.", 2)
        S_T("They made me do it, Please forgive me!'\n", 2)
        S_T("You put the note in your pocket and walk out the door.", 2)    
    elif ANSWER in no: 
        S_T("You decide not to open it and leave the house. \n", 2)

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

    print("Do you go straight or right? (straight/right)")
    ANSWER = input("").lower().strip()

    while ANSWER not in straight and ANSWER not in right:
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 

    if ANSWER in straight:    
        S_T("You continue and suddenly hear a rustle.", 2)
        S_T("You turn to see a bush", 2) 
        WalkScenarioOne()
    elif ANSWER in right:
        S_T("You turn right and you start walking.", 2)
        S_T("You start hearing things, like screeches.", 2)
        S_T("The noises get louder and louder, becoming", 2)
        S_T("near impossible to even hear your thoughts.", 2)
        WalkScenarioTwo()
    

def TheWalkPartB():
    """
    The second part of the TheWalk() function which both players
    will recieve no matter what path they go down.
    """
    S_T("It starts to get colder the further you walk into the forest.", 2)
    S_T("You begin to fear that there was no end to this nightmare.", 2)
    S_T("And in fact you were destined to die out here.", 2)
    S_T("You try to remember anything as to how you,", 2)
    S_T("ended up here. Why was it so familiar?", 2)
    S_T("Who was that man?", 2)
    S_T("How did he know your name?", 2)
    S_T("Is this some sick joke?", 2)
    S_T("Is this even legal? It can't be?", 2)


def WalkScenarioOne():
    """
    This is the first scenario for TheWalk() function
    Will only be called if player continues straight in
    the PickDirection if/else statement.
    """
    print("What do you do? (1 Use weapon/ 2 Walk)")
    ANSWER = input("").lower().strip()
    while ANSWER not in use_weapon and ANSWER not in carry_walking: 
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in use_weapon:
        S_T("You poke the bush and the rustling stops", 2)
        S_T("but a few seconds later a badger jumps at you", 2)
        S_T("and scratches you.", 1)
        S_T("You lose 2 health and your insanity increases.", 2)
        HealthStats(-2)
        InsanityStats(2)
        CheckStats()
    elif ANSWER in carry_walking:
        S_T("The rustling stops after a few seconds.", 2)
        S_T("you quickly scurry past and continue your walk,", 2)
        S_T("careful not to disturb the beast.", 2)
    
    TheWalkPartB()
    TheWalk1_A()


def TheWalk1_A():
    """
    This function is called
    the player takes the straight path and after 
    TheWalkPartB() is called.
    """
    S_T("The path begins to fade out as nature covers the concrete.", 2)
    S_T("No one has been down here in a while.", 2)
    S_T("Have you chosen the right path?", 2)
    S_T("Is the predator down here?", 2)
    S_T("You try to stay strong.", 2)
    S_T("You have come to far to give up now, surely there is only,", 2)
    S_T("a few hours left to the go.", 2)
    S_T("Your latern begins to flicker ever so slightly.", 2)
    S_T("The winds have almost completely stopped, making it more eerie", 2)
    S_T("than before.", 2)
    S_T("You step in a puddle and you foot becomes soaked.", 2)
    S_T("But is it rain water?", 2)
    S_T("You bend down and a faint dark red begins to show. \n", 2)
    S_T("No! ", 2)
    S_T("It can't be.", 2)
    S_T("You feel a drop on your head and you look up. \n", 2)
    S_T("You muffle your own screams as you realise its not rain but", 2)
    S_T("infact blood. \n", 2)
    S_T("THE BEAST! \n", 2)
    S_T("You take off into the woods, no longer following a path.", 2)
    S_T("Your heart pants like crazy, your eyesight blurred,", 2)
    S_T("as fear escapes your eyes", 2)
    S_T("It's safe for the time being.", 2)
    S_T("However in the distant you hear chanting...", 2)
    S_T("you can't make out what they are saying over the banging", 2)
    S_T("of the drums.", 2)
    S_T("To your right you smoke rising into the sky, behind the trees.", 2)
    S_T("Fire!!", 2)
    S_T("You are torn for choice.", 2)
    
    print("Where do you go? (1 Chanting/ 2 Fire)")
    ANSWER = input("").lower().strip()

    while ANSWER not in chanting and ANSWER not in fire:
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in chanting:
        the_chant()
    elif ANSWER in fire:
        the_fire()



def the_fire():
    """
    This function is called when the player 
    picks option two in the PickDirectionTwo
    if/else statement. 
    """
    S_T("You make your way to the smoke.", 2)
    S_T("Ash starts to consume the atmosphere.", 2)
    S_T("the flickering of the fire is the only", 2)
    S_T("comforting sound you've heard in a while.", 2)
    S_T("It's a nice sound.", 2)
    S_T("As you approach the area you see a log being used as a bench.", 2)
    S_T("A lone figure is occupying one of the benches.", 2)
    S_T("Hesitantly, you make your way and notice something. \n", 2)

    potion()


def potion():
    S_T("It's the man! the man from the beginning.", 2)
    S_T("As if by magic, the man turns around. There is no way", 2)
    S_T("he heard you coming. \n", 2)
    S_T(f"'Well {name} glad to know you made it this far.", 2)
    S_T("Although we never doubted you at all. ", 2)
    S_T("Have you met the predator yet?'", 2)
    S_T("You shake your head.", 2)
    S_T("'Oh wow! that's lucky.", 2)
    S_T("Most people don't make it this far.'", 2)
    S_T("You have been through the wars though.", 2)
    S_T("I'm going to offer two potions. You may only pick one though.", 2)
    S_T("One will increase your health back up, the other will decrease", 2)
    S_T("your insanity level. So which will it be? \n", 2)
    HealthStats(0)
    InsanityStats(0)
    print("Which potion do you want? (1 Health/ 2 Insanity)")
    ANSWER = input("").lower().strip()
    while ANSWER not in potion_health and ANSWER not in potion_insanity:
        S_T("Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in potion_health:
        S_T("Good choice. Take this and drink it and your health will", 2)
        S_T("increase by 3 points. \n", 2)
        S_T("You take the potion and drink the whole thing in one go,", 2)
        S_T("forgetting about your dehydration.", 2)
        S_T("You feel the potion work it's way through your body,", 2)
        S_T("giving you more strength than before.", 2)
        HealthStats(3)
        S_T("", 2)
        S_T("Something doesn't feel right now though.", 2)
        S_T("You start hearing noises, but there's nothing around. \n", 2)
        S_T("The faint chuckles cause you to turn around to see the man", 2)
        S_T("trying to stifle his laughter. This can't be good. \n", 2)
        S_T("'Oh Man! you gobbled that right up. Without hesitation.", 2)
        S_T("Did you really think I was going to let you just make", 2)
        S_T(f"yourself stronger. Dear {name} you still have a lot to", 2)
        S_T("learn. Everything comes with a price.' \n", 2)
        S_T("A pounding in your head clouds your thoughts.", 2)
        S_T("You quickly piece together what has happened. \n", 2)
        S_T("'For the price of more health your insanity has been", 2)
        S_T("increased. HAHAHA!!!' \n", 2)
        InsanityStats(1)
        S_T("", 2)
        S_T("And just like that, the man had disappeared... again.", 2)
    elif ANSWER in potion_insanity:
        S_T("Good Choice! Take this and your insanity level will", 2)
        S_T("decrease by 2", 2)
        S_T("You don't hesitate and gulp the potion down with ease.", 2)
        S_T("The effects of the potion happen almost instantly,", 2)
        S_T("your thoughts became clearer. \n", 2)
        InsanityStats(-2)
        S_T("However, almost immediately afterwards you feel a sharp", 2)
        S_T("pain in your stomach, you crouch over to stop the pain.", 2)
        S_T("The faint chuckles cause you to turn around to see the man", 2)
        S_T("trying to stifle his laughter. This can't be good. \n", 2)
        S_T("'Oh Man! you gobbled that right up. Without hesitation.", 2)
        S_T("Did you really think I was going to let you just make", 2)
        S_T(f"yourself stronger. Dear {name} you still have a lot to", 2)
        S_T("learn. Everything comes with a price.' \n", 2)
        S_T("The stabbing pain only grows worse.", 2)
        S_T("You quickly piece together what has happened. \n", 2)
        S_T("'For the price of less insanity your health has been", 2)
        S_T("decreased. HAHAHA!!!' \n", 2)
        HealthStats(-3)
        S_T("", 2)
        S_T("And just like that, the man had disappeared... again.", 2)
    
    hypnotised()

    
        

def the_chant():
    """
    This function is called when the player
     picks option 1 in theWalk1_A().
    """
    S_T("You slowly make your way to the chanting", 2)
    S_T("trying not to alert your position to them.", 2)
    S_T("The noise gets louder and louder as you near them.", 2)
    S_T("Eventually the sounds seem to surround you.", 2)
    S_T("You step on a twig and it crunches.", 2)
    S_T("The chanting abruptly stops.", 2)
    S_T("One by one, eyes start staring at you as you spin around. \n", 2)
    S_T("You're trapped.", 2)
    S_T("There's no escape. ", 2)
    S_T("The eyes seem to be floating closer to you.", 2)
    S_T("And with that your latern goes out, leaving the moon as", 2)
    S_T("your only source of light.", 2)
    S_T("The glow of the moon higlights the chanters, however", 2)
    S_T("they are still silent. \n", 2)
    S_T("Your insanity level increases by 2.", 2)
    InsanityStats(2)
    CheckStats()
    S_T("", 2)
    S_T("You see a bony finger come towards you and within seconds", 2)
    S_T("You feel many hands grasp you and lift you off the ground", 2)
    S_T("There's no luck in escaping as you try to wriggle out.\n", 2)
    S_T("After what feels like hours of being held hostage but was a", 2)
    S_T("measley few minutes, they drop you down on the floor. ", 2)
    S_T("The smell of smoke fills your nostrils as you look around", 2)
    S_T("and notice the smoke from the fire was closer than before.", 2)
    S_T("They form another circle around you and watch as you", 2)
    S_T("stumble to your feet.", 2)
    S_T("You hold onto your weapon as you decide your next move.", 2)

    print("Do you attack? (yes/no)")
    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        S_T(f"Invalid input Please try again {name}.", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        S_T("You take out your weapon and point it to one of the members.", 2)
        S_T("They try to snatch it out your hands but you are too quick.", 2)
        S_T("You end up snipping their hands as you pull back.", 2)
        S_T("However, the rest aren't scared by that encounter,", 2)
        S_T("in fact they seem to get closer than before.", 2)
        S_T("They all start chanting again and you immediately", 2)
        S_T("drop your weapon, becoming completely hypontised.", 2)
        S_T("You start levitating, only this time no one is grabbing you.", 2)
        S_T("Then all of a sudden you fell to the ground, hard.", 2)
        S_T("You lay there unable to move as you are winded. \n", 2)
        S_T("Your health drops 3 points.", 2)
        HealthStats(-3)
        CheckStats()
        S_T("", 2)
        S_T("When you look around again, you see that they have all", 2)
        S_T("disappeared, just like the man back at the building.", 2)
        S_T("'I wonder if he is connected to them.' You say out loud.", 2)
        S_T("You make your way over to the fire, and sit down.", 2)
        S_T("It feels good to be able to sit down.", 2)
    elif ANSWER in no:
        S_T("You go to take out your weapon but think better off it.", 2)
        S_T("There's way to many to take on alone.", 2)
        S_T("They all slowly turn to face one direction and then", 2)
        S_T("in unity, they all start gliding away, floating", 2)
        S_T("out of the cloaks and leaving them on the floor.", 2)
        S_T("Just like the man in the building.", 2)
        S_T("The fires tempts you as you realise you are freezing.", 2)

    S_T("After a while you hear a rustle in the bushes and you", 2)
    S_T("immediately tense up. However, there was almost a difference", 2)
    S_T("You saw some eyes glow and a something walked out.", 2)

    potion()


def WalkScenarioTwo():
    """
    This function will only be called if the player
     turns right from the PickDirection question.
    """
    print("What do you do? (1 Stand/ 2 Run)")
    ANSWER = input("").lower().strip()

    while ANSWER not in stand and ANSWER not in run: 
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in stand:
        S_T("The ground starts rumbling as you stand frozen.", 2)
        S_T("Then out of nowhere, a herd of deers come stampeding", 2)
        S_T("towards you. You crouch down to avoid a blow.", 2)
        S_T("However that wasn't wise. The deers trampled you as", 2)
        S_T("you laid hopeless. You lose 3 health.", 2)
        HealthStats(-3)
        CheckStats()
    elif ANSWER in run:
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

    TheWalkPartB()
    the_walk1_b()


def the_walk1_b():
    """
    This function is called after the player 
    has gone through TheWalkScenarioTwo(). 
    """

    S_T("You are thirsty but there's no water around.", 2)
    S_T("There was a water source about a mile back that", 2)
    S_T("you remember seeing but decide against it as.", 2)
    S_T("Those deers were running from something and", 2)
    S_T("you weren't about to find out either.", 2)
    S_T("Forward was the only option. \n", 2)
    S_T("The trek began to take a toll on you.", 2)
    S_T("You needed to sit down as soon as.", 2)
    S_T("But just as you were about to the stop,", 2)
    S_T("the sound of trickling water blessed your", 2)
    S_T("ears. You sprint as fast as your tired", 2)
    S_T("legs will take you. \n", 2)
    S_T("A river!! \n", 2)
    S_T("It has been the best thing to happen since", 2)
    S_T("you woke up in this nightmare", 2)
    S_T("You bend down and cup your hands,", 2)
    S_T("trying to gather as much as possible.", 2)
    S_T("The night grew more cold, causing shivers", 2)
    S_T("to run through your spine like electical", 2)
    S_T("currents. Warmth will be the next task.", 2)
    S_T("The path is no longer in eyesight as you", 2)
    S_T("strayed away from it to get hydrated.", 2)
    S_T("Every direction looks the same.", 2)

    compass()    

def compass():
    print("Which direction shall you go? (North/South/East/West)")
    ANSWER = input("").lower().strip()

    while ANSWER not in north and ANSWER not in south and ANSWER not in east and ANSWER not in west: 
        S_T(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in north:
        S_T("You start walking North but after a while", 2)
        S_T("you are stopped by an invisible barrier.", 2)
        S_T("There is no other choice but to go back. \n", 2)
        compass()
    elif ANSWER in south:
        S_T("South seems like a wise choice.", 2)
        S_T("There's a lot of coverage with trees", 2)
        S_T("but not too much that you can't see", 2)
        S_T("potential dangers.", 2)
        S_T("After a while you realise the", 2)
        S_T("area seems familar. \n", 2)
        S_T("You are back at the river, the", 2)
        S_T("exact same spot. Your footprints", 2)
        S_T("remain indented in the floor.", 2)
        S_T("You'll need to pick another", 2)
        S_T("direction. \n", 2)
        compass()
    elif ANSWER in east:
        S_T("East was in the same direction as", 2)
        S_T("the flow of river. \n", 2)
        S_T("'It has to lead somewhere.", 2)
        S_T("All rivers lead to something.'", 2)
        S_T("You say out loud. up until today", 2)
        S_T("you never spoke to yourself but ", 2)
        S_T("today has changed all that.", 2)
        S_T("Your grandma told you one day", 2)
        S_T("'you'll start and won't ever want", 2)
        S_T("to stop. Mine started one day in", 2)
        S_T("the forest while trekking through", 2)
        S_T("some serious thunderstorms.' \n", 2)
        S_T("You stop dead in your tracks.", 2)
        S_T("The story of your grandma seemed", 2)
        S_T("a little too like your situation", 2)
        S_T("right now.", 2)
        S_T("Did Grandma go through this as well?", 2)
        S_T("Is that why everything looks so", 2)
        S_T("familar? \n", 2)
        S_T("Just as you finish that thought", 2)
        S_T("the ground beging shaking violently", 2)
        S_T("as a roar ruptures through the sky. \n", 2)
        S_T("The predator is near. \n", 2)
        the_predators_son()
    elif ANSWER in west:
        S_T("You go west in hopes of setting up a camp site", 2)
        S_T("although with your luck there won't be", 2)
        S_T("anything to set up camp with.", 2)
        S_T("After about 5 minutes of walking you decide to", 2)
        S_T("set up here. you begin to look around to find", 2)
        S_T("any wood that is dry enough to light, although", 2)
        S_T("everything has been soaked from the rain.", 2)
        S_T("You try lighting some logs with your latern but", 2)
        S_T("you burn youself doing so. You start smelling", 2)
        S_T("smoke in the air but you assume its from the", 2)
        S_T("attempts of your own fire. However, you look", 2)
        S_T("around and see smoke rising and and disappearing", 2)
        S_T("into thin air. \n", 2)
        S_T("Finally!! \n", 2)
        S_T("You sprint in the direction of the smoke.", 2)
        S_T("You can almost fee lthe warmth filling your", 2)
        S_T("body before you even reach it.", 2)

        the_fire()
        potion()


def hypnotised():
    S_T("This noise begins to take over your entire body,", 2)
    S_T("causing you to loose all control.", 2)
    S_T("Your feet start moving against your will and your", 2)
    S_T("hands begin swaying in a military formation.", 2)
    S_T("You seem to be walking so fast as you rush through", 2)
    S_T("the forest.", 2)
    S_T("In the far distance you begin to see some castle", 2)
    S_T("walls stretch across the land. \n", 2)
    S_T("The CITADEL!! \n", 2)
    S_T("You have finally made it.", 2)
    S_T("The darkness slowly started to lift as the sun rose", 2)
    S_T("beyond the clouds.", 2)
    S_T("As you near the castle walls you make a sudden stop.", 2)
    S_T("Each second that goes by you get more control back", 2)
    S_T("of your body, but you are still under this hypnosis.", 2)
    S_T("Still frozen in place you watch as the castle gates", 2)
    S_T("lower down to reveal The predator.", 2)

def the_predators_son():
    """
    This function is called if the player 
    picks 'East'when asked which direction
    they want to go from function compass.
    """
    S_T("You make your way towards the roar", 2)
    S_T("The strength of knowing your Grandma ", 2)
    S_T("has potentially gone through this has", 2)
    S_T("made you willing to fight back.", 2)
    S_T("With every step you took, the roars got", 2)
    S_T("louder and the ground shaked more.", 2)
    S_T("It was almost time. \n", 2)
    S_T("Whipping noises rung through your ears", 2)
    S_T("as the predator surrounds you.", 2)
    S_T("He is constantly speeding up, which", 2)
    S_T("is kicking up a lot of dirt and making it", 2)
    S_T("harder to see. \n", 2)
    S_T("Then he stops...", 2)
    S_T("And pounces... \n", 2)
    print("What do you do? (cower/run)")

    ANSWER = input("=>").lower().strip()

    while ANSWER not in run and ANSWER not in cower:
        S_T(f"Invalid input name. Please try again {name}", 2)
        ANSWER = input("").lower().strip()  

    if ANSWER in run:
        S_T("You tried to outrun the pounce but", 2)
        S_T("not with much luck. the predator clipped", 2)
        S_T("your clothes as he landed, dragging you", 2)
        S_T("to the floor. He then continues to drag", 2)
        S_T("you around on the ground. You can't", 2)
        S_T("escape.", 2)
        S_T("after what feels like minutes of torture.", 2)
        S_T("the predator stops playing with you", 2)
        S_T("like a toy.", 2)
        S_T("You lose 3 health.", 2)
        HealthStats(-3)
        CheckStats()
        S_T("however the fight isn't over yet.", 2)
        S_T("The predator takes a swipe with his", 2)
        S_T("beast like claws. You are able to dodge.", 2)
        S_T("This only angers him. He uses his tail", 2)
        S_T("and grips you around the waist.", 2)
        S_T("he lifts you in the air and raises you", 2)
        S_T("just above his head, almost as if playing", 2)
        S_T("with his food.", 2)
        print("What do you do? (1 Wriggle/ 2 Attack)")
        ANSWER = input("").lower().strip()

        while ANSWER not in wriggle and ANSWER not in attack:
            S_T(f"Invalid input name. Please try again {name}", 2)
            ANSWER = input("").lower().strip()
        if ANSWER in wriggle:
            S_T("You try to wriggle yourself free but the grip", 2)
            S_T("only gets tighter. You can feel the life being", 2)
            S_T("squeezed out of you and in that moment you", 2)
            S_T("believe this is the end.", 2)
            S_T("You lose 1 health.", 2)
            HealthStats(-1)
            CheckStats()
            S_T("As you are lowered into the beasts mouth,", 2)
            S_T("you decide on a risky tactic. With all the force", 2)
            S_T("you can manage you boot the beast square in the face.", 2)
            S_T("The beast wimpers and immediately drops you", 2)
            S_T("to the ground.", 2)
            S_T("The predator bolts off, leaving you on the floor.", 2)
        elif ANSWER in attack:
            S_T("With the hand that is free, you reach behind you", 2)
            S_T(f"and grab out your item. The predator hisses", 2)
            S_T("as you raisse the weapon and send it striking", 2)
            S_T("on his tail.", 2)
            S_T("A massive clink can be heard as it connects to", 2)
            S_T("the tail. The tail is made out of some metal.", 2)
            S_T("The predator still hisses out in pain and drops you.", 2)
            S_T("The predator bolts off, leaving you on the floor.", 2)

    elif ANSWER in cower:
        S_T("You crouch to your knees with your hands in the air,", 2)
        S_T("clutching your weapon. A dark shadow glooms over you", 2)
        S_T("quickly as you see the predator jump. At this moment", 2)
        S_T("you strike your weapon up, just catching the predators", 2)
        S_T("stomach. The predator reacted badly, first standing on", 2)
        S_T("his back legs, screaming out in pain. He then whips", 2)
        S_T("his tail at you which sends you flying into a nearby", 2)
        S_T("tree. Winded, you want him scurry away with blurred", 2)
        S_T("vision.", 2)
        S_T("You lose 3 health.", 2)
        HealthStats(-3)
        CheckStats()   
    
    S_T("You stand up and dust yourself off. You notice an apple", 2)
    S_T("on the floor. Starving, you eat the entire thing almost", 2)
    S_T("instantly. Your health increase by 2 points. \n", 2)
    HealthStats(2)
    CheckStats()

    hypnotised()

    S_T("However this doesn't look like the one you faced", 2)
    S_T("earlier. It was thrice as big.", 2)
    S_T("It had the head of a dog, and the tail like a", 2)
    S_T("tiger. You thought the", 2)
    S_T("one earlier was impossible to survive from but this ", 2)
    S_T("one was actually going to be impossible.", 2)
    S_T("And just when you thought it couldn't get worse,", 2)
    S_T("The Beast opens his mouth and speaks... \n", 2)
    S_T("'So I guess you've met one of my sons.'", 2)
    S_T("His voice so deep that it shook the ground.", 2)
    S_T("he stood fimrly, his stance intimdating you.", 2)
    S_T("'I'll make you pay for what you did to him.", 2)
    S_T("His brothers aren't very happy either.' \n", 2)
    S_T("BROTHERS?! There's an entire family of them.", 2)
    S_T("There is no escape from this... at all.", 2)




the_predators_son()

#PlayGame()