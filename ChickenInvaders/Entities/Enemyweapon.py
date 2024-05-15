import pygame
import ChickenInvaders.importitem as item

class Enemyweapon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = item.EnemyWeapon1
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self,Player_group):
        self.rect.y += 2
        if self.rect.top > item.HEIGHT:
            self.kill()
        if pygame.sprite.spritecollide(self,Player_group,False,pygame.sprite.collide_mask):
            for player in pygame.sprite.spritecollide(self,Player_group,False,pygame.sprite.collide_mask):
                player.hit(100)
            self.kill()
            # reduce spaceship health

