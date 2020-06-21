import time
import random


def print_pause(msg_to_print, seconds):
    print(msg_to_print)
    time.sleep(seconds)


def intro(item, option):
    print_pause("You wake up, stranded on a tropical beach. ", 2)
    print_pause("In front of you the vast blue Ocean.", 1)
    print_pause("Behind you the jungle.", 1)
    print_pause("To your right, not too far away on the beach,\n"
                "a dock, with no boats.", 2)
    print_pause("You look up towards the horizon,\n"
                "and in the distance, \n"
                "you see that a ship with a black flag"
                " is approaching..", 2)
    print_pause("Oh, you remember now.. Pirates!", 2)
    print_pause("They are chasing you beacause you own a very "
                "precious object, \n"
                "that they could sell for a fortune!", 2)
    print_pause("The object is the very old " + option + ",\n"
                "that you have inherited from your family ancestors.", 2)
    print_pause("They have been chasing you for days trough the Ocean,\n"
                "until last night, \n"
                "they lost track of your boat because of a heavy storm \n"
                "that also crashed your small boat,\n"
                "leaving you at the mercy of the waves....", 3)
    print_pause("This is all you remember..", 1)
    print_pause("While shaking off the sand from your eyes,\n"
                "you realise that the Pirate ship \n"
                "is coming closer and closer..\n", 2)


def beach(item, option):
    print_pause("Enter 1 to go to the 'dock'.\n"
                "Enter 2 to go to the 'jungle'.\n", 1)
    print_pause("What would you like to do?", 1)
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            dock(item, option)
            break
        elif choice1 == "2":
            jungle(item, option)
            break


def tall_tree():
    stay_climb = input("Press (1) to hide on top of tall tree.\n"
                       "Press (2) to sit down on a rock and rest.\n")
    if stay_climb == "1":
        print_pause("You climb on the tree.", 1)
        print_pause("While hiding, you start thinking"
                    " about a way to escape the island,\n"
                    "and suddenly you have an idea:\n", 2)
        print_pause("You realise that, if 'ALL' of them "
                    "are looking for you in the jungle..", 1)
        print_pause("There is a high chance that the dock,\n"
                    "is not going to be crowded with pirates..", 1)
        print_pause("That can be your chance to approach their ship,"
                    "and figure out a way to escape!...\n", 2)
        print_pause("But first..you have to buy some time and hide,\n"
                    "at least until they go deeper into the jungle,\n"
                    "and it's safe for you to climb down ..\n", 2)
        print_pause("As You hide and hide.. trying not to make any noise, \n"
                    "you see a Pirate, walking towards your position. ", 2)
        print_pause("With surprise you notice that \n"
                    "he just wants to sit down on a rock, "
                    "right under your tree.\n"
                    "He drinks some water,\n"
                    "takes off his Pirate Jacket and Pirate Hat,"
                    " and then leaves in a hurry again,\n"
                    "forgetting his jacket and hat on the ground.", 2)
        print_pause("Mmmh.. very interesting!\n", 1)
        print_pause("It looks like it's safe for you to climb down now.", 1)
        print_pause("You take a look at the rock where he was sitting,\n"
                    "and intuitively, you decide to \n"
                    "wear the 'fancy pirate leather Jacket'"
                    "and the 'fancy pirate Hat',\n"
                    "in order to disguise yourself as one of them.", 1)
        print_pause("You look exactly like a pirate now!", 1)
        print_pause("You head back to the beach.\n", 2)

    elif stay_climb == "2":
        print_pause("The pirates see you sitting there "
                    "and capture you.", 1)
        lose_game()

    else:
        tall_tree()


def jungle(item, option):
    if "pirate_disguise" in item:
        print_pause("You go back to the jungle.", 1)
        print_pause("There is nothing more for you to do here..\n"
                    "You should try to find a way out"
                    " to escape the island now!", 1)
        print_pause("You go back to the beach.", 1)

    else:
        print_pause("You go to the jungle.", 1)
        print_pause("As you run trough the deep "
                    "and dense jungle, ", 1)
        print_pause("all of a sudden you hear "
                    "a noise and you stop moving..", 1)
        print_pause("it's those pirates again!"
                    " They must know that you are here..", 1)
        print_pause("In front of you, you see a"
                    " tall but climbable tree.", 1)
        print_pause("What do you want to do?", 1)
        tall_tree()
        item.append("pirate_disguise")
    beach(item, option)


def escape_island(option):
    drop_boat = input("Press (B) to Approach emergency boat "
                      "on board of the ship, and escape!").lower()
    while True:
        if drop_boat == "B".lower():
            print_pause("You enter the boat.", 1)
            print_pause("With pride you look at your "
                        "shiny " + option + " and finally..!", 1)
            print_pause("Sail away!!", 1)
            print_pause("Congratulations, you managed to escape the island!\n"
                        "You are victorious!", 1)
            play_again()
            break
        else:
            escape_island(option)


def ship(item, option):
    print_pause("You step on board of the ship.", 1)
    escape_island(option)


def alerted_pirate():
    print_pause("As you slowly walk pass the drunken pirate..\n"
                "You have almost almost arrived in front of the ship,\n"
                "when he suddenly wakes up, and shouts to you:\n", 1)
    print_pause("'Yoohhohhooh pirate!'", 1)
    print_pause("'Oh wait, you are not one of ours!!'\n"
                "'Stay where you are or I'll shoot!'\n", 1)


def dock(item, option):
    print_pause("As you slowly walk towards the dock, you notice that\n"
                "there is only one pirate, who is guarding the ship,\n"
                "holding a gun in one hand "
                "and a rum bottle in the other..\n", 2)

    if "pirate_disguise" not in item:
        print_pause("It's too risky to try to walk pass that pirate now..\n"
                    "The other pirates will be here very soon..\n"
                    "You are unarmed, and too weak after last night..\n"
                    "there must be an other way to get to the ship, "
                    "without him noticing you.\n", 2)
    while True:
        choice2 = input("Would you like to (1) go to ship or"
                        " (2) go to the jungle?\n")
        if choice2 == "1":
            if "pirate_disguise" in item:
                print_pause("As you slowly walk pass the drunken pirate..\n"
                            "You almost arrive in front of the ship,\n"
                            "when he suddenly wakes up, "
                            "and shouts to you:\n", 1)
                print_pause("'Yoohhohhooh! Stop right there pirate!'", 2)
                print_pause("'Oh it's you, Jack'! "
                            "You scared me there for a moment!'", 1)
                print_pause("..and right away "
                            "he falls back to sleep again..", 1)
                print_pause("Luckely he didn't recognise you..\n", 1)
                print_pause("Very good, you managed to reach the ship "
                            "without being noticed!", 2)
                ship(item, option)

            else:
                alerted_pirate()
                lose_game()

        if choice2 == "2":
            jungle(item, option)
            break


def lose_game():
    print_pause("The pirates have captured you.\n"
                "Sorry, you lost.", 1)
    play_again()


def play_again():
    again = input("Would you like to play again? (y/n)\n").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ...", 2)
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time, adventurer.", 1)
        exit()
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Gold Sapphire Ring of the Ancients",
                            "Silver Amulet of Wisdom", "Red Dragon's Tooth"])
    intro(item, option)
    beach(item, option)


play_game()
