import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Character import Character


class Player(Character):
    def __init__(self,x,y,health = 100):
        super().__init__(x,y,health)
        self.character_img = item.HERO1
        self.weapon_img = item.WEAPON_NEUTRON
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health
    def move_weapons(self,vel,objs):
        self.cooldown()
        for weapon in self.weapons:
            weapon.move(vel)
            if weapon.off_screen(item.HEIGHT):
                self.weapons.remove(weapon)
            else:
                for obj in objs:
                    if weapon.collision(obj):
                        objs.remove(obj)
                        self.weapons.remove(weapon)


