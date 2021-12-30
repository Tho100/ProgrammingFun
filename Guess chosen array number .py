import numpy as np
import random

# * Define generator
def generator(n):
    a = np.random.randint(3, size=(3))
    f = np.random.choice(a)
    if(n == f):
        print("Correct!")
        return f
# * Define user
def user():
    p = int(input("> "))
    generator(p)

user()
