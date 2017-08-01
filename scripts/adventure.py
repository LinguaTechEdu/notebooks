# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def dice(*sides):
    return "Dice roll!"


def play():
    GAME_ON = True
    
    while GAME_ON:
        player = input("Name: ")
        print("{} approaches the doorway as the hallway forks in two different directions. Which way?".format(player))
        goto = input("(r)ight or (l)eft? ")
        print("You turn {}. There's nothing but darkness ahead".format(goto))
        
        goto = input("(b)ack or (c)ontinue? ")
        print("You carryon through the darkness ...before a pair of glowing yellow eyes peers from beyond. A breath catches in your throat"
              " before you spot a small doorway to your right.")
        
        goto = input("(f)oward or (r)ight?")
        print("You go through the small doorway and enter a room witha faint glow and a club resting against the wall.")
        
        goto = input("(t)ake the club")
        print("As soon as your hand grabs the handle of your new weapon, the glowing eyes enters the room and slowly haunts towards you ...")
        
        goto = input("(a)ttack or (d)efend?")
        print("You swing the club at the eyes and it lands with a thud on the creatures head, but he doesn't go down just yet.")
        
        goto = input("(a)ttack or (d)efend?")
        print("It claws at you with slow moving arms and misses.")
        
        goto = input("(a)ttack or (d)efend?")
        print("With one final swing the creature goes down, eyes glowing no more... and suddenly a bright blue portal opens up before you.")
        print("You walk through it and find yourself safely back in town with a sack of loot in your hands.")
        
        GAME_ON = False

play()        
