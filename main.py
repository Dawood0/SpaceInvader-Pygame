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

# setting the background
background=pygame.image.load("19333449.jpg")
background=pygame.transform.scale(background,(500,500))

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
enemyx=random.randint(0,450)
enemyy=random.randint(0,350)
enemyx_change=0.1
enemyy_change=0.1

# bullet
bullet=pygame.image.load("bullet.png")
bullet=pygame.transform.rotate(bullet,90)
bullet=pygame.transform.scale(bullet,(35,35))
bulletx=0
bullety=0
bulletx_change=0
bullety_change=0.5

def Player():
    screen.blit(player,(playerx+playerx_change,playery+playery_change))       # means to draw on the screen

def Enemy(x,y):
    screen.blit(enemy,(x,y))

def Bullet(x,y):
    screen.blit(bullet,(x,y))

kills=0

# while loop for continuous running game
game = True
while game:
    screen.fill((100, 200, 200))        # rgb values
    screen.blit(background,(0,0))      # setting the background

    # loop for closing the window when clicking the x red close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        # checking if a key is pressed
        if event.type == pygame.KEYDOWN:        # if key is pressed down
            if event.key == pygame.K_ESCAPE: pygame.quit()
            if event.key == pygame.K_LEFT:
                # print("left pressed")
                playerx_change -= 0.2
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.2
                # print("righht pressed")
            if event.key == pygame.K_UP:
                # print("up pressed")
                playery_change -= 0.2
            if event.key == pygame.K_DOWN:
                playery_change = 0.2
                # print("down pressed")




        if event.type == pygame.KEYUP:          # if key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0
            if event.key == pygame.K_SPACE:
                bulletx=playerx
                bullety=playery


    playerx += playerx_change
    playery += playery_change

    enemyx += enemyx_change
    # enemyy += enemyy_change

    bullety-=bullety_change

    # preventing the player from going out of bounds
    if playerx>screen.get_size()[0]-50 or playerx<0: playerx-=playerx_change
    if playery>screen.get_size()[1]-50 or playery<0: playery-=playery_change

    # preventing enemy from going out of bounds
    if enemyx>screen.get_size()[0]-50 or enemyx<0:
        enemyx_change=-1*enemyx_change
        enemyy+=10
    if enemyy>screen.get_size()[1]-50 or enemyy<0: enemyy_change=-1*enemyy_change


    # collision
    if abs(bulletx-enemyx)<20 and abs(bullety-enemyy)<20:
        enemyx=random.randint(0,450)
        enemyy=random.randint(0,350)
        kills+=1
        print(kills)



    Player()
    Enemy(enemyx,enemyy)
    Bullet(bulletx-5,bullety)
    Bullet(bulletx+20,bullety)
    pygame.display.update()
