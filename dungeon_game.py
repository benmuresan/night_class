"""
This program is a dungeon crawler type game.  The main character selects a weapon, a sidekick, and some armor, and then
goes on a quest to kill "Monsters".  Each room that is entered has a 50/50 chance of containing a monster.  Most of the
 possible options within the room are random.  Including whether or not the room is occupied by a monster, the monsters
 name, the weapon he is holding, his outfit, and his life points.

The duel phase, generates a hit points value for both the Player and the Monster randomly.  The Player and Monster fight
until one or the other dies.  If the Monster dies first the Player has the option of continuing into another room,
checking his status, looking around, or quiting the game altogether.
"""

__author__ = 'Ben Muresan'

import random
import os


class Player():
    """
    @name str: name of the player
    @weapon str: weapon for the player
    @pet str: player's pet
    @armor str: player's armor
    @life int: life points used to calculate if they player is alive or dead
    """
    def __init__(self, name, weapon, pet, armor):
        self.player_name = name
        self.player_weapon = weapon
        self.player_pet = pet
        self.player_armor = armor
        self.life = 100
        # TODO: maybe make the pet feature into something cool like another class instance with behaviors


class Monster():
    """
    @name str: name of the monster
    @life int: life points used to calculate if the monster is alive or dead
    @weapon str: weapon for the monster
    @armor str: monsters outfit
    """
    def __init__(self, name, life, weapon, wear):
        self.m_name = m_name()
        self.m_life = m_life()
        self.m_weapon = m_weapon()
        self.m_wear = m_wear()


def m_name():
    """
    selects a random name from local name_poss
    :return: string
    """
    name_poss = ["Dingle Doodle", "Fang", "Frank", "Demon", "Fast Devil"]
    name_choice = random.choice(name_poss)
    return name_choice


def m_weapon():
    """
    selects a random weapon from local weapon_possibility
    :return: string
    """
    weapon_possibility = ["Stick", "Sword", "Flower", "Broom", "Rag", "Legos", "Knife"]
    weapon_choice = random.choice(weapon_possibility)
    return weapon_choice


def m_wear():
    """
    selects a random outfit from local wear_possibility
    :return: string
    """
    wear_possibility = ["Suit", "Moo Moo", "Nothing!", "A Hat!"]
    wear_choice = random.choice(wear_possibility)
    return wear_choice


def m_life():
    """
    selects random life points for the Monster from local monster_life
    :return: int
    """
    monster_life = random.randint(10, 50)
    return monster_life


def strike():
    """
    selects random hit points for the Player from local name_poss
    :return: int
    """
    hit = random.randint(10, 20)
    return hit


def m_strike():
    """
    selects random hit points for the Monster from local hit
    :return: int
    """
    hit = random.randint(5, 10)
    return hit


def duel(player_attack, monster_attack, mnum_choice):
    x = player_attack
    y = monster_attack
    print("*" * 75)
    print("You will attack this vile creature!")
    print(" ")
    while True:
        print("You attack {} with your {}.  The damage is {}.".format(mnum_choice.m_name, player1.player_weapon, x))
        print(" ")
        mnum_choice.m_life = mnum_choice.m_life - x
        player1.life = player1.life - y
        if player1.life <= 0:
            clear()
            print("{} has ended your adventure early.  You died.".format(mnum_choice.m_name))
            print("*" * 30 + "GAME OVER" + "*" * 30)
            break
        if mnum_choice.m_life >= 1:
            print("{} is still alive! His life is at {}.".format(mnum_choice.m_name, mnum_choice.m_life))
            print("*" * 75)
            print(" ")
            print("{} attacks you with his {}.  Your life is now {}.".format(mnum_choice.m_name, mnum_choice.m_weapon,
                                                                             player1.life))
            fight_again = int(input("ENTER 1 to attack again.  ENTER 0 to run. "))
            if fight_again == 1:
                continue
            elif fight_again == 0:
                clear()
                print("You run away just in time!")
                break
        else:
            clear()
            print("*" * 75)
            print("{} has died! You are victorious.".format(mnum_choice.m_name))
            print("*" * 75)
            break


def status():
    print "*"*75
    print("{}'s status is: ".format(player1.player_name))
    print("Life = {}.".format(player1.life))
    print("Wielding a {}.".format(player1.player_weapon))
    print("Your sidekick is a {}.".format(player1.player_pet))
    print("You're wearing a {}.".format(player1.player_armor))
    print "*"*75
    print(" ")


def spawn():
    spawn_num = random.randint(1, 20)
    if spawn_num <= 10:
        return False
    else:
        return True


def play():
    spawn_alive = spawn()
    if spawn_alive is True:
        mnum_choice = Monster(m_name(), m_life, m_weapon(), m_wear())
        clear()
        print "*"*75
        print("You have entered a new room, it appears there is a MONSTER here.\n")
        print("You look at the monster, {}, and notice that:".format(mnum_choice.m_name))
        print(" ")
        print "*"*75
        print("His Life Points are = {}.".format(mnum_choice.m_life))
        print("He is Wielding a {}.".format(mnum_choice.m_weapon))
        print("He is wearing a {}.".format(mnum_choice.m_wear))
        print "*"*75
        print(" ")
        fight_choice = int(input("ENTER 1 to fight!  ENTER 0 to run. "))
        if fight_choice == 1:
            clear()
            duel(strike(), m_strike(), mnum_choice)
        elif fight_choice == 0:
            clear()
            print("*" * 75)
            print("You run away from {} in shame.".format(mnum_choice.m_name))
    elif spawn_alive is False:
        clear()
        print("*" * 75)
        print("You have entered a new room, it is empty.")


clear = lambda: os.system('clear')

clear()
print "*"*75
print("Welcome to Dungeon Crawler Premium!")
print " "

player_name = raw_input("What is your name hero? ")

clear()

print "*" * 75
print(" ")
print("{} , welcome, you stand in a dark room dimly lit by one lamp to the left.".format(player_name))
print("Before you is a:")
print(" ")
print("SWORD")
print("NUNCHUCKS")
print(" ")
player_weapon = raw_input("Which do you choose? ")

clear()

print("*" * 75)
print " "

print("Excellent choice {}, the {} suits you well.".format(player_name, player_weapon))
print "-" * 75
print " "
print("There is a slight whine to your right.")
print("Before you is a:")
print(" ")
print("MONKEY")
print("SKUNK")
print("TURTLE")
print(" ")

player_pet = raw_input("They want to travel with you, which would you like? ")

clear()

print("*" * 75)
print("The {} is an interesting choice for you.".format(player_pet))
print(" ")
print("The {} skampers onto your shoulder.".format(player_pet))
print(" ")
print "*"*75
print("You move forward and into the next room.")
print "*"*75
print " "
print("This room is dark and dank.  There is armor here!")
print(" ")
print("Before you is:")
print(" ")
print("HELMET")
print("TUBE SOCKS")
print(" ")

player_armor = raw_input("Which would you like? ")

clear()

print("*" * 75)
# print(" ")
print("You don the {} and admire yourself in the mirror on the wall.".format(player_armor))
# print " "

player1 = Player(player_name, player_weapon, player_pet, player_armor)

status()

try:
    direction_choice = raw_input("""1:  To move NORTH  3:  To move WEST
2:  To move SOUTH  4:  To move EAST
> """)

    if direction_choice in ("1", "2", "3", "4"):
        play()
    else:
        clear()
        print("I did not understand that entry.")
except:
    clear()
    print "I did not understand that entry."


"""
main loop -
exaplin the game logic...
"""


while True and player1.life >= 1:
    print(" ")
    print("Shall we move on?")
    print(" ")
    print("""1:  To move NORTH  3:  To move EAST
2:  To move SOUTH  4:  To move WEST""")
    print(" ")
    print("5:  To see your status.")
    print("6:  To look around.")
    print("7:  To quit.")
    direction = raw_input(">? ")
    if direction.isalpha():
        print("I did not understand that entry.")
    else:
        if direction in ("1", "2", "3", "4"):
            play()
        elif direction == "5":
            clear()
            status()
        elif direction == "6":
            clear()
            print "*"*75
            print("That option is not ready yet.")
            print(" ")
        elif direction == "7":
            clear()
            print("*" * 75)
            print(" ")
            print("Goodbye!")
            print("")
            break

# """if __name__= "__main__":
#     do stuff