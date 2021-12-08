import time

user_stats = {
    
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
dodge = ("1", "dodge")
legs = ("1", "legs")
back = ("2", "back")


def s_t(text: str, delay: int):
    """
    Prints out a line of text for the story and delays
    the next line for a certain amount of time.
    """

    print(text)
    time.sleep(delay)


def health_stats(health_number: int):
    """
    Increases or decreases the users health by a specified amount
    then displys the users with the new health score.
    """

    user_stats["health"] = user_stats["health"] + (health_number)
    s_t("Your health is: " + str(user_stats['health']), 2)


def insanity_stats(insanity_number: int):
    """
    Increases or decreases the users insanity by a specific amount 
    then displays the users with the new insanity score.
    """
    user_stats["insanity"] = user_stats["insanity"] + (insanity_number)
    s_t("Your insanity level is: " + str(user_stats['insanity']), 2)


def no_health():
    """
    This function is called within the check_stats function.
    If the user has of 0 or below, the player will die and the game 
    will be over.
    """
    s_t("You have been severly injured.", 2)
    s_t("You are too tired to continue.", 2)
    s_t("You can rest now.", 2)
    s_t("The Hunt is Over", 2)


def max_insanity():
    """
    This function will be called within the check_stats function.
    If the users inasity level reaches above 5, the player will halluncinate
    and the game will be over.
    """

    s_t("You start to see things, things that aren't really there.", 2)
    s_t("There is no going back now.", 2)
    s_t("You lose all control over your body and you run off...", 2)
    s_t("Never to be seen again", 2)


def check_stats():
    """
    Will be called any time the users stats are affected.
    If health drops below 0 or insanity is higher than 5, then
    the correct function will be called and it will be 
    game over.
    """

    if user_stats["health"] <= 0:
        no_health()
    if user_stats["insanity"] >= 5:
        max_insanity()


def play_game():
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
        s_t("Invalid input Please try again.", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        s_t("Brillant!! Lets start", 2)

        global name 
        name = input("What is your name? \n")
        s_t(f"Hello {name}... GOODLUCK!!!", 2)
        s_t("HAHAHAHA \n", 2)
        opening()
    elif ANSWER in no:
        print("That's a shame. See you around!")


def opening():
    s_t("You wake up... dazed!", 2)
    s_t("The gloomy forest sets in as you realise you are lost.", 2)
    s_t("The place has a sense of familarity but", 2)
    s_t("you aren't quite sure how.", 2)
    s_t("You stumble to your feet and frantically search", 2)
    s_t("for shelter as the moon slowly rises.", 2)
    s_t("In the distance you see the roof of a small building", 2)
    s_t("peering out behind the trees", 2)
    s_t("The fog has already began to set and you make your", 2)
    s_t("to the dainty, creepy shed", 2)
    s_t("When you approach the door you see a faint orange glow ", 2)
    s_t("appear in the doorway, which is slightly ajar \n", 2)

    print("Do you open the door? (yes/no?)")

    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        s_t(f"Invalid input Please try again {name}", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        s_t("The door slowly creeps open revealing an open room,", 2)
        s_t("and in the middle of it stands a tall dark figure,", 2)
        s_t("a cloak covering the entity from head to toe.", 2)
    elif ANSWER in no:
        s_t("You walk around and peer through a window", 2)
        s_t("for a better look when suddenly a dark figure", 2)
        s_t("jumps at the window. Startled, you take a step back.", 2)
        s_t("The man gesutres you to come inside.", 2)
        s_t("You make your way back around to the door and enter.", 2)
        s_t("Your insanity level has increased \n", 2)
        insanity_stats(+2)
        check_stats()

    s_t("The man lifts his hood and points to a chair.", 2)
    s_t("You catch on and sit down in the worn chair", 2)
    s_t("He throws more wood on the fire and just stands there", 2)
    s_t("watching it roar as the flames warm up the room.", 2)
    s_t("You begin to feel uneasy as he scurries closer to you.", 2)
    s_t(f"So {name}, I see you are finally awake!", 2)
    s_t("Do you want to know why you are here? \n", 2)

    print("Do you answer back? (yes/no)")
    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        s_t(f"Invalid input Please try again {name}.", 2)
        ANSWER = input("").lower().strip()
    if ANSWER in yes:
        s_t("You nod and say;'Wait how do you know my name?'", 2)
        s_t("'Where am I?'", 2)
    
    elif ANSWER in no:
        s_t("You questioned how he knew your name", 2)
        s_t("but decided not to say anything.", 2)

    s_t("The man paces back and forth, almost to say something", 2)
    s_t("'It doesn't matter how I know your name!'", 2)
    s_t("He snapped as he twisted his head almost 180 degrees", 2)
    s_t("'All that matters is The Hunt can now begin.'", 2)
    s_t("he lifted his hands up just as a clap of thunder bellowed", 2)
    s_t("almost as if the man had summoned the phenomenon. \n", 2)
    s_t("'The Hunt?' You question, your hands shake with fear \n", 2)
    s_t("'The hunt is a matter of life and death. Unfortunately", 2)
    s_t("you have been assigned the role of prey.", 2)
    s_t("You have 8 hours to survive the forest and make it to", 2)
    s_t("THE CITADEL!!", 2)
    s_t("You will have a weapon of your choosing.", 2)
    s_t("The man makes his way over to a locked door.", 2)
    s_t("He opens it and reveals a variety of weapons.", 2)
    s_t("Axes...", 0)
    s_t("Knives...", 0)
    s_t("Swords...", 0)
    s_t("Pool cue...", 0)

    global item
    item = input("Which weapon do you pick? (Sword, Axe, Knife, Cue, Nothing) \n")
    s_t(f"I see you picked {item}. Good choice", 2)
    s_t(f"You pick up {item}. ", 2)
    s_t("You turn to ask who the predator is but the man is gone.", 2)
    s_t("Any indication that he was here is the cloak bundled up.", 2)
    s_t("You bend down and run the cloak through your fingers \n", 2)
    
    print("Do you pick it up? (yes/no)")
    ANSWER = input("").lower().strip() 
    while ANSWER not in yes and ANSWER not in no: 
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 
    if ANSWER in yes: 
        s_t("You place the cloak over your shoulders and leave.", 2)
    elif ANSWER in no:
        s_t("You stand back up and head to the door.", 2)

    s_t("As you leave you notice a drawer cracked open slightly. \n", 2)

    print("Do you open it? (yes/no)")
    ANSWER = input("").lower().strip() 
    while ANSWER not in yes and ANSWER not in no: 
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 
    if ANSWER in yes:
        s_t("you see a note inside and a photo. It's of you.", 2)
        s_t("You unfold the note and it reads; 'I'm sorry.", 2)
        s_t("They made me do it, Please forgive me!'\n", 2)
        s_t("You put the note in your pocket and walk out the door.", 2)    
    elif ANSWER in no: 
        s_t("You decide not to open it and leave the house. \n", 2)

    s_t("You notice a hanging latern the porch.", 2)
    s_t("You take it off the wall and start your journey. \n", 2)

    the_walk()


def the_walk():
    """
    This function is the second part of the Game where the
    player has just left the house.
    There will consist nested if/else statements as the player progresses."
    """
    s_t("It feels like hours have passed since you started.", 2)
    s_t("The path strecthed out for ages, you've had nothing", 2)
    s_t("to keep you company expect the whistling winds as", 2)
    s_t("they raced through the trees.", 2)
    s_t("The thunder had stopped but the rain was still hard.\n", 2)
    s_t("FINALLY!!! \n", 2)
    s_t("The path splits into two.", 2)

    print("Do you go straight or right? (straight/right)")
    ANSWER = input("").lower().strip()

    while ANSWER not in straight and ANSWER not in right:
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip() 

    if ANSWER in straight:    
        s_t("You continue and suddenly hear a rustle.", 2)
        s_t("You turn to see a bush", 2) 
        walk_scenario_one()
    elif ANSWER in right:
        s_t("You turn right and you start walking.", 2)
        s_t("You start hearing things, like screeches.", 2)
        s_t("The noises get louder and louder, becoming", 2)
        s_t("near impossible to even hear your thoughts.", 2)
        walk_scenario_two()
    

def the_walk_part_b():
    """
    The second part of the the_walk() function which both players
    will recieve no matter what path they go down.
    """
    s_t("It starts to get colder the further you walk into the forest.", 2)
    s_t("You begin to fear that there was no end to this nightmare.", 2)
    s_t("And in fact you were destined to die out here.", 2)
    s_t("You try to remember anything as to how you,", 2)
    s_t("ended up here. Why was it so familiar?", 2)
    s_t("Who was that man?", 2)
    s_t("How did he know your name?", 2)
    s_t("Is this some sick joke?", 2)
    s_t("Is this even legal? It can't be?", 2)


def walk_scenario_one():
    """
    This is the first scenario for the_walk() function
    Will only be called if player continues straight in
    the PickDirection if/else statement.
    """
    print("What do you do? (1 Use weapon/ 2 Walk)")
    ANSWER = input("").lower().strip()
    while ANSWER not in use_weapon and ANSWER not in carry_walking: 
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in use_weapon:
        s_t("You poke the bush and the rustling stops", 2)
        s_t("but a few seconds later a badger jumps at you", 2)
        s_t("and scratches you.", 1)
        s_t("You lose 2 health and your insanity increases.", 2)
        health_stats(-2)
        insanity_stats(2)
        check_stats()
    elif ANSWER in carry_walking:
        s_t("The rustling stops after a few seconds.", 2)
        s_t("you quickly scurry past and continue your walk,", 2)
        s_t("careful not to disturb the beast.", 2)
    
    the_walk_part_b()
    the_walk_1_a()


def the_walk_1_a():
    """
    This function is called
    the player takes the straight path and after 
    the_walk_part_b() is called.
    """
    s_t("The path begins to fade out as nature covers the concrete.", 2)
    s_t("No one has been down here in a while.", 2)
    s_t("Have you chosen the right path?", 2)
    s_t("Is the predator down here?", 2)
    s_t("You try to stay strong.", 2)
    s_t("You have come to far to give up now, surely there is only,", 2)
    s_t("a few hours left to the go.", 2)
    s_t("Your latern begins to flicker ever so slightly.", 2)
    s_t("The winds have almost completely stopped, making it more eerie", 2)
    s_t("than before.", 2)
    s_t("You step in a puddle and you foot becomes soaked.", 2)
    s_t("But is it rain water?", 2)
    s_t("You bend down and a faint dark red begins to show. \n", 2)
    s_t("No! ", 2)
    s_t("It can't be.", 2)
    s_t("You feel a drop on your head and you look up. \n", 2)
    s_t("You muffle your own screams as you realise its not rain but", 2)
    s_t("infact blood. \n", 2)
    s_t("THE BEAST! \n", 2)
    s_t("You take off into the woods, no longer following a path.", 2)
    s_t("Your heart pants like crazy, your eyesight blurred,", 2)
    s_t("as fear escapes your eyes", 2)
    s_t("It's safe for the time being.", 2)
    s_t("However in the distant you hear chanting...", 2)
    s_t("you can't make out what they are saying over the banging", 2)
    s_t("of the drums.", 2)
    s_t("To your right you smoke rising into the sky, behind the trees.", 2)
    s_t("Fire!!", 2)
    s_t("You are torn for choice.", 2)
    
    print("Where do you go? (1 Chanting/ 2 Fire)")
    ANSWER = input("").lower().strip()

    while ANSWER not in chanting and ANSWER not in fire:
        s_t(f"Invalid input Please try again {name}.", 2) 
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
    s_t("You make your way to the smoke.", 2)
    s_t("Ash starts to consume the atmosphere.", 2)
    s_t("the flickering of the fire is the only", 2)
    s_t("comforting sound you've heard in a while.", 2)
    s_t("It's a nice sound.", 2)
    s_t("As you approach the area you see a log being used as a bench.", 2)
    s_t("A lone figure is occupying one of the benches.", 2)
    s_t("Hesitantly, you make your way and notice something. \n", 2)

    potion()


def potion():
    s_t("It's the man! the man from the beginning.", 2)
    s_t("As if by magic, the man turns around. There is no way", 2)
    s_t("he heard you coming. \n", 2)
    s_t(f"'Well {name} glad to know you made it this far.", 2)
    s_t("Although we never doubted you at all. ", 2)
    s_t("Have you met the predator yet?'", 2)
    s_t("You shake your head.", 2)
    s_t("'Oh wow! that's lucky.", 2)
    s_t("Most people don't make it this far.'", 2)
    s_t("You have been through the wars though.", 2)
    s_t("I'm going to offer two potions. You may only pick one though.", 2)
    s_t("One will increase your health back up, the other will decrease", 2)
    s_t("your insanity level. So which will it be? \n", 2)
    health_stats(0)
    insanity_stats(0)
    print("Which potion do you want? (1 Health/ 2 Insanity)")
    ANSWER = input("").lower().strip()
    while ANSWER not in potion_health and ANSWER not in potion_insanity:
        s_t("Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in potion_health:
        s_t("Good choice. Take this and drink it and your health will", 2)
        s_t("increase by 3 points. \n", 2)
        s_t("You take the potion and drink the whole thing in one go,", 2)
        s_t("forgetting about your dehydration.", 2)
        s_t("You feel the potion work it's way through your body,", 2)
        s_t("giving you more strength than before.", 2)
        health_stats(3)
        s_t("", 2)
        s_t("Something doesn't feel right now though.", 2)
        s_t("You start hearing noises, but there's nothing around. \n", 2)
        s_t("The faint chuckles cause you to turn around to see the man", 2)
        s_t("trying to stifle his laughter. This can't be good. \n", 2)
        s_t("'Oh Man! you gobbled that right up. Without hesitation.", 2)
        s_t("Did you really think I was going to let you just make", 2)
        s_t(f"yourself stronger. Dear {name} you still have a lot to", 2)
        s_t("learn. Everything comes with a price.' \n", 2)
        s_t("A pounding in your head clouds your thoughts.", 2)
        s_t("You quickly piece together what has happened. \n", 2)
        s_t("'For the price of more health your insanity has been", 2)
        s_t("increased. HAHAHA!!!' \n", 2)
        insanity_stats(1)
        s_t("", 2)
        s_t("And just like that, the man had disappeared... again.", 2)
    elif ANSWER in potion_insanity:
        s_t("Good Choice! Take this and your insanity level will", 2)
        s_t("decrease by 2", 2)
        s_t("You don't hesitate and gulp the potion down with ease.", 2)
        s_t("The effects of the potion happen almost instantly,", 2)
        s_t("your thoughts became clearer. \n", 2)
        insanity_stats(-2)
        s_t("However, almost immediately afterwards you feel a sharp", 2)
        s_t("pain in your stomach, you crouch over to stop the pain.", 2)
        s_t("The faint chuckles cause you to turn around to see the man", 2)
        s_t("trying to stifle his laughter. This can't be good. \n", 2)
        s_t("'Oh Man! you gobbled that right up. Without hesitation.", 2)
        s_t("Did you really think I was going to let you just make", 2)
        s_t(f"yourself stronger. Dear {name} you still have a lot to", 2)
        s_t("learn. Everything comes with a price.' \n", 2)
        s_t("The stabbing pain only grows worse.", 2)
        s_t("You quickly piece together what has happened. \n", 2)
        s_t("'For the price of less insanity your health has been", 2)
        s_t("decreased. HAHAHA!!!' \n", 2)
        health_stats(-3)
        s_t("", 2)
        s_t("And just like that, the man had disappeared... again.", 2)
    
    hypnotised()
    finale_a()
          

def the_chant():
    """
    This function is called when the player
     picks option 1 in the_walk_1_a().
    """
    s_t("You slowly make your way to the chanting", 2)
    s_t("trying not to alert your position to them.", 2)
    s_t("The noise gets louder and louder as you near them.", 2)
    s_t("Eventually the sounds seem to surround you.", 2)
    s_t("You step on a twig and it crunches.", 2)
    s_t("The chanting abruptly stops.", 2)
    s_t("One by one, eyes start staring at you as you spin around. \n", 2)
    s_t("You're trapped.", 2)
    s_t("There's no escape. ", 2)
    s_t("The eyes seem to be floating closer to you.", 2)
    s_t("And with that your latern goes out, leaving the moon as", 2)
    s_t("your only source of light.", 2)
    s_t("The glow of the moon higlights the chanters, however", 2)
    s_t("they are still silent. \n", 2)
    s_t("Your insanity level increases by 2.", 2)
    insanity_stats(2)
    check_stats()
    s_t("", 2)
    s_t("You see a bony finger come towards you and within seconds", 2)
    s_t("You feel many hands grasp you and lift you off the ground", 2)
    s_t("There's no luck in escaping as you try to wriggle out.\n", 2)
    s_t("After what feels like hours of being held hostage but was a", 2)
    s_t("measley few minutes, they drop you down on the floor. ", 2)
    s_t("The smell of smoke fills your nostrils as you look around", 2)
    s_t("and notice the smoke from the fire was closer than before.", 2)
    s_t("They form another circle around you and watch as you", 2)
    s_t("stumble to your feet.", 2)
    s_t("You hold onto your weapon as you decide your next move.", 2)

    print("Do you attack? (yes/no)")
    ANSWER = input("").lower().strip()

    while ANSWER not in yes and ANSWER not in no:
        s_t(f"Invalid input Please try again {name}.", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in yes:
        s_t("You take out your weapon and point it to one of the members.", 2)
        s_t("They try to snatch it out your hands but you are too quick.", 2)
        s_t("You end up snipping their hands as you pull back.", 2)
        s_t("However, the rest aren't scared by that encounter,", 2)
        s_t("in fact they seem to get closer than before.", 2)
        s_t("They all start chanting again and you immediately", 2)
        s_t("drop your weapon, becoming completely hypontised.", 2)
        s_t("You start levitating, only this time no one is grabbing you.", 2)
        s_t("Then all of a sudden you fell to the ground, hard.", 2)
        s_t("You lay there unable to move as you are winded. \n", 2)
        s_t("Your health drops 3 points.", 2)
        health_stats(-3)
        check_stats()
        s_t("", 2)
        s_t("When you look around again, you see that they have all", 2)
        s_t("disappeared, just like the man back at the building.", 2)
        s_t("'I wonder if he is connected to them.' You say out loud.", 2)
        s_t("You make your way over to the fire, and sit down.", 2)
        s_t("It feels good to be able to sit down.", 2)
    elif ANSWER in no:
        s_t("You go to take out your weapon but think better off it.", 2)
        s_t("There's way to many to take on alone.", 2)
        s_t("They all slowly turn to face one direction and then", 2)
        s_t("in unity, they all start gliding away, floating", 2)
        s_t("out of the cloaks and leaving them on the floor.", 2)
        s_t("Just like the man in the building.", 2)
        s_t("The fires tempts you as you realise you are freezing.", 2)

    s_t("After a while you hear a rustle in the bushes and you", 2)
    s_t("immediately tense up. However, there was almost a difference", 2)
    s_t("You saw some eyes glow and a something walked out.", 2)

    potion()


def walk_scenario_two():
    """
    This function will only be called if the player
     turns right from the PickDirection question.
    """
    print("What do you do? (1 Stand/ 2 Run)")
    ANSWER = input("").lower().strip()

    while ANSWER not in stand and ANSWER not in run: 
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in stand:
        s_t("The ground starts rumbling as you stand frozen.", 2)
        s_t("Then out of nowhere, a herd of deers come stampeding", 2)
        s_t("towards you. You crouch down to avoid a blow.", 2)
        s_t("However that wasn't wise. The deers trampled you as", 2)
        s_t("you laid hopeless. You lose 3 health.", 2)
        health_stats(-3)
        check_stats()
    elif ANSWER in run:
        s_t("You bolt in the opposite direction of the sounds,", 2)
        s_t("trying your best to out run the predators.", 2)
        s_t("However it wasn't a predator but a herd of deer.", 2)
        s_t("They were sprinting at full spped and almost", 2)
        s_t("immediately ran past you. One wasn't quite as fast", 2)
        s_t("and was beginning to trail behind. You wait for it", 2)
        s_t("to get closer to you and as it apporaches you grab his", 2)
        s_t("antlers and hop on the back.", 2)
        s_t("Now startled, the deer speeds up and within time", 2)
        s_t("has caught back up to the herd.", 2)
        s_t("'What was they running from?'", 2)
        s_t("You hop off the deer and head back, realising you", 2)
        s_t("had dropped your weapon.", 2)

    the_walk_part_b()
    the_walk_1_b()


def the_walk_1_b():
    """
    This function is called after the player 
    has gone through the_walk_scenario_two(). 
    """

    s_t("You are thirsty but there's no water around.", 2)
    s_t("There was a water source about a mile back that", 2)
    s_t("you remember seeing but decide against it as.", 2)
    s_t("Those deers were running from something and", 2)
    s_t("you weren't about to find out either.", 2)
    s_t("Forward was the only option. \n", 2)
    s_t("The trek began to take a toll on you.", 2)
    s_t("You needed to sit down as soon as.", 2)
    s_t("But just as you were about to the stop,", 2)
    s_t("the sound of trickling water blessed your", 2)
    s_t("ears. You sprint as fast as your tired", 2)
    s_t("legs will take you. \n", 2)
    s_t("A river!! \n", 2)
    s_t("It has been the best thing to happen since", 2)
    s_t("you woke up in this nightmare", 2)
    s_t("You bend down and cup your hands,", 2)
    s_t("trying to gather as much as possible.", 2)
    s_t("The night grew more cold, causing shivers", 2)
    s_t("to run through your spine like electical", 2)
    s_t("currents. Warmth will be the next task.", 2)
    s_t("The path is no longer in eyesight as you", 2)
    s_t("strayed away from it to get hydrated.", 2)
    s_t("Every direction looks the same.", 2)

    compass()    


def compass():
    print("Which direction shall you go? (North/South/East/West)")
    ANSWER = input("").lower().strip()

    while ANSWER not in north and ANSWER not in south and ANSWER not in east and ANSWER not in west: 
        s_t(f"Invalid input Please try again {name}.", 2) 
        ANSWER = input("").lower().strip()
    if ANSWER in north:
        s_t("You start walking North but after a while", 2)
        s_t("you are stopped by an invisible barrier.", 2)
        s_t("There is no other choice but to go back. \n", 2)
        compass()
    elif ANSWER in south:
        s_t("South seems like a wise choice.", 2)
        s_t("There's a lot of coverage with trees", 2)
        s_t("but not too much that you can't see", 2)
        s_t("potential dangers.", 2)
        s_t("After a while you realise the", 2)
        s_t("area seems familar. \n", 2)
        s_t("You are back at the river, the", 2)
        s_t("exact same spot. Your footprints", 2)
        s_t("remain indented in the floor.", 2)
        s_t("You'll need to pick another", 2)
        s_t("direction. \n", 2)
        compass()
    elif ANSWER in east:
        s_t("East was in the same direction as", 2)
        s_t("the flow of river. \n", 2)
        s_t("'It has to lead somewhere.", 2)
        s_t("All rivers lead to something.'", 2)
        s_t("You say out loud. up until today", 2)
        s_t("you never spoke to yourself but ", 2)
        s_t("today has changed all that.", 2)
        s_t("Your grandma told you one day", 2)
        s_t("'you'll start and won't ever want", 2)
        s_t("to stop. Mine started one day in", 2)
        s_t("the forest while trekking through", 2)
        s_t("some serious thunderstorms.' \n", 2)
        s_t("You stop dead in your tracks.", 2)
        s_t("The story of your grandma seemed", 2)
        s_t("a little too like your situation", 2)
        s_t("right now.", 2)
        s_t("Did Grandma go through this as well?", 2)
        s_t("Is that why everything looks so", 2)
        s_t("familar? \n", 2)
        s_t("Just as you finish that thought", 2)
        s_t("the ground beging shaking violently", 2)
        s_t("as a roar ruptures through the sky. \n", 2)
        s_t("The predator is near. \n", 2)
        the_predators_son()
    elif ANSWER in west:
        s_t("You go west in hopes of setting up a camp site", 2)
        s_t("although with your luck there won't be", 2)
        s_t("anything to set up camp with.", 2)
        s_t("After about 5 minutes of walking you decide to", 2)
        s_t("set up here. you begin to look around to find", 2)
        s_t("any wood that is dry enough to light, although", 2)
        s_t("everything has been soaked from the rain.", 2)
        s_t("You try lighting some logs with your latern but", 2)
        s_t("you burn youself doing so. You start smelling", 2)
        s_t("smoke in the air but you assume its from the", 2)
        s_t("attempts of your own fire. However, you look", 2)
        s_t("around and see smoke rising and and disappearing", 2)
        s_t("into thin air. \n", 2)
        s_t("Finally!! \n", 2)
        s_t("You sprint in the direction of the smoke.", 2)
        s_t("You can almost fee lthe warmth filling your", 2)
        s_t("body before you even reach it.", 2)

        the_fire()
        potion()


def finale_a():
    s_t("As the predator got closer you could feel the", 2)
    s_t("fear radiating from your body, and he could sense ", 2)
    s_t("it. \n", 2)
    s_t("'I cannot let you in this castle. You are a hard one", 2)
    s_t("to track down. I've been waiting for this moment for", 2)
    s_t("20 years. She was right you know! Your grandmother.", 2)
    s_t("She has been the only person able to beat me, but she", 2)
    s_t("told that you would be able to as well.' \n", 2)
    s_t("'What do you know about my Grandma??!!!' You scream", 2)
    s_t("The Beasts laughter drowing out your screams. He knew", 2)
    s_t("you were scared.", 2)
    s_t("You take a defensive stance, your hand holding", 2)
    s_t("the handle of your weapon.", 2)
    s_t("Dawn rose through the clouds and you began to take", 2)
    s_t("in your surroundings. It's not real....", 2)
    s_t("None of it is. Is it a simulation? \n", 2)
    s_t("'You've only got 10 minutes to defeat me.' He said", 2)
    s_t("stil smirking. \n", 2)
    s_t("'That long huh' you reciprocate his smirk, growing", 2)
    s_t("more confident by the second...", 2)


def finale_b():
    s_t("The Beast jumps at you.", 2)
    print("What do you do? (1 dodge/ 2 attack)")
    ANSWER = input("").lower()

    while ANSWER not in attack and ANSWER not in dodge:
        s_t(f"Invalid input. Please try again {name}", 2)
        ANSWER = input("").lower().strip()
    if ANSWER in dodge:
        s_t("You successfully dodge the attack.", 2)
        s_t("This only enrages him more. \n", 2)
    elif ANSWER in attack:
        s_t("You strike your weapon at the beast.", 2)
        s_t("However he is too quick and dodges you, but", 2)
        s_t("scratches your legs in the process. \n", 2)
    
    s_t("The beast turns to look at you again, this time", 2)
    s_t("with anger pouring at his eyes.", 2)
    s_t("He roars, which echos and bounces off these", 2)
    s_t("invisible barriers. It startles you and then", 2)
    s_t("he strikes you again, charging at full speed.", 2)

    print("What do you do? (1 dodge/ 2 attack)")
    ANSWER = input("").lower().strip()

    while ANSWER not in attack and ANSWER not in dodge:
        s_t(f"Invalid input. Please try again {name}.", 2)
        ANSWER = input("").lower().strip()

    if ANSWER in dodge:
        s_t("You try to dodge but the beast anticipated", 2)
        s_t("your move this time. He attacks your arm", 2)
        s_t("You lose one health. \n", 2)
        health_stats(-1)
        check_stats()
        s_t("", 2)
    elif ANSWER in attack:
        s_t("You stand with your back against him.", 2)
        s_t("As you hear him get closer you swing at", 2)
        s_t("full power and hit him straight in the", 2)
        s_t("face. This sends him back a few feet,", 2)
        s_t("causing him to lose balance. \n", 2)

    s_t("'You are going to have to try a lot harder than", 2)
    s_t(f"that {name}. I know your Grandmother did.'", 2)
    s_t("Hearing him talk about your Grandma like that ", 2)
    s_t("makes you so angry. Thinking how she had to go", 2)
    s_t("through this as well. \n", 2)
    s_t("This time you strike first.", 2)

    print("Where do you attack? (1 legs/ 2 back)")
    ANSWER = input("").lower().strip()

    while ANSWER not in legs and ANSWER not in back:
        s_t(f"Invalid input. Please try again {name}", 2)
        ANSWER = input("").lower().strip()

    if ANSWER in legs:
        s_t("As you charge towards him, you slide at", 2)
        s_t("the very last second, sliding underneath", 2)
        s_t(f"his stomach, your {item} slicing through", 2)
        s_t("his ankles. This was very effective. \n", 2)
        s_t("The Beast jumps feets into the air as you", 2)
        s_t("stand up. His wimpers just as loud as his", 2)
        s_t("roars. \n", 2)
    elif ANSWER in back:
        s_t("You sprint towards the beast,", 2)
        s_t(f"your {item} up like a javelin.", 2)
        s_t("The beast tries to use his tail", 2)
        s_t("to grab you but you stand on it", 2)
        s_t("and jump high into the air.", 2)
        s_t("you land on his back and run your", 2)
        s_t("weapon along his back.", 2)
        s_t("He screams out of pain, standing", 2)
        s_t("on his back, launching you far away.", 2)
        s_t("You crouch and roll on the ground", 2)
        s_t("as you connect to the floor. \n", 2)
    
    s_t("The beast is growing tired, but you have", 2)
    s_t("only just started. Your energy grows.", 2)
    s_t("The beast doesn't stop his attacks though.", 2)
    s_t("You watch as his runs and jumps up the castle", 2)
    s_t("walls.", 2)
    s_t("He twists around and launches himself towards", 2)
    s_t("you. \n", 2)

    print("What do you do? (1 dodge/ 2 attack)")
    ANSWER = input("").lower().strip()
     
    while ANSWER not in dodge and ANSWER not in attack:
        s_t(f"Invalid input. Please try again {name}.", 2)
        ANSWER = input("").lower().strip()
    
    if ANSWER in dodge:
        s_t("You roll out the way but the beast could sense it.", 2)
        s_t("he changed his direction mid way in the air", 2)
        s_t("landed right on top of you.", 2)
        s_t("You lose 2 health.", 2)
        health_stats(-2)
        check_stats()
    elif ANSWER in attack:
        s_t("You try to attack him from below but he", 2)
        s_t("had the high ground. Your attack was ineffective.", 2)
        s_t("You lose 3 health.", 2)
        health_stats(-3)
        check_stats()


def hypnotised():
    """
    Function is called no matter what path 
    the player chooses. This is the function
    to take them to the end battle.
    """
    s_t("This noise begins to take over your entire body,", 2)
    s_t("causing you to loose all control.", 2)
    s_t("Your feet start moving against your will and your", 2)
    s_t("hands begin swaying in a military formation.", 2)
    s_t("You seem to be walking so fast as you rush through", 2)
    s_t("the forest.", 2)
    s_t("In the far distance you begin to see some castle", 2)
    s_t("walls stretch across the land. \n", 2)
    s_t("The CITADEL!! \n", 2)
    s_t("You have finally made it.", 2)
    s_t("The darkness slowly started to lift as the sun rose", 2)
    s_t("beyond the clouds.", 2)
    s_t("As you near the castle walls you make a sudden stop.", 2)
    s_t("Each second that goes by you get more control back", 2)
    s_t("of your body, but you are still under this hypnosis.", 2)
    s_t("Still frozen in place you watch as the castle gates", 2)
    s_t("lower down to reveal The predator.", 2)


def the_predators_son():
    """
    This function is called if the player 
    picks 'East'when asked which direction
    they want to go from function compass.
    """
    s_t("You make your way towards the roar", 2)
    s_t("The strength of knowing your Grandma ", 2)
    s_t("has potentially gone through this has", 2)
    s_t("made you willing to fight back.", 2)
    s_t("With every step you took, the roars got", 2)
    s_t("louder and the ground shaked more.", 2)
    s_t("It was almost time. \n", 2)
    s_t("Whipping noises rung through your ears", 2)
    s_t("as the predator surrounds you.", 2)
    s_t("He is constantly speeding up, which", 2)
    s_t("is kicking up a lot of dirt and making it", 2)
    s_t("harder to see. \n", 2)
    s_t("Then he stops...", 2)
    s_t("And pounces... \n", 2)
    print("What do you do? (cower/run)")

    ANSWER = input("=>").lower().strip()

    while ANSWER not in run and ANSWER not in cower:
        s_t(f"Invalid input name. Please try again {name}", 2)
        ANSWER = input("").lower().strip()  

    if ANSWER in run:
        s_t("You tried to outrun the pounce but", 2)
        s_t("not with much luck. the predator clipped", 2)
        s_t("your clothes as he landed, dragging you", 2)
        s_t("to the floor. He then continues to drag", 2)
        s_t("you around on the ground. You can't", 2)
        s_t("escape.", 2)
        s_t("after what feels like minutes of torture.", 2)
        s_t("the predator stops playing with you", 2)
        s_t("like a toy.", 2)
        s_t("You lose 3 health.", 2)
        health_stats(-3)
        check_stats()
        s_t("however the fight isn't over yet.", 2)
        s_t("The predator takes a swipe with his", 2)
        s_t("beast like claws. You are able to dodge.", 2)
        s_t("This only angers him. He uses his tail", 2)
        s_t("and grips you around the waist.", 2)
        s_t("he lifts you in the air and raises you", 2)
        s_t("just above his head, almost as if playing", 2)
        s_t("with his food.", 2)
        print("What do you do? (1 Wriggle/ 2 Attack)")
        ANSWER = input("").lower().strip()

        while ANSWER not in wriggle and ANSWER not in attack:
            s_t(f"Invalid input name. Please try again {name}", 2)
            ANSWER = input("").lower().strip()
        if ANSWER in wriggle:
            s_t("You try to wriggle yourself free but the grip", 2)
            s_t("only gets tighter. You can feel the life being", 2)
            s_t("squeezed out of you and in that moment you", 2)
            s_t("believe this is the end.", 2)
            s_t("You lose 1 health.", 2)
            health_stats(-1)
            check_stats()
            s_t("As you are lowered into the beasts mouth,", 2)
            s_t("you decide on a risky tactic. With all the force", 2)
            s_t("you can manage you boot the beast square in the face.", 2)
            s_t("The beast wimpers and immediately drops you", 2)
            s_t("to the ground.", 2)
            s_t("The predator bolts off, leaving you on the floor.", 2)
        elif ANSWER in attack:
            s_t("With the hand that is free, you reach behind you", 2)
            s_t(f"and grab out your {item}. The predator hisses", 2)
            s_t("as you raisse the weapon and send it striking", 2)
            s_t("on his tail.", 2)
            s_t("A massive clink can be heard as it connects to", 2)
            s_t("the tail. The tail is made out of some metal.", 2)
            s_t("The predator still hisses out in pain and drops you.", 2)
            s_t("The predator bolts off, leaving you on the floor.", 2)

    elif ANSWER in cower:
        s_t("You crouch to your knees with your hands in the air,", 2)
        s_t("clutching your weapon. A dark shadow glooms over you", 2)
        s_t("quickly as you see the predator jump. At this moment", 2)
        s_t("you strike your weapon up, just catching the predators", 2)
        s_t("stomach. The predator reacted badly, first standing on", 2)
        s_t("his back legs, screaming out in pain. He then whips", 2)
        s_t("his tail at you which sends you flying into a nearby", 2)
        s_t("tree. Winded, you want him scurry away with blurred", 2)
        s_t("vision.", 2)
        s_t("You lose 3 health.", 2)
        health_stats(-3)
        check_stats()   
    
    s_t("You stand up and dust yourself off. You notice an apple", 2)
    s_t("on the floor. Starving, you eat the entire thing almost", 2)
    s_t("instantly. Your health increase by 2 points. \n", 2)
    health_stats(2)
    check_stats()

    hypnotised()

    s_t("However this doesn't look like the one you faced", 2)
    s_t("earlier. It was thrice as big.", 2)
    s_t("It had the head of a dog, and the tail like a", 2)
    s_t("tiger. You thought the", 2)
    s_t("one earlier was impossible to survive from but this ", 2)
    s_t("one was actually going to be impossible.", 2)
    s_t("And just when you thought it couldn't get worse,", 2)
    s_t("The Beast opens his mouth and speaks... \n", 2)
    s_t("'So I guess you've met one of my sons.'", 2)
    s_t("His voice so deep that it shook the ground.", 2)
    s_t("he stood fimrly, his stance intimdating you.", 2)
    s_t("'I'll make you pay for what you did to him.", 2)
    s_t("His brothers aren't very happy either.' \n", 2)
    s_t("BROTHERS?! There's an entire family of them.", 2)
    s_t("There is no escape from this... at all.", 2)

    finale_a()


play_game()