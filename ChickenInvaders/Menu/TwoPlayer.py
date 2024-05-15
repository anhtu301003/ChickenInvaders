import pygame
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
import random
import ChickenInvaders.level.Level1 as Lv1
def twoplayer(type=2):
    Lv1.Level1(type)