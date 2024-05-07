import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Character import Character
import random

from ChickenInvaders.Entities.Food import Food


class Enemy(Character):
    def __init__(self, x, y, character_img,health):
        super().__init__(x, y, health)
        self.weapon_img = item.EnemyWeapon1
        self.character_img = character_img
        self.health = health
        self.mask = pygame.mask.from_surface(self.character_img)
        self.direction = 1 #hướng di chuyển 1 là phải -1 là trái
        self.weapons = []

    def move(self, vel):
        self.x += vel * self.direction
        if self.x + self.get_width() > item.WIDTH or self.x < 0:  # Kiểm tra nếu đến mép màn hình
            self.direction *= -1  # Đảo hướng di chuyển

    def die(self):
        # Hàm được gọi khi enemy bị bắn chết
        # Tạo một đối tượng Food tại vị trí của enemy
        food = Food(self.x, self.y, item.Food1)  # Đảm bảo item.Food1 là hình ảnh của đùi gà
        return food

