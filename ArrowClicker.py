import pygame
from time import sleep
import numpy as np
from pygame.constants import K_DOWN, K_RIGHT, KEYDOWN

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # TODO: Manipulate png position using arrow keys

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX -= 12
            if event.key == pygame.K_RIGHT:
                pX += 12
            # TODO: Quit key
            if event.key == pygame.K_ESCAPE:
                quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pass
            
    player(pX,pY)
    pygame.display.update()
