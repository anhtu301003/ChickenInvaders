import pygame

class Character():
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
    #lấy chiều rộng
    def get_width(self):
        return self.character_img.get_width()

    # lấy chiều dài
    def get_height(self):
        return self.character_img.get_height()
