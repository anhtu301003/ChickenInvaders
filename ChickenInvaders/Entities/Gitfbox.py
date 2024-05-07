import pygame

from ChickenInvaders.Menu.Collide import collide


class Gift:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def off_screen(self, height):
        return not(self.y <= height and self.y >= -self.img.get_height())

    def collision(self, obj):
        return collide(obj, self)