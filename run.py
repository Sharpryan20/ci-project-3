import time

from constants import *

answer = ""

def print_sleep(
    text: str, delay: int):
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
    print_sleep(
        "Your health is: " + str(user_stats["health"]), 2)

def play_again():
    """
    This function is called when the players reach the end
    of the game, health reaches 0 or their insanity level 
    rises to 5.
    """
    print("Would you like to play again? (yes/no)")
    answer = input("").lower().strip()
    while answer not in YES and answer not in NO:
        print_sleep(
            "Invalid input. Please try again.", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "Great! lets go again.", 2
            )
        play_game()
    elif answer in NO:
        print_sleep(
            "Okay no worries! Hope you enjoyed yourself.", 2
            )
    play_game()


def insanity_stats(insanity_number: int):
    """
    Increases or decreases the users insanity by a specific amount
    then displays the users with the new insanity score.
    """
    user_stats["insanity"] = user_stats["insanity"] + (insanity_number)
    print_sleep(
        "Your insanity level is: " + str(user_stats["insanity"]), 2)


def no_health():
    """
    This function is called within the check_stats function.
    If the user has of 0 or below, the player will die and the game
    will be over.
    """
    print_sleep(
        "You have been severly injured.", 2
        )
    print_sleep(
        "You are too tired to continue.", 2
        )
    print_sleep(
        "You can rest now.", 2
        )
    print_sleep(
        "The Hunt is Over", 2
        )
    print_sleep(
        '''\x1b[96m
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|\033[0m
            \n
            ''', 1)
    play_again()


def max_insanity():
    """
    This function will be called within the check_stats function.
    If the users inasity level reaches above 5, the player will halluncinate
    and the game will be over.
    """
    print_sleep(
        "You start to see things, things that aren't really there.", 2
        )
    print_sleep(
        "There is no going back now.", 2
        )
    print_sleep(
        "You lose all control over your body and you run off...", 2
        )
    print_sleep(
        "Never to be seen again", 2
        )
    print_sleep(
        '''\x1b[96m
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|\033[0m
            \n
            ''', 1)
    play_again()

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
    print(
        """\033[94m
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
    \033[0m\n"""
    )

    print("Are you ready to join us in The Hunt? (yes/no)")
    answer = input("").lower().strip()
    while answer not in YES and answer not in NO:
        print_sleep(
            "Invalid input Please try again.", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "Brillant!! Lets start", 2
            )
        global name
        name = input("What is your name? \n")
        print_sleep(
            f"Hello {name}... GOODLUCK!!!", 2
            )
        print_sleep(
            "HAHAHAHA \n", 2
            )
        opening()
    elif answer in NO:
        print("That's a shame. See you around!")


def opening():
    """
    Function called after player has entered their name.
    """
    print_sleep(
        "You wake up... dazed!", 2
        )
    print_sleep(
        "The gloomy forest sets in as you realise you are lost.", 2
        )
    print_sleep(
        "The place has a sense of familarity but", 2
        )
    print_sleep(
        "you aren't quite sure how.", 2
        )
    print_sleep(
        "You stumble to your feet and frantically search", 2
        )
    print_sleep(
        "for shelter as the moon slowly rises.", 2
        )
    print_sleep(
        "In the distance you see the roof of a small building", 2
        )
    print_sleep(
        "peering out behind the trees", 2
        )
    print_sleep(
        "The fog has already began to set and you make your", 2
        )
    print_sleep(
        "to the dainty, creepy shed", 2
        )
    print_sleep(
        "When you approach the door you see a faint orange glow ", 2
        )
    print_sleep(
        "appear in the doorway, which is slightly ajar \n", 2
        )

    print("Do you open the door? (yes/no?)")

    answer = input("").lower().strip()

    while answer not in YES and answer not in NO:
        print_sleep(
            f"Invalid input Please try again {name}", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "The door slowly creeps open revealing an open room,", 2
            )
        print_sleep(
            "and in the middle of it stands a tall dark figure,", 2
            )
        print_sleep(
            "a cloak covering the entity from head to toe.", 2
            )
    elif answer in NO:
        print_sleep(
            "You walk around and peer through a window", 2
            )
        print_sleep(
            "for a better look when suddenly a dark figure", 2
            )
        print_sleep(
            "jumps at the window. Startled, you take a step back.", 2
            )
        print_sleep(
            "The man gesutres you to come inside.", 2
            )
        print_sleep(
            "You make your way back around to the door and enter.", 2
            )
        print_sleep(
            "Your insanity level has increased \n", 2
            )
        insanity_stats(+2)
        check_stats()

    print_sleep(
        "The man lifts his hood and points to a chair.", 2
        )
    print_sleep(
        "You catch on and sit down in the worn chair", 2
        )
    print_sleep(
        "He throws more wood on the fire and just stands there", 2
        )
    print_sleep(
        "watching it roar as the flames warm up the room.", 2
        )
    print_sleep(
        "You begin to feel uneasy as he scurries closer to you.", 2
        )
    print_sleep(
        f"So {name}, I see you are finally awake!", 2
        )
    print_sleep(
        "Do you want to know why you are here? \n", 2
        )

    print("Do you answer back? (yes/no)")
    answer = input("").lower().strip()

    while answer not in YES and answer not in NO:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "You nod and say;'Wait how do you know my name?'", 2
            )
        print_sleep(
            "'Where am I?'", 2
            )

    elif answer in NO:
        print_sleep(
            "You questioned how he knew your name", 2
            )
        print_sleep(
            "but decided not to say anything.", 2
            )

    print_sleep(
        "The man paces back and forth, almost to say something", 2
        )
    print_sleep(
        "'It doesn't matter how I know your name!'", 2
        )
    print_sleep(
        "He snapped as he twisted his head almost 180 degrees", 2
        )
    print_sleep(
        "'All that matters is The Hunt can now begin.'", 2
        )
    print_sleep(
        "he lifted his hands up just as a clap of thunder bellowed", 2
        )
    print_sleep(
        "almost as if the man had summoned the phenomenon. \n", 2
        )
    print_sleep(
        "'The Hunt?' You question, your hands shake with fear \n", 2
        )
    print_sleep(
        "'The hunt is a matter of life and death. Unfortunately", 2
        )
    print_sleep(
        "you have been assigned the role of prey.", 2
        )
    print_sleep(
        "You have 8 hours to survive the forest and make it to", 2
        )
    print_sleep(
        "THE CITADEL!!", 2
        )
    print_sleep(
        "You will be given a weapon though.", 2
        )
    print_sleep(
        "He makes his way towards the cupboard and opens it.", 2
        )
    print_sleep(
        "He hands you over a sword.", 2
        )
    global item
    item = input("What do you name the sword? \n")
    print_sleep(
        f"I see you named it {item}. Good choice", 2
        )
    print_sleep(
        f"You pick up {item}.", 2
        )
    print_sleep(
        "You turn to ask who the predator is but the man is gone.", 2
        )
    print_sleep(
        "Any indication that he was here is the cloak bundled up.", 2
        )
    print_sleep(
        "You bend down and run the cloak through your fingers \n", 2
        )

    print("Do you pick it up? (yes/no)")
    answer = input("").lower().strip()
    while answer not in YES and answer not in NO:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "You place the cloak over your shoulders and leave.", 2
            )
    elif answer in NO:
        print_sleep(
            "You stand back up and head to the door.", 2
            )

    print_sleep(
        "As you leave you notice a drawer cracked open slightly. \n", 2
        )

    print("Do you open it? (yes/no)")
    answer = input("").lower().strip()
    while answer not in YES and answer not in NO:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in YES:
        print_sleep(
            "you see a note inside and a photo. It's of you.", 2
            )
        print_sleep(
            "You unfold the note and it reads; 'I'm sorry.", 2
            )
        print_sleep(
            "They made me do it, Please forgive me!'\n", 2
            )
        print_sleep(
            "You put the note in your pocket and walk out the door.", 2
            )
    elif answer in NO:
        print_sleep(
            "You decide not to open it and leave the house. \n", 2
            )

    print_sleep(
        "You notice a hanging latern the porch.", 2
        )
    print_sleep(
        "You take it off the wall and start your journey. \n", 2
        )

    the_walk()


def the_walk():
    """
    This function is the second part of the Game where the
    player has just left the house.
    There will consist nested if/else statements as the player progresses."
    """
    print_sleep(
        "It feels like hours have passed since you started.", 2
        )
    print_sleep(
        "The path strecthed out for ages, you've had nothing", 2
        )
    print_sleep(
        "to keep you company expect the whistling winds as", 2
        )
    print_sleep(
        "they raced through the trees.", 2
        )
    print_sleep(
        "The thunder had stopped but the rain was still hard.\n", 2
        )
    print_sleep(
        "FINALLY!!! \n", 2
        )
    print_sleep(
        "The path splits into two.", 2
        )

    print("Do you go straight or right? (straight/right)")
    answer = input("").lower().strip()

    while answer not in STRAIGHT and answer not in RIGHT:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()

    if answer in STRAIGHT:
        print_sleep(
            "You continue and suddenly hear a rustle.", 2
            )
        print_sleep(
            "You turn to see a bush", 2
            )
        walk_scenario_one()
    elif answer in RIGHT:
        print_sleep(
            "You turn right and you start walking.", 2
            )
        print_sleep(
            "You start hearing things, like screeches.", 2
            )
        print_sleep(
            "The noises get louder and louder, becoming", 2
            )
        print_sleep(
            "near impossible to even hear your thoughts.", 2
            )
        walk_scenario_two()


def the_walk_part_b():
    """
    The second part of the the_walk() function which both players
    will recieve no matter what path they go down.
    """
    print_sleep(
        "It starts to get colder the further you walk into the forest.", 2
        )
    print_sleep(
        "You begin to fear that there was no end to this nightmare.", 2
        )
    print_sleep(
        "And in fact you were destined to die out here.", 2
        )
    print_sleep(
        "You try to remember anything as to how you,", 2
        )
    print_sleep(
        "ended up here. Why was it so familiar?", 2
        )
    print_sleep(
        "Who was that man?", 2
        )
    print_sleep(
        "How did he know your name?", 2
        )
    print_sleep(
        "Is this some sick joke?", 2
        )
    print_sleep(
        "Is this even legal? It can't be?", 2
        )


def walk_scenario_one():
    """
    This is the first scenario for the_walk() function
    Will only be called if player continues straight in
    the PickDirection if/else statement.
    """
    print("What do you do? (1 Use weapon/ 2 Walk)")
    answer = input("").lower().strip()
    while answer not in USE_WEAPON and answer not in CARRY_WALKING:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in USE_WEAPON:
        print_sleep(
            "You poke the bush and the rustling stops", 2
            )
        print_sleep(
            "but a few seconds later a badger jumps at you", 2
            )
        print_sleep(
            "and scratches you.", 1)
        print_sleep(
            "You lose 2 health and your insanity increases.", 2
            )
        health_stats(-2)
        insanity_stats(2)
        check_stats()
    elif answer in CARRY_WALKING:
        print_sleep(
            "The rustling stops after a few seconds.", 2
            )
        print_sleep(
            "you quickly scurry past and continue your walk,", 2
            )
        print_sleep(
            "careful not to disturb the beast.", 2
            )

    the_walk_part_b()
    the_walk_1_a()


def the_walk_1_a():
    """
    This function is called
    the player takes the straight path and after
    the_walk_part_b() is called.
    """
    print_sleep(
        "The path begins to fade out as nature covers the concrete.", 2
        )
    print_sleep(
        "No one has been down here in a while.", 2
        )
    print_sleep(
        "Have you chosen the right path?", 2
        )
    print_sleep(
        "Is the predator down here?", 2
        )
    print_sleep(
        "You try to stay strong.", 2
        )
    print_sleep(
        "You have come to far to give up now, surely there is only,", 2
        )
    print_sleep(
        "a few hours left to the go.", 2
        )
    print_sleep(
        "Your latern begins to flicker ever so slightly.", 2
        )
    print_sleep(
        "The winds have almost completely stopped, making it more eerie", 2
        )
    print_sleep(
        "than before.", 2
        )
    print_sleep(
        "You step in a puddle and you foot becomes soaked.", 2
        )
    print_sleep(
        "But is it rain water?", 2
        )
    print_sleep(
        "You bend down and a faint dark red begins to show. \n", 2
        )
    print_sleep(
        "No! ", 2
        )
    print_sleep(
        "It can't be.", 2
        )
    print_sleep(
        "You feel a drop on your head and you look up. \n", 2
        )
    print_sleep(
        "You muffle your own screams as you realise its not rain but", 2
        )
    print_sleep(
        "infact blood. \n", 2
        )
    print_sleep(
        "THE BEAST! \n", 2
        )
    print_sleep(
        "You take off into the woods, no longer following a path.", 2
        )
    print_sleep(
        "Your heart pants like crazy, your eyesight blurred,", 2
        )
    print_sleep(
        "as fear escapes your eyes", 2
        )
    print_sleep(
        "It's safe for the time being.", 2
        )
    print_sleep(
        "However in the distant you hear chanting...", 2
        )
    print_sleep(
        "you can't make out what they are saying over the banging", 2
        )
    print_sleep(
        "of the drums.", 2
        )
    print_sleep(
        "To your right you smoke rising into the sky, behind the trees.", 2
        )
    print_sleep(
        "Fire!!", 2
        )
    print_sleep(
        "You are torn for choice.", 2
        )

    print("Where do you go? (1 Chanting/ 2 Fire)")
    answer = input("").lower().strip()

    while answer not in CHANTING and answer not in FIRE:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in CHANTING:
        the_chant()
    elif answer in FIRE:
        the_fire()


def the_fire():
    """
    This function is called when the player
    picks option two in the PickDirectionTwo
    if/else statement.
    """
    print_sleep(
        "You make your way to the smoke.", 2
        )
    print_sleep(
        "Ash starts to consume the atmosphere.", 2
        )
    print_sleep(
        "the flickering of the fire is the only", 2
        )
    print_sleep(
        "comforting sound you've heard in a while.", 2
        )
    print_sleep(
        "It's a nice sound.", 2
        )
    print_sleep(
        "As you approach the area you see a log being used as a bench.", 2
        )
    print_sleep(
        "A lone figure is occupying one of the benches.", 2
        )
    print_sleep(
        "Hesitantly, you make your way and notice something. \n", 2
        )

    potion()


def potion():
    print_sleep(
        "It's the man! the man from the beginning.", 2
        )
    print_sleep(
        "As if by magic, the man turns around. There is no way", 2
        )
    print_sleep(
        "he heard you coming. \n", 2
        )
    print_sleep(
        f"'Well {name} glad to know you made it this far.", 2
        )
    print_sleep(
        "Although we never doubted you at all. ", 2
        )
    print_sleep(
        "Have you met the predator yet?'", 2
        )
    print_sleep(
        "You shake your head.", 2
        )
    print_sleep(
        "'Oh wow! that's lucky.", 2
        )
    print_sleep(
        "Most people don't make it this far.'", 2
        )
    print_sleep(
        "You have been through the wars though.", 2
        )
    print_sleep(
        "I'm going to offer two potions. You may only pick one though.", 2
        )
    print_sleep(
        "One will increase your health back up, the other will decrease", 2
        )
    print_sleep(
        "your insanity level. So which will it be? \n", 2
        )
    health_stats(0)
    insanity_stats(0)
    print("Which potion do you want? (1 Health/ 2 Insanity)")
    answer = input("").lower().strip()
    while answer not in POTION_HEALTH and answer not in POTION_INSANITY:
        print_sleep(
            "Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in POTION_HEALTH:
        print_sleep(
            "Good choice. Take this and drink it and your health will", 2
            )
        print_sleep(
            "increase by 3 points. \n", 2
            )
        print_sleep(
            "You take the potion and drink the whole thing in one go,", 2
            )
        print_sleep(
            "forgetting about your dehydration.", 2
            )
        print_sleep(
            "You feel the potion work it's way through your body,", 2
            )
        print_sleep(
            "giving you more strength than before.", 2
            )
        health_stats(3)
        print_sleep(
            "", 2
            )
        print_sleep(
            "Something doesn't feel right now though.", 2
            )
        print_sleep(
            "You start hearing noises, but there's nothing around. \n", 2
            )
        print_sleep(
            "The faint chuckles cause you to turn around to see the man", 2
            )
        print_sleep(
            "trying to stifle his laughter. This can't be good. \n", 2
            )
        print_sleep(
            "'Oh Man! you gobbled that right up. Without hesitation.", 2
            )
        print_sleep(
            "Did you really think I was going to let you just make", 2
            )
        print_sleep(
            f"yourself stronger. Dear {name} you still have a lot to", 2
            )
        print_sleep(
            "learn. Everything comes with a price.' \n", 2
            )
        print_sleep(
            "A pounding in your head clouds your thoughts.", 2
            )
        print_sleep(
            "You quickly piece together what has happened. \n", 2
            )
        print_sleep(
            "'For the price of more health your insanity has been", 2
            )
        print_sleep(
            "increased. HAHAHA!!!' \n", 2
            )
        insanity_stats(1)
        print_sleep(
            "", 2
            )
        print_sleep(
            "And just like that, the man had disappeared... again.", 2
            )
    elif answer in POTION_INSANITY:
        print_sleep(
            "Good Choice! Take this and your insanity level will", 2
            )
        print_sleep(
            "decrease by 2", 2
            )
        print_sleep(
            "You don't hesitate and gulp the potion down with ease.", 2
            )
        print_sleep(
            "The effects of the potion happen almost instantly,", 2
            )
        print_sleep(
            "your thoughts became clearer. \n", 2
            )
        insanity_stats(-2)
        print_sleep(
            "However, almost immediately afterwards you feel a sharp", 2
            )
        print_sleep(
            "pain in your stomach, you crouch over to stop the pain.", 2
            )
        print_sleep(
            "The faint chuckles cause you to turn around to see the man", 2
            )
        print_sleep(
            "trying to stifle his laughter. This can't be good. \n", 2
            )
        print_sleep(
            "'Oh Man! you gobbled that right up. Without hesitation.", 2
            )
        print_sleep(
            "Did you really think I was going to let you just make", 2
            )
        print_sleep(
            f"yourself stronger. Dear {name} you still have a lot to", 2
            )
        print_sleep(
            "learn. Everything comes with a price.' \n", 2
            )
        print_sleep(
            "The stabbing pain only grows worse.", 2
            )
        print_sleep(
            "You quickly piece together what has happened. \n", 2
            )
        print_sleep(
            "'For the price of less insanity your health has been", 2
            )
        print_sleep(
            "decreased. HAHAHA!!!' \n", 2
            )
        health_stats(-3)
        print_sleep(
            "", 2
            )
        print_sleep(
            "And just like that, the man had disappeared... again.", 2
            )

    hypnotised()
    finale_a()


def the_chant():
    """
    This function is called when the player
     picks option 1 in the_walk_1_a().
    """
    print_sleep(
        "You slowly make your way to the chanting", 2
        )
    print_sleep(
        "trying not to alert your position to them.", 2
        )
    print_sleep(
        "The noise gets louder and louder as you near them.", 2
        )
    print_sleep(
        "Eventually the sounds seem to surround you.", 2
        )
    print_sleep(
        "You step on a twig and it crunches.", 2
        )
    print_sleep(
        "The chanting abruptly stops.", 2
        )
    print_sleep(
        "One by one, eyes start staring at you as you spin around. \n", 2
        )
    print_sleep(
        "You're trapped.", 2
        )
    print_sleep(
        "There's no escape. ", 2
        )
    print_sleep(
        "The eyes seem to be floating closer to you.", 2
        )
    print_sleep(
        "And with that your latern goes out, leaving the moon as", 2
        )
    print_sleep(
        "your only source of light.", 2
        )
    print_sleep(
        "The glow of the moon higlights the chanters, however", 2
        )
    print_sleep(
        "they are still silent. \n", 2
        )
    print_sleep(
        "Your insanity level increases by 2.", 2
        )
    insanity_stats(2)
    check_stats()
    print_sleep(
        "", 2
        )
    print_sleep(
        "You see a bony finger come towards you and within seconds", 2
        )
    print_sleep(
        "You feel many hands grasp you and lift you off the ground", 2
        )
    print_sleep(
        "There's no luck in escaping as you try to wriggle out.\n", 2
        )
    print_sleep(
        "After what feels like hours of being held hostage but was a", 2
        )
    print_sleep(
        "measley few minutes, they drop you down on the floor. ", 2
        )
    print_sleep(
        "The smell of smoke fills your nostrils as you look around", 2
        )
    print_sleep(
        "and notice the smoke from the fire was closer than before.", 2
        )
    print_sleep(
        "They form another circle around you and watch as you", 2
        )
    print_sleep(
        "stumble to your feet.", 2
        )
    print_sleep(
        "You hold onto your weapon as you decide your next move.", 2
        )

    print("Do you attack? (yes/no)")
    answer = input("").lower().strip()

    while answer not in YES and answer not in NO:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()

    if answer in YES:
        print_sleep(
            "You take out your weapon and point it to one of the members.", 2
            )
        print_sleep(
            "They try to snatch it out your hands but you are too quick.", 2
            )
        print_sleep(
            "You end up snipping their hands as you pull back.", 2
            )
        print_sleep(
            "However, the rest aren't scared by that encounter,", 2
            )
        print_sleep(
            "in fact they seem to get closer than before.", 2
            )
        print_sleep(
            "They all start chanting again and you immediately", 2
            )
        print_sleep(
            "drop your weapon, becoming completely hypontised.", 2
            )
        print_sleep(
            "You start levitating, only this time no one is grabbing you.", 2
            )
        print_sleep(
            "Then all of a sudden you fell to the ground, hard.", 2
            )
        print_sleep(
            "You lay there unable to move as you are winded. \n", 2
            )
        print_sleep(
            "Your health drops 3 points.", 2
            )
        health_stats(-3)
        check_stats()
        print_sleep(
            "", 2
            )
        print_sleep(
            "When you look around again, you see that they have all", 2
            )
        print_sleep(
            "disappeared, just like the man back at the building.", 2
            )
        print_sleep(
            "'I wonder if he is connected to them.' You say out loud.", 2
            )
        print_sleep(
            "You make your way over to the fire, and sit down.", 2
            )
        print_sleep(
            "It feels good to be able to sit down.", 2
            )
    elif answer in NO:
        print_sleep(
            "You go to take out your weapon but think better off it.", 2
            )
        print_sleep(
            "There's way to many to take on alone.", 2
            )
        print_sleep(
            "They all slowly turn to face one direction and then", 2
            )
        print_sleep(
            "in unity, they all start gliding away, floating", 2
            )
        print_sleep(
            "out of the cloaks and leaving them on the floor.", 2
            )
        print_sleep(
            "Just like the man in the building.", 2
            )
        print_sleep(
            "The fires tempts you as you realise you are freezing.", 2
            )

    print_sleep(
        "After a while you hear a rustle in the bushes and you", 2
        )
    print_sleep(
        "immediately tense up. However, there was almost a difference", 2
        )
    print_sleep(
        "You saw some eyes glow and a something walked out.", 2
        )

    potion()


def walk_scenario_two():
    """
    This function will only be called if the player
     turns right from the PickDirection question.
    """
    print("What do you do? (1 Stand/ 2 Run)")
    answer = input("").lower().strip()

    while answer not in STAND and answer not in RUN:
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in STAND:
        print_sleep(
            "The ground starts rumbling as you stand frozen.", 2
            )
        print_sleep(
            "Then out of nowhere, a herd of deers come stampeding", 2
            )
        print_sleep(
            "towards you. You crouch down to avoid a blow.", 2
            )
        print_sleep(
            "However that wasn't wise. The deers trampled you as", 2
            )
        print_sleep(
            "you laid hopeless. You lose 3 health.", 2
            )
        health_stats(-3)
        check_stats()
    elif answer in RUN:
        print_sleep(
            "You bolt in the opposite direction of the sounds,", 2
            )
        print_sleep(
            "trying your best to out run the predators.", 2
            )
        print_sleep(
            "However it wasn't a predator but a herd of deer.", 2
            )
        print_sleep(
            "They were sprinting at full speed and almost", 2
            )
        print_sleep(
            "immediately ran past you. One wasn't quite as fast", 2
            )
        print_sleep(
            "and was beginning to trail behind. You wait for it", 2
            )
        print_sleep(
            "to get closer to you and as it apporaches you grab his", 2
            )
        print_sleep(
            "antlers and hop on the back.", 2
            )
        print_sleep(
            "Now startled, the deer speeds up and within time", 2
            )
        print_sleep(
            "has caught back up to the herd.", 2
            )
        print_sleep(
            "'What was they running from?'", 2
            )
        print_sleep(
            "You hop off the deer and head back, realising you", 2
            )
        print_sleep(
            "had dropped your weapon.", 2
            )

    the_walk_part_b()
    the_walk_1_b()


def the_walk_1_b():
    """
    This function is called after the player
    has gone through the_walk_scenario_two().
    """

    print_sleep(
        "You are thirsty but there's no water around.", 2
        )
    print_sleep(
        "There was a water source about a mile back that", 2
        )
    print_sleep(
        "you remember seeing but decide against it as.", 2
        )
    print_sleep(
        "Those deers were running from something and", 2
        )
    print_sleep(
        "you weren't about to find out either.", 2
        )
    print_sleep(
        "Forward was the only option. \n", 2
        )
    print_sleep(
        "The trek began to take a toll on you.", 2
        )
    print_sleep(
        "You needed to sit down as soon as.", 2
        )
    print_sleep(
        "But just as you were about to the stop,", 2
        )
    print_sleep(
        "the sound of trickling water blessed your", 2
        )
    print_sleep(
        "ears. You sprint as fast as your tired", 2
        )
    print_sleep(
        "legs will take you. \n", 2
        )
    print_sleep(
        "A river!! \n", 2
        )
    print_sleep(
        "It has been the best thing to happen since", 2
        )
    print_sleep(
        "you woke up in this nightmare", 2
        )
    print_sleep(
        "You bend down and cup your hands,", 2
        )
    print_sleep(
        "trying to gather as much as possible.", 2
        )
    print_sleep(
        "The night grew more cold, causing shivers", 2
        )
    print_sleep(
        "to run through your spine like electical", 2
        )
    print_sleep(
        "currents. Warmth will be the next task.", 2
        )
    print_sleep(
        "The path is no longer in eyesight as you", 2
        )
    print_sleep(
        "strayed away from it to get hydrated.", 2
        )
    print_sleep(
        "Every direction looks the same.", 2
        )

    compass()


def compass():
    """
    This function is called after
    the_walk_1_b.
    """
    print("Which direction shall you go? (North/South/East/West)")
    answer = input("").lower().strip()

    while (
        answer not in NORTH
        and answer not in SOUTH
        and answer not in EAST
        and answer not in WEST
    ):
        print_sleep(
            f"Invalid input Please try again {name}.", 2
            )
        answer = input("").lower().strip()
    if answer in NORTH:
        print_sleep(
            "You start walking North but after a while", 2
            )
        print_sleep(
            "you are stopped by an invisible barrier.", 2
            )
        print_sleep(
            "There is no other choice but to go back. \n", 2
            )
        compass()
    elif answer in SOUTH:
        print_sleep(
            "South seems like a wise choice.", 2
            )
        print_sleep(
            "There's a lot of coverage with trees", 2
            )
        print_sleep(
            "but not too much that you can't see", 2
            )
        print_sleep(
            "potential dangers.", 2
            )
        print_sleep(
            "After a while you realise the", 2
            )
        print_sleep(
            "area seems familar. \n", 2
            )
        print_sleep(
            "You are back at the river, the", 2
            )
        print_sleep(
            "exact same spot. Your footprints", 2
            )
        print_sleep(
            "remain indented in the floor.", 2
            )
        print_sleep(
            "You'll need to pick another", 2
            )
        print_sleep(
            "direction. \n", 2
            )
        compass()
    elif answer in EAST:
        print_sleep(
            "East was in the same direction as", 2
            )
        print_sleep(
            "the flow of river. \n", 2
            )
        print_sleep(
            "'It has to lead somewhere.", 2
            )
        print_sleep(
            "All rivers lead to something.'", 2
            )
        print_sleep(
            "You say out loud. up until today", 2
            )
        print_sleep(
            "you never spoke to yourself but ", 2
            )
        print_sleep(
            "today has changed all that.", 2
            )
        print_sleep(
            "Your grandma told you one day", 2
            )
        print_sleep(
            "'you'll start and won't ever want", 2
            )
        print_sleep(
            "to stop. Mine started one day in", 2
            )
        print_sleep(
            "the forest while trekking through", 2
            )
        print_sleep(
            "some serious thunderstorms.' \n", 2
            )
        print_sleep(
            "You stop dead in your tracks.", 2
            )
        print_sleep(
            "The story of your grandma seemed", 2
            )
        print_sleep(
            "a little too like your situation", 2
            )
        print_sleep(
            "right now.", 2
            )
        print_sleep(
            "Did Grandma go through this as well?", 2
            )
        print_sleep(
            "Is that why everything looks so", 2
            )
        print_sleep(
            "familar? \n", 2
            )
        print_sleep(
            "Just as you finish that thought", 2
            )
        print_sleep(
            "the ground beging shaking violently", 2
            )
        print_sleep(
            "as a roar ruptures through the sky. \n", 2
            )
        print_sleep(
            "The predator is near. \n", 2
            )
        the_predators_son()
    elif answer in WEST:
        print_sleep(
            "You go west in hopes of setting up a camp site", 2
            )
        print_sleep(
            "although with your luck there won't be", 2
            )
        print_sleep(
            "anything to set up camp with.", 2
            )
        print_sleep(
            "After about 5 minutes of walking you decide to", 2
            )
        print_sleep(
            "set up here. you begin to look around to find", 2
            )
        print_sleep(
            "any wood that is dry enough to light, although", 2
            )
        print_sleep(
            "everything has been soaked from the rain.", 2
            )
        print_sleep(
            "You try lighting some logs with your latern but", 2
            )
        print_sleep(
            "you burn youself doing so. You start smelling", 2
            )
        print_sleep(
            "smoke in the air but you assume its from the", 2
            )
        print_sleep(
            "attempts of your own fire. However, you look", 2
            )
        print_sleep(
            "around and see smoke rising and and disappearing", 2
            )
        print_sleep(
            "into thin air. \n", 2
            )
        print_sleep(
            "Finally!! \n", 2
            )
        print_sleep(
            "You sprint in the direction of the smoke.", 2
            )
        print_sleep(
            "You can almost fee lthe warmth filling your", 2
            )
        print_sleep(
            "body before you even reach it.", 2
            )

        the_fire()
        potion()


def finale_part_a():
    """
    This function is called no matter what path
    the users take. This is the start of the
    finale.
    """
    print_sleep(
        "As the predator got closer you could feel the", 2
        )
    print_sleep(
        "fear radiating from your body, and he could sense ", 2
        )
    print_sleep(
        "it. \n", 2
        )
    print_sleep(
        "'I cannot let you in this castle. You are a hard one", 2
        )
    print_sleep(
        "to track down. I've been waiting for this moment for", 2
        )
    print_sleep(
        "20 years. She was right you know! Your grandmother.", 2
        )
    print_sleep(
        "She has been the only person able to beat me, but she", 2
        )
    print_sleep(
        "told that you would be able to as well.' \n", 2
        )
    print_sleep(
        "'What do you know about my Grandma??!!!' You scream", 2
        )
    print_sleep(
        "The Beasts laughter drowing out your screams. He knew", 2
        )
    print_sleep(
        "you were scared.", 2
        )
    print_sleep(
        "You take a defensive stance, your hand holding", 2
        )
    print_sleep(
        "the handle of your weapon.", 2
        )
    print_sleep(
        "Dawn rose through the clouds and you began to take", 2
        )
    print_sleep(
        "in your surroundings. It's not real....", 2
        )
    print_sleep(
        "None of it is. Is it a simulation? \n", 2
        )
    print_sleep(
        "'You've only got 10 minutes to defeat me.' He said", 2
        )
    print_sleep(
        "stil smirking. \n", 2
        )
    print_sleep(
        "'That long huh' you reciprocate his smirk, growing", 2
        )
    print_sleep(
        "more confident by the second...", 2
        )
    finale_b()


def finale_part_b():
    """
    This function is called after finale_a.
    This is all the questions the players
    wille be asked in the finale.
    """
    print_sleep(
        "The Beast jumps at you.", 2
        )
    print("What do you do? (1 dodge/ 2 attack)")
    answer = input("").lower()

    while answer not in ATTACK and answer not in DODGE:
        print_sleep(
            f"Invalid input. Please try again {name}", 2
            )
        answer = input("").lower().strip()
    if answer in DODGE:
        print_sleep(
            "You successfully dodge the attack.", 2
            )
        print_sleep(
            "This only enrages him more. \n", 2
            )
    elif answer in ATTACK:
        print_sleep(
            "You strike your weapon at the beast.", 2
            )
        print_sleep(
            "However he is too quick and dodges you, but", 2
            )
        print_sleep(
            "scratches your legs in the process. \n", 2
            )

    print_sleep(
        "The beast turns to look at you again, this time", 2
        )
    print_sleep(
        "with anger pouring at his eyes.", 2
        )
    print_sleep(
        "He roars, which echos and bounces off these", 2
        )
    print_sleep(
        "invisible barriers. It startles you and then", 2
        )
    print_sleep(
        "he strikes you again, charging at full speed.", 2
        )

    print("What do you do? (1 dodge/ 2 attack)")
    answer = input("").lower().strip()

    while answer not in ATTACK and answer not in DODGE:
        print_sleep(
            f"Invalid input. Please try again {name}.", 2
            )
        answer = input("").lower().strip()

    if answer in DODGE:
        print_sleep(
            "You try to dodge but the beast anticipated", 2
            )
        print_sleep(
            "your move this time. He attacks your arm", 2
            )
        print_sleep(
            "You lose one health. \n", 2
            )
        health_stats(-1)
        check_stats()
        print_sleep(
            "", 2
            )
    elif answer in ATTACK:
        print_sleep(
            "You stand with your back against him.", 2
            )
        print_sleep(
            "As you hear him get closer you swing at", 2
            )
        print_sleep(
            "full power and hit him straight in the", 2
            )
        print_sleep(
            "face. This sends him back a few feet,", 2
            )
        print_sleep(
            "causing him to lose balance. \n", 2
            )

    print_sleep(
        "'You are going to have to try a lot harder than", 2
        )
    print_sleep(
        f"that {name}. I know your Grandmother did.'", 2
        )
    print_sleep(
        "Hearing him talk about your Grandma like that ", 2
        )
    print_sleep(
        "makes you so angry. Thinking how she had to go", 2
        )
    print_sleep(
        "through this as well. \n", 2
        )
    print_sleep(
        "This time you strike first.", 2
        )

    print("Where do you attack? (1 legs/ 2 back)")
    answer = input("").lower().strip()

    while answer not in LEGS and answer not in BACK:
        print_sleep(
            f"Invalid input. Please try again {name}", 2
            )
        answer = input("").lower().strip()

    if answer in LEGS:
        print_sleep(
            "As you charge towards him, you slide at", 2
            )
        print_sleep(
            "the very last second, sliding underneath", 2
            )
        print_sleep(
            f"his stomach, your {item} slicing through", 2
            )
        print_sleep(
            "his ankles. This was very effective. \n", 2
            )
        print_sleep(
            "The Beast jumps feets into the air as you", 2
            )
        print_sleep(
            "stand up. His wimpers just as loud as his", 2
            )
        print_sleep(
            "roars. \n", 2
            )
    elif answer in BACK:
        print_sleep(
            "You sprint towards the beast,", 2
            )
        print_sleep(
            f"your {item} up like a javelin.", 2
            )
        print_sleep(
            "The beast tries to use his tail", 2
            )
        print_sleep(
            "to grab you but you stand on it", 2
            )
        print_sleep(
            "and jump high into the air.", 2
            )
        print_sleep(
            "you land on his back and run your", 2
            )
        print_sleep(
            "weapon along his back.", 2
            )
        print_sleep(
            "He screams out of pain, standing", 2
            )
        print_sleep(
            "on his back, launching you far away.", 2
            )
        print_sleep(
            "You crouch and roll on the ground", 2
            )
        print_sleep(
            "as you connect to the floor. \n", 2
            )

    print_sleep(
        "The beast is growing tired, but you have", 2
        )
    print_sleep(
        "only just started. Your energy grows.", 2
        )
    print_sleep(
        "The beast doesn't stop his attacks though.", 2
        )
    print_sleep(
        "You watch as his runs and jumps up the castle", 2
        )
    print_sleep(
        "walls.", 2
        )
    print_sleep(
        "He twists around and launches himself towards", 2
        )
    print_sleep(
        "you. \n", 2
        )

    print("What do you do? (1 dodge/ 2 attack)")
    answer = input("").lower().strip()

    while answer not in DODGE and answer not in ATTACK:
        print_sleep(
            f"Invalid input. Please try again {name}.", 2
            )
        answer = input("").lower().strip()

    if answer in DODGE:
        print_sleep(
            "You roll out the way but the beast could sense it.", 2
            )
        print_sleep(
            "he changed his direction mid way in the air", 2
            )
        print_sleep(
            "landed right on top of you.", 2
            )
        print_sleep(
            "You lose 2 health.", 2
            )
        health_stats(-2)
        check_stats()
    elif answer in ATTACK:
        print_sleep(
            "You try to attack him from below but he", 2
            )
        print_sleep(
            "had the high ground. Your attack was ineffective.", 2
            )
        print_sleep(
            "You lose 3 health.", 2
            )
        health_stats(-3)
        check_stats()
    finale_c()


def finale_part_c():
    """
    This is the final function called
    in this file. It also asks the player if
    they want to play again.
    """
    print_sleep(
        "The beast was effective with his attacks. He was still", 2
        )
    print_sleep(
        "weak from your blows though. 'Not long now' you think", 2
        )
    print_sleep(
        "to yourself. One more attack and he should be defeated. \n", 2
        )
    print_sleep(
        "You both charge towards each other and almost in sync,", 2
        )
    print_sleep(
        "you both jump high into the air.", 2
        )
    print_sleep(
        "You somehow get a higher jump than the beast and land", 2
        )
    print_sleep(
        "on his head, to which you use it as a launchpad.", 2
        )
    print_sleep(
        f"while in the air you take out your {item} and land", 2
        )
    print_sleep(
        "on the Beasts back as you both continue to fall to the", 2
        )
    print_sleep(
        "ground. the beast collapses to the floor as you plummet", 2
        )
    print_sleep(
        "your weapon into his back. He screams out. \n", 2
        )
    print_sleep(
        "It's not over though.", 2
        )
    print_sleep(
        "You get off the beast and fall to the floor. You are", 2
        )
    print_sleep(
        "exhausted from the fight.", 2
        )
    print_sleep(
        "All of a sudden you see these lights come down from", 2
        )
    print_sleep(
        "the sky and lift the beast in the air.", 2
        )
    print_sleep(
        "They wrap around him like a blanket, and within", 2
        )
    print_sleep(
        "seconds the beast had transformed into a man... \n", 2
        )
    print_sleep(
        "THE MAN! \n", 2
        )
    print_sleep(
        "It was him all along. \n", 2
        )
    print_sleep(
        "He starts to talk, but not from his mouth, almost as", 2
        )
    print_sleep(
        "if someone was talking for him. \n", 2
        )
    print_sleep(
        "'Well done! I wasn't sure if you actually had it in", 2
        )
    print_sleep(
        "you to defeat him. I modified him and made him stronger", 2
        )
    print_sleep(
        "since I was able to defeat him.' The voice spoke. Strangely", 2
        )
    print_sleep(
        "familiar. Then it hit you. \n", 2
        )
    print_sleep(
        "'Grandma?' You manage to stutter. \n", 2
        )
    print_sleep(
        "'Well you figured it out! It is me dear! Your sister", 2
        )
    print_sleep(
        "couldn't figure it out though. I'll explain it all", 2
        )
    print_sleep(
        "soon I promise.'", 2
        )
    print_sleep(
        "And with that the voice was gone and the man dropped", 2
        )
    print_sleep(
        "to the floor. Seconds after an intercom system spoke out.", 2
        )
    print_sleep(
        "'Welcome...", 2
        )
    print_sleep(
        "To...", 2
        )
    print_sleep(
        "The...", 2
        )
    print_sleep(
        "Hunt... \n", 2
        )
    print_sleep(
        "It's Not Over!... \n", 2
        )
    print_sleep(
        "To Be Continued!", 2
        )

    play_again()


def hypnotised():
    """
    Function is called no matter what path
    the player chooses. This is the function
    to take them to the end battle.
    """
    print_sleep(
        "This noise begins to take over your entire body,", 2
        )
    print_sleep(
        "causing you to loose all control.", 2
        )
    print_sleep(
        "Your feet start moving against your will and your", 2
        )
    print_sleep(
        "hands begin swaying in a military formation.", 2
        )
    print_sleep(
        "You seem to be walking so fast as you rush through", 2
        )
    print_sleep(
        "the forest.", 2
        )
    print_sleep(
        "In the far distance you begin to see some castle", 2
        )
    print_sleep(
        "walls stretch across the land. \n", 2
        )
    print_sleep(
        "The CITADEL!! \n", 2
        )
    print_sleep(
        "You have finally made it.", 2
        )
    print_sleep(
        "The darkness slowly started to lift as the sun rose", 2
        )
    print_sleep(
        "beyond the clouds.", 2
        )
    print_sleep(
        "As you near the castle walls you make a sudden stop.", 2
        )
    print_sleep(
        "Each second that goes by you get more control back", 2
        )
    print_sleep(
        "of your body, but you are still under this hypnosis.", 2
        )
    print_sleep(
        "Still frozen in place you watch as the castle gates", 2
        )
    print_sleep(
        "lower down to reveal The predator.", 2
        )


def the_predators_son():
    """
    This function is called if the player
    picks 'East'when asked which direction
    they want to go from function compass.
    """
    print_sleep(
        "You make your way towards the roar", 2
        )
    print_sleep(
        "The strength of knowing your Grandma ", 2
        )
    print_sleep(
        "has potentially gone through this has", 2
        )
    print_sleep(
        "made you willing to fight back.", 2
        )
    print_sleep(
        "With every step you took, the roars got", 2
        )
    print_sleep(
        "louder and the ground shaked more.", 2
        )
    print_sleep(
        "It was almost time. \n", 2
        )
    print_sleep(
        "Whipping noises rung through your ears", 2
        )
    print_sleep(
        "as the predator surrounds you.", 2
        )
    print_sleep(
        "He is constantly speeding up, which", 2
        )
    print_sleep(
        "is kicking up a lot of dirt and making it", 2
        )
    print_sleep(
        "harder to see. \n", 2
        )
    print_sleep(
        "Then he stops...", 2
        )
    print_sleep(
        "And pounces... \n", 2
        )
    print("What do you do? (cower/run)")

    answer = input("").lower().strip()

    while answer not in RUN and answer not in COWER:
        print_sleep(
            f"Invalid input name. Please try again {name}", 2
            )
        answer = input("").lower().strip()

    if answer in RUN:
        print_sleep(
            "You tried to outrun the pounce but", 2
            )
        print_sleep(
            "not with much luck. the predator clipped", 2
            )
        print_sleep(
            "your clothes as he landed, dragging you", 2
            )
        print_sleep(
            "to the floor. He then continues to drag", 2
            )
        print_sleep(
            "you around on the ground. You can't", 2
            )
        print_sleep(
            "escape.", 2
            )
        print_sleep(
            "after what feels like minutes of torture.", 2
            )
        print_sleep(
            "the predator stops playing with you", 2
            )
        print_sleep(
            "like a toy.", 2
            )
        print_sleep(
            "You lose 3 health.", 2
            )
        health_stats(-3)
        check_stats()
        print_sleep(
            "however the fight isn't over yet.", 2
            )
        print_sleep(
            "The predator takes a swipe with his", 2
            )
        print_sleep(
            "beast like claws. You are able to dodge.", 2
            )
        print_sleep(
            "This only angers him. He uses his tail", 2
            )
        print_sleep(
            "and grips you around the waist.", 2
            )
        print_sleep(
            "he lifts you in the air and raises you", 2
            )
        print_sleep(
            "just above his head, almost as if playing", 2
            )
        print_sleep(
            "with his food.", 2
            )
        print("What do you do? (1 Wriggle/ 2 Attack)")
        answer = input("").lower().strip()

        while answer not in WRIGGLE and answer not in ATTACK:
            print_sleep(
                f"Invalid input name. Please try again {name}", 2
                )
            answer = input("").lower().strip()
        if answer in WRIGGLE:
            print_sleep(
                "You try to wriggle yourself free but the grip", 2
                )
            print_sleep(
                "only gets tighter. You can feel the life being", 2
                )
            print_sleep(
                "squeezed out of you and in that moment you", 2
                )
            print_sleep(
                "believe this is the end.", 2
                )
            print_sleep(
                "You lose 1 health.", 2
                )
            health_stats(-1)
            check_stats()
            print_sleep(
                "As you are lowered into the beasts mouth,", 2
                )
            print_sleep(
                "you decide on a risky tactic. With all the force", 2
                )
            print_sleep(
                "you can manage you boot the beast square in the face.", 2
                )
            print_sleep(
                "The beast wimpers and immediately drops you", 2
                )
            print_sleep(
                "to the ground.", 2
                )
            print_sleep(
                "The predator bolts off, leaving you on the floor.", 2
                )
        elif answer in ATTACK:
            print_sleep(
                "With the hand that is free, you reach behind you", 2
                )
            print_sleep(
                f"and grab out your {item}. The predator hisses", 2
                )
            print_sleep(
                "as you raise the weapon and send it striking", 2
                )
            print_sleep(
                "on his tail.", 2
                )
            print_sleep(
                "A massive clink can be heard as it connects to", 2
                )
            print_sleep(
                "the tail. The tail is made out of some metal.", 2
                )
            print_sleep(
                "The predator still hisses out in pain and drops you.", 2
                )
            print_sleep(
                "The predator bolts off, leaving you on the floor.", 2
                )

    elif answer in COWER:
        print_sleep(
            "You crouch to your knees with your hands in the air,", 2
            )
        print_sleep(
            "clutching your weapon. A dark shadow glooms over you", 2
            )
        print_sleep(
            "quickly as you see the predator jump. At this moment", 2
            )
        print_sleep(
            "you strike your weapon up, just catching the predators", 2
            )
        print_sleep(
            "stomach. The predator reacted badly, first standing on", 2
            )
        print_sleep(
            "his back legs, screaming out in pain. He then whips", 2
            )
        print_sleep(
            "his tail at you which sends you flying into a nearby", 2
            )
        print_sleep(
            "tree. Winded, you want him scurry away with blurred", 2
            )
        print_sleep(
            "vision.", 2
            )
        print_sleep(
            "You lose 3 health.", 2
            )
        health_stats(-3)
        check_stats()

    print_sleep(
        "You stand up and dust yourself off. You notice an apple", 2
        )
    print_sleep(
        "on the floor. Starving, you eat the entire thing almost", 2
        )
    print_sleep(
        "instantly. Your health increase by 2 points. \n", 2
        )
    health_stats(2)
    check_stats()

    hypnotised()

    print_sleep(
        "However this doesn't look like the one you faced", 2
        )
    print_sleep(
        "earlier. It was thrice as big.", 2
        )
    print_sleep(
        "It had the head of a dog, and the tail like a", 2
        )
    print_sleep(
        "tiger. You thought the", 2
        )
    print_sleep(
        "one earlier was impossible to survive from but this ", 2
        )
    print_sleep(
        "one was actually going to be impossible.", 2
        )
    print_sleep(
        "And just when you thought it couldn't get worse,", 2
        )
    print_sleep(
        "The Beast opens his mouth and speaks... \n", 2
        )
    print_sleep(
        "'So I guess you've met one of my sons.'", 2
        )
    print_sleep(
        "His voice so deep that it shook the ground.", 2
        )
    print_sleep(
        "he stood fimrly, his stance intimdating you.", 2
        )
    print_sleep(
        "'I'll make you pay for what you did to him.", 2
        )
    print_sleep(
        "His brothers aren't very happy either.' \n", 2
        )
    print_sleep(
        "BROTHERS?! There's an entire family of them.", 2
        )
    print_sleep(
        "There is no escape from this... at all.", 2
        )

    finale_a()


play_game()
