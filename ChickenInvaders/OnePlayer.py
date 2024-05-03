import pygame,sys
from ButtonMenu import Button
import mainscreen

background = pygame.image.load("./Resource/Background/background.png")
background = pygame.transform.scale(background, (800, 600))


playerImg = pygame.image.load("./Resource/Hero/hero.png")
playerImg = pygame.transform.scale(playerImg, (110, 200))
playerX = 100
playerY = 100
running = True
playerX_change = 0
playerY_change = 0
def player(x,y):
    mainscreen.SCREEN.blit(playerImg, (x, y))
def oneplayer():
    global running
    running = running
    global playerX, playerY
    playerX = playerX
    playerY = playerY
    global playerX_change, playerY_change
    while running:
        mainscreen.SCREEN.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerX_change = -1
                if event.key == pygame.K_d:
                    playerX_change = 1
                if event.key == pygame.K_w:
                    playerY_change = -1
                if event.key == pygame.K_s:
                    playerY_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                    playerX_change = 0
                    playerY_change = 0

        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        pygame.display.update()
