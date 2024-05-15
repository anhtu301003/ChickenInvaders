import pygame
import ChickenInvaders.importitem as item
import random

from ChickenInvaders.Entities.Weapon import Weapon
import ChickenInvaders.Resource.Music.importmusic as itemMusic

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y,health):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice([item.Enemy1,item.Enemy2,item.Enemy3])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [x, y]
        self.move_counter = 0
        self.health = health
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.rect.right > item.WIDTH or self.rect.left < 0:
            self.move_direction *= -1
            self.rect.y += self.rect.height
        if self.health <= 0:
            self.kill()

    def set_image(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def hit(self, damage):  # Thêm phương thức hit
        self.health -= damage
        pygame.mixer.music.load(itemMusic.musicchicken)
        pygame.mixer.music.play()
        if self.health <= 0:
            self.kill()
