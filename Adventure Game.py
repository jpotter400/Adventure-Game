#!/usr/bin/env python
# coding: utf-8

# In[60]:


name = input("Type your name: ")
print("Welcome", name, "to this adventure! We need help rescuing a princess!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You approached a river! You can walk around it our swim across. Type 'walk to walk around or 'swim' to swim across ")
    
    if answer == "swim":
        print("You swam across and were eaten by an aligator!")
        
    elif answer == "walk":
        print("You walked for many miles and ... ran out of water and lost the game!")
        
    else: 
        print("Uh oh! Wrong answer, you lose.")
        
        
elif answer == 'right':    
    answer = input("You've walked up on a village! Do you go into town or go back (town/back)? ")
    if answer == "back":
        print("You went back but on your way you ran into a pack of wolves! Game over.")
    if answer == "town":
        answer = input("You were greated by the villagers.. BUT they need help with a task. Will you help? (yes/no)")
        if answer == "yes":
            answer = input("They need help slaying a dragon! Will you help? (yes/no)")
            if answer == "no":
                print("The village stoned you to death! Try again!")
            if answer == "yes":
                    print("You slayed the dragon! The village was maned after you and you were awarded a heafty amount of gold!")
        elif answer == "no":
            print("They slayed the princess themselves! Try again!")
        elif answer == "no":
                print("Oh no! The princess was slayin! Better luck next time.")

