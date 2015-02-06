__author__ = 'Beni'

import random
import os

class Player():
    def __init__(self, name, weapon, pet, armor):
        self.player_name = name
        self.player_weapon = weapon
        self.player_pet = pet
        self.player_armor = armor
        self.life = 100


class Monster():
    def __init__(self, name, life, weapon, wear):
        self.m_name = m_name()
        self.m_life = m_life()
        self.m_weapon = m_weapon()
        self.m_wear = m_wear()


def m_name():
    name_poss = ["Dingle Doodle", "Fang", "Frank", "Demon", "Fast Devil"]
    name_choice = random.choice(name_poss)
    return name_choice


def m_weapon():
    weapon_possibility = ["Stick", "Sword", "Flower", "Broom"]
    weapon_choice = random.choice(weapon_possibility)
    return weapon_choice


def m_wear():
    wear_possibility = ["Suit", "Moo Moo", "Nothing!", "A Hat!"]
    wear_choice = random.choice(wear_possibility)
    return wear_choice


def m_choice():
    monster_var = ["m1", "m2", "m3", "m4", "m5", "m6", "m7"]
    monster_choice = random.choice(monster_var)
    return monster_choice


def m_life():
    monster_life = random.randint(10, 50)
    return monster_life


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
    if spawn_alive == True:
        mnum_choice = m_choice()
        mnum_choice = Monster(m_name(), m_life, m_weapon(), m_wear())
        clear()
        print "*"*75
        print("You have entered a new room, it appears there is a MONSTER here.")
        print(" ")
        print("You look at the monster and notice that:")
        print(" ")
        print "*"*75
        print("{}'s status is: ".format(mnum_choice.m_name))
        print("Life = {}.".format(mnum_choice.m_life))
        print("Wielding a {}.".format(mnum_choice.m_weapon))
        print("He's wearing a {}.".format(mnum_choice.m_wear))
        print "*"*75
        print(" ")
    else:
        clear()
        print(" ")
        print("You have entered a new room, it is empty.")


clear = lambda: os.system('clear')

clear()
print "*"*75
print("Welcome to Dungeon Crawler Premium!")
print " "

player_name = raw_input("What is your name hero? ")

clear()

print " "
print("{} , welcome, you stand in a dark room dimly lit by one lamp to the left.".format(player_name))
print("Before you is a:")
print(" ")
print("SWORD")
print("NUNCHUCKS")
print(" ")
player_weapon = raw_input("Which do you choose? ")

clear()

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
print(" ")
print("You don the {} and admire yourself in the mirror on the wall.".format(player_armor))
print " "

player1 = Player(player_name, player_weapon, player_pet, player_armor)

status()

while True:
    print("Shall we move on?")
    print("1:  To move forward.")
    print("2:  To look at yourself.")
    print("3:  To look around.")
    print("4:  To quit.")
    direction = raw_input(">? ")
    if direction == "1":
        play()
    elif direction == "2":
        clear()
        status()
    elif direction == "3":
        clear()
        print "*"*75
        print("That option is not ready yet.")
        print(" ")
    elif direction == "4":
        break
    else:
        clear()
        print"*"*75
        print("I did not understand your entry!")