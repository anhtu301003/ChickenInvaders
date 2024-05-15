import pygame

import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Explosion import Explosion
from ChickenInvaders.Entities.Food import Food
from ChickenInvaders.Entities.Gitfbox import Gift
import ChickenInvaders.Resource.Music.importmusic as itemMusic

class Weapon(pygame.sprite.Sprite):
    def __init__(self,x,y,weapon_level):
        pygame.sprite.Sprite.__init__(self)
        self.weapon_level = weapon_level
        self.images = [item.WEAPON_NEUTRON1,item.WEAPON_NEUTRON2,item.WEAPON_NEUTRON3]
        self.image = self.images[self.weapon_level-1]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [x,y]

    def update(self, Enemy_group, Food_group, Explosion_group, Gift_group):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()
        hit_enemies = pygame.sprite.spritecollide(self, Enemy_group, False)
        for enemy in hit_enemies:
            enemy.hit(100)  # Gọi phương thức hit với damage là 100
            if enemy.health <= 0:  # Nếu enemy đã chết
                self.kill()
                explosion = Explosion(self.rect.centerx, self.rect.y, 5)
                Explosion_group.add(explosion)
                food = Food(self.rect.centerx, self.rect.top)
                Food_group.add(food)
            else:
                self.kill()  # Loại bỏ viên đạn sau khi nó đã va chạm


