#! python3
"""
In this file I'm putting the helper functions that don't really
fit anywhere else

"""
import random

def roll(string):
    dice = string.split("d")

    if "+" in string: # If there are any modifiers, split them off
        dice.append(int(string.split("+")[1]))
    elif "-" in string[1]: # If there are any modifiers, split them off
        dice.append(-int(string.split("-")[1]))

    # now we should have a list of [num,type,mod]
    dice = [int(i) for i in dice]
    # now its full of integers
    total = 0
    for i in range(dice[0]):
        total += random.randint(1,dice[1])

    try: total += dice[2] # add the modifier
    except IndexError: pass # there might not always be a mod
    
    return total

class gender():
    """ A class that I can reference caller.db.gender.they to get
    the appropriate version of he/she"""
    def __init__(self,name,they,them,their):
        self.name = name
        self.they = they
        self.them = them
        self.thier = their
        
male = gender("male","he","him","his")
female = gender("female","she","her","hers")
other = gender("other","they","them","their")