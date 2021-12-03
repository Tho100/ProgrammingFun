import pygame
from time import sleep
import numpy as np

pygame.init()

# Create a window

scn = pygame.display.set_mode((1200, 542))
pygame.display.set_caption("Main Window")

# Icon border

icon = pygame.image.load("C:\\Users\\HP\\Downloads\\Game\\arrows.png")
pygame.display.set_icon(icon)

# In-game image

upKey = pygame.image.load("C:\\Users\\HP\\Downloads\\Game\\UpKey.png")

pX = 370
pY = 10

def player(x,y):
    scn.blit(upKey, (x, y))
# TODO: Keep windows running
run = True
while run:
    # RGB (Background color)
    scn.fill((122,128,144))
    pX += 0.5
    # TODO: Manipulate key Position
    print(pX)
    if(pX == 471.5): # 1s = 1000mls | 0.5s = 500mls 
        sleep(1.5) # Delays break for 1.5 seconds (1500 miliseconds) 
        print("HOLY SHIT FINALLY")
        break
    elif(pX < 471.5):
        print("Not there yet")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player(pX,pY)
    pygame.display.update()