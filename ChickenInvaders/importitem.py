import pygame
import time
import random

#Chiều dài, chiều rộng màn hình
WIDTH, HEIGHT = 1000, 800

#font chữ
def FontGame(Size):
    return pygame.font.Font('Resource/Items/Jersey25-Regular.ttf', Size)

#Backgrounds
BG = pygame.image.load("Resource/Background/Background.png")
TITLE_GAME = pygame.image.load("Resource/Items/Titlegame.png")


#Heros
HERO = pygame.image.load("Resource/Hero/Hero.png")

#Weapons
WEAPON_NEUTRON = pygame.image.load("Resource/Weapons/Neutronguns/neutron1.png")