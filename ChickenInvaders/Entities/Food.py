import pygame

from ChickenInvaders.Menu.Collide import collide


class Food:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.cool_down_counter = 0

    def draw(self,window):
        window.blit(self.image,(self.x,self.y))


    def move(self,vel):
        self.y += vel

    def off_screen(self,height):
        return not(self.y <= height and self.y >= 0)

    def collision(self,obj):
        return collide(self,obj)