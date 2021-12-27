# This is a sample Python script.

import pygame
import time
import random

# initializing game
pygame.init()

# making a screen
screen = pygame.display.set_mode((500, 500))

# setting name and icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# player
player=pygame.image.load('spaceship.png')
player=pygame.transform.scale(player,(50,50))
playerx=230
playery=450
playerx_change=0
playery_change=0

# enemies
enemy=pygame.image.load('enemy.png')
enemy=pygame.transform.scale(enemy,(50,50))






def Player():
    screen.blit(player,(playerx+playerx_change,playery+playery_change))       # means to draw on the screen



# while loop for continuous running game
game = True
while game:
    screen.fill((100, 200, 200))  # rgb values

    # loop for closing the window when clicking the x red close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        # checking if a key is pressed
        if event.type == pygame.KEYDOWN:        # if key is pressed down
            if event.key == pygame.K_ESCAPE: pygame.quit()
            if event.key == pygame.K_LEFT:
                print("left pressed")
                playerx_change -= 0.1
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.1
                print("righht pressed")
            if event.key == pygame.K_UP:
                print("up pressed")
                playery_change -= 0.1
            if event.key == pygame.K_DOWN:
                playery_change = 0.1
                print("down pressed")

        if event.type == pygame.KEYUP:          # if key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0

    playerx += playerx_change
    playery += playery_change
    if playerx>screen.get_size()[0]-50 or playerx<0: playerx-=playerx_change
    if playery>screen.get_size()[1]-50 or playery<0: playery-=playery_change


    Player()
    pygame.display.update()
