import pygame
import time
import random

#Chiều dài, chiều rộng màn hình
WIDTH, HEIGHT = 1000, 800
#Chiều dài, chiều rộng enemy
WIDTH_ENEMY,HEIGHT_ENEMY = 100,80
#Chiều dài,chiều rộng hero
WIDTH_HERO,HEIGHT_HERO = 120,100
#font chữ
def FontGame(Size):
    return pygame.font.Font('Resource/Items/Jersey25-Regular.ttf', Size)

#Backgrounds
BG = pygame.image.load("Resource/Background/Background.png")
TITLE_GAME = pygame.image.load("Resource/Items/Titlegame.png")


#Heros
HERO1 = pygame.image.load("Resource/Hero/Hero.png")
HERO1 = pygame.transform.scale(HERO1,(WIDTH_HERO,HEIGHT_HERO))
HERO2 = pygame.image.load("Resource/Hero/Hero.png")

#Weapons
WEAPON_NEUTRON = pygame.image.load("Resource/Weapons/Railguns/railgun1.png")
WEAPON_NEUTRON = pygame.image.load("Resource/Weapons/Neutronguns/neutron1.png")


#Enemies
Enemy1 = pygame.image.load("Resource/Enemies/chicken1.png")
Enemy1 = pygame.transform.scale(Enemy1,(WIDTH_ENEMY,HEIGHT_ENEMY))

Enemy2 = pygame.image.load("Resource/Enemies/chicken2.png")
Enemy2 = pygame.transform.scale(Enemy2,(WIDTH_ENEMY,HEIGHT_ENEMY))

Enemy3 = pygame.image.load("Resource/Enemies/chicken3.png")
Enemy3 = pygame.transform.scale(Enemy3,(WIDTH_ENEMY,HEIGHT_ENEMY))

#Enemies Weapons
EnemyWeapon1 = pygame.image.load("Resource/Enemies/chicken_weapon1.png")
EnemyWeapon1 = pygame.transform.scale(EnemyWeapon1,(20,30))