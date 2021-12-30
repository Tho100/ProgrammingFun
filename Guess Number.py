import numpy as np
import random

# Define number generator

def num_generator(n):
    a = random.randint(1,6)
    if(n == a):
        print('fuck you')

# Define player function    

def player_func():
    t = 5
    while t > 0:
        t -= 1
        ply = int(input("> "))
        num_generator(ply)
        # * End the game if the user reached 5 inputs 
        if(t == 0):
            print("Game Ended")
            
# * Call game func
player_func()
