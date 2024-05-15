import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Weapon import Weapon
import ChickenInvaders.Resource.Music.importmusic as itemMusic
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,health):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.image = item.HERO1
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.score = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.last_shot = pygame.time.get_ticks()
        self.weapon_level = 1

    def update(self,Player_Weapon_group,Gift_group,Enemy_group,Enemy_weapon_group,Food_group):
        speed = 8
        cooldown = 500

        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.left >0:
            self.rect.x -= speed
        if key[pygame.K_d] and self.rect.right < item.WIDTH:
            self.rect.x += speed
        if key[pygame.K_w] and self.rect.top >0:
            self.rect.y -= speed
        if key[pygame.K_s] and self.rect.bottom < item.HEIGHT:
            self.rect.y += speed

        time_now = pygame.time.get_ticks()

        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            weapon = Weapon(self.rect.centerx, self.rect.top, self.weapon_level)
            Player_Weapon_group.add(weapon)
            self.last_shot = time_now

        if pygame.sprite.spritecollide(self,Gift_group,True):
            self.weapon_level += 1

        if pygame.sprite.spritecollide(self,Food_group,True):
            self.score += 1


        if pygame.sprite.spritecollide(self,Enemy_group,True):
            self.health -= 100
            self.kill()


    def hit(self, damage):  # Thêm phương thức hit
        self.health -= damage
        if self.health <= 0:
            self.kill()

    def get_attribute(self):
        return {
            'score': self.score,
            'x': self.rect.centerx,
            'y': self.rect.centery,
            'health': self.health,
            'weapon_level': self.weapon_level
        }