import pygame
import ChickenInvaders.importitem as item
class Food(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = item.Food1
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self,Player_group):
        self.rect.y += 3
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self,Player_group,False):
            self.kill()