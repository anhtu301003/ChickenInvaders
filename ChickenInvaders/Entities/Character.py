import pygame

from ChickenInvaders.Entities.Weapon import Weapon
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
        self.cool_down_counter = 0
    def draw(self,window):
        window.blit(self.character_img,(self.x,self.y))
        for weapon in self.weapons:
            weapon.draw(window)

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
                obj.health -=10
                self.weapons.remove(weapon)


    def shoot(self):
        if self.cool_down_counter == 0:
            weapon = Weapon(self.x + self.character_img.get_width()/2 - 12.5,self.y,self.weapon_img)
            self.weapons.append(weapon)
            self.cool_down_counter = 1

    #lấy chiều rộng
    def get_width(self):
        return self.character_img.get_width()

    # lấy chiều dài
    def get_height(self):
        return self.character_img.get_height()
