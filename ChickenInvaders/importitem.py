import os

import pygame
from pygame import mixer
import time
import random


#Chiều dài, chiều rộng màn hình
WIDTH, HEIGHT = 1000, 800

#Chiều dài, chiều rộng enemy
WIDTH_ENEMY,HEIGHT_ENEMY = 100,80

#Chiều dài, chiều rộng enemy
WIDTH_BOSS,HEIGHT_BOSS = 400,300

#Chiều dài,chiều rộng hero
WIDTH_HERO,HEIGHT_HERO = 120,100

#lấy đường đẫn
current_dir = os.path.dirname(os.path.abspath(__file__))

#font chữ
pygame.font.init()
fontpath = os.path.join(current_dir, 'Resource/Items/Jersey25-Regular.ttf')
def FontGame(Size):
    return pygame.font.Font(fontpath, Size)

#Backgrounds
BG = pygame.image.load(os.path.join(current_dir, 'Resource/Background/Background.png'))
TITLE_GAME = pygame.image.load(os.path.join(current_dir, "Resource/Items/Titlegame.png"))


#Heros
HERO1 = pygame.image.load(os.path.join(current_dir,"Resource/Hero/Hero.png"))
HERO1 = pygame.transform.scale(HERO1,(WIDTH_HERO,HEIGHT_HERO))
HERO2 = pygame.image.load(os.path.join(current_dir,"Resource/Hero/Hero.png"))

#Weapons
WEAPON_NEUTRON1 = pygame.image.load(os.path.join(current_dir,"Resource/Weapons/Neutronguns/neutron1.png"))
WEAPON_NEUTRON2 = pygame.image.load(os.path.join(current_dir,"Resource/Weapons/Neutronguns/neutron2.png"))
WEAPON_NEUTRON3 = pygame.image.load(os.path.join(current_dir,"Resource/Weapons/Neutronguns/neutron3.png"))


#Enemies
Enemy1 = pygame.image.load(os.path.join(current_dir,"Resource/Enemies/chicken1.png"))
Enemy1 = pygame.transform.scale(Enemy1,(WIDTH_ENEMY,HEIGHT_ENEMY))

Enemy2 = pygame.image.load(os.path.join(current_dir,"Resource/Enemies/chicken2.png"))
Enemy2 = pygame.transform.scale(Enemy2,(WIDTH_ENEMY,HEIGHT_ENEMY))

Enemy3 = pygame.image.load(os.path.join(current_dir,"Resource/Enemies/chicken3.png"))
Enemy3 = pygame.transform.scale(Enemy3,(WIDTH_ENEMY,HEIGHT_ENEMY))

Boss = pygame.image.load(os.path.join(current_dir,"Resource/Enemies/bosschicken.png"))
Boss = pygame.transform.scale(Boss,(WIDTH_BOSS,HEIGHT_BOSS))

#Enemies Weapons
EnemyWeapon1 = pygame.image.load(os.path.join(current_dir,"Resource/Enemies/chicken_weapon1.png"))
EnemyWeapon1 = pygame.transform.scale(EnemyWeapon1,(20,30))

#Foods
Food1 = pygame.image.load(os.path.join(current_dir,"Resource/Foods/Food.png"))
Food2 = pygame.image.load(os.path.join(current_dir,"Resource/Foods/Food2.png"))


#Gifts
Gift = pygame.image.load(os.path.join(current_dir,"Resource/Weapons/Neutronguns/neutrongift.png"))

#Next
NextLeft= pygame.image.load(os.path.join(current_dir,"Resource/Items/nextleft.png"))
NextRight= pygame.image.load(os.path.join(current_dir,"Resource/Items/nextright.png"))

#easy
easy = []
medium = []
hard = []

easymode= pygame.image.load(os.path.join(current_dir,"Resource/Items/easy.png"))
mediummode= pygame.image.load(os.path.join(current_dir,"Resource/Items/medium.png"))
hardmode= pygame.image.load(os.path.join(current_dir,"Resource/Items/hard.png"))
easymode = pygame.transform.scale(easymode,(100,50))
mediummode = pygame.transform.scale(mediummode,(100,50))
hardmode = pygame.transform.scale(hardmode,(100,50))
