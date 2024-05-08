import pygame

from ChickenInvaders.Entities.Food import Food
from ChickenInvaders.Entities.Weapon import Weapon
from ChickenInvaders.Entities.Gitfbox import Gift
import ChickenInvaders.importitem as item

class Character():
    COOLDOWN = 30

    def __init__(self,x,y,health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.weapon_img = None
        self.weapons = []
        self.foods = []
        self.gifts = []
        self.cool_down_counter = 0

    def draw(self,window):
        window.blit(self.character_img,(self.x,self.y))
        for weapon in self.weapons:
            weapon.draw(window)
        for food in self.foods:
            food.draw(window)


    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def move_weapons(self,vel,obj):
        self.cooldown()
        for weapon in self.weapons:
            weapon.move(vel)
            if weapon.off_screen(item.HEIGHT):
                self.weapons.remove(weapon)
            elif weapon.collision(obj):
                obj.health -= 100
                self.weapons.remove(weapon)

    def move_food(self,vel,obj):
        self.cooldown()
        for food in self.foods:
            food.move(vel)
            if food.off_screen(item.HEIGHT):
                self.foods.remove(food)
            elif food.collision(obj):
                obj.health -= 100
                self.foods.remove(food)


    def shoot(self):
        if self.cool_down_counter == 0:
            weapon = Weapon(self.x + self.character_img.get_width()/2 - 12.5,self.y + self.character_img.get_height(),self.weapon_img)
            self.weapons.append(weapon)
            self.cool_down_counter = 1

    def food_shoot(self):
        if self.cool_down_counter == 0:
            food = Food(self.x + self.character_img.get_width()/2 - 12.5,self.y + self.character_img.get_height(),item.Food1)
            self.foods.append(Food)
            self.cool_down_counter = 1


    #lấy chiều rộng
    def get_width(self):
        return self.character_img.get_width()

    # lấy chiều dài
    def get_height(self):
        return self.character_img.get_height()



