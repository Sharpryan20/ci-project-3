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
        InsanityStats(+2)
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
    FightOne = input("What do you do? (1 Use weapon/2 Carry on walking) \n")
    if FightOne.lower().strip() == "1":
        S_T("You poke the bush and the rustling stops", 2)
        S_T("but a few seconds later a badger jumps at you", 2)
        S_T("and scratches you.", 1)
        S_T("You lose 2 health and your insanity increases.", 2)
        HealthStats(-2)
        InsanityStats(2)
        CheckStats()
    elif FightOne == "2":
        S_T("The rustling stops after a few seconds.", 2)
        S_T("you quickly scurry past and continue your walk,", 2)
        S_T("careful not to disturb the beast.", 2)
    else:
        print("Invalid input. Please try again.")
    
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
    S_T("Infact blood. \n", 2)
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
    PickDirectionTwo = input("Where do you go? (1 Chanting/ 2 Fire) \n")
    if PickDirectionTwo.lower().strip() == "1":
        the_chant()
    elif PickDirectionTwo == "2":
        the_fire()
    else:
        print("Invalid input. Please try again.")


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
    potion_picker = input("Which potion do you want? (1 Health/ 2 Insanity) \n")
    if potion_picker.lower().strip() == "1":
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
    elif potion_picker == "2":
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
    else:
        print("Invalid input. Please try again.")
        

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

    attack_one = input("Do you attack? (yes/no) \n")
    if attack_one.lower().strip() == "yes":
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
    elif attack_one == "no":
        S_T("You go to take out your weapon but think better off it.", 2)
        S_T("There's way to many to take on alone.", 2)
        S_T("They all slowly turn to face one direction and then", 2)
        S_T("in unity, they all start gliding away, floating", 2)
        S_T("out of the cloaks and leaving them on the floor.", 2)
        S_T("Just like the man in the building.", 2)
        S_T("The fires tempts you as you realise you are freezing.", 2)
    else:
        print("Invalid input. Please try again.")

    S_T("After a while you hear a rustle in the bushes and you", 2)
    S_T("immediately tense up. However, there was almost a difference", 2)
    S_T("You saw some eyes glow and a something walked out.", 2)

    potion()


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
    pick_direction_three = input("Which direction shall you go?")


def compass():
    pick_direction_three = input("Which direction shall you go? (North/South/East/west) \n")
    if pick_direction_three.lower().strip() == "north":
        S_T("You start walking North but after a while", 2)
        S_T("you are stopped by an invisible barrier.", 2)
        S_T("There is no other choice but to go back. \n", 2)
        compass()
    elif pick_direction_three == "South":
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
    else:
        print("invalid input. Please try again.")
   

#the_chant()

# TheWalk()


# PlayGame()

# the_fire()

compass()

