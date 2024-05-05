import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Character import Character


class Enemy(Character):
    ENEMY_IMG = {
        "chicken1": item.Enemy1,
        "chicken2": item.Enemy2,
        "chicken3": item.Enemy3
    }

    def __init__(self, x, y, type_enemy, health=100):
        super().__init__(x, y, health)
        self.character_img = self.ENEMY_IMG[type_enemy]
        self.weapon_img = item.EnemyWeapon1
        self.mask = pygame.mask.from_surface(self.character_img)

    def move(self, vel):
        self.y += vel

