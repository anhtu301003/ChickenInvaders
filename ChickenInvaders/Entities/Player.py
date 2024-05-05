import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Character import Character


class Player(Character):
    def __init__(self,x,y,health = 100):
        super().__init__(x,y,health)
        self.character_img = item.HERO1
        self.weapon_img = item.WEAPON_NEUTRON
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health


