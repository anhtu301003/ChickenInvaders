import pygame
import ChickenInvaders.importitem as item
import random

from ChickenInvaders.Entities.Weapon import Weapon


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice([item.Enemy1,item.Enemy2,item.Enemy3])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.rect.right > item.WIDTH or self.rect.left < 0:
            self.move_direction *= -1
            self.rect.y += self.rect.height
