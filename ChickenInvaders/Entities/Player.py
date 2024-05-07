import pygame
import ChickenInvaders.importitem as item
from ChickenInvaders.Entities.Character import Character
from ChickenInvaders.Entities.Food import Food
from ChickenInvaders.Entities.Weapon import Weapon


class Player(Character):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.character_img = item.HERO1
        self.weapon_img = item.WEAPON_NEUTRON
        self.mask = pygame.mask.from_surface(self.character_img)
        self.max_health = health

    def move_weapons(self, vel, objs):
        self.cooldown()
        for weapon in self.weapons:
            weapon.move(vel)
            if weapon.off_screen(item.HEIGHT):
                self.weapons.remove(weapon)
            else:
                for obj in objs:
                    if weapon.collision(obj):
                        obj.health -= 100
                        self.weapons.remove(weapon)
                        if obj.health <= 0:
                            objs.remove(obj)
                            food = Food(obj.x, obj.y, item.Food1)
                            self.foods.append(food)  # Thêm thức ăn vào danh sách thức ăn của người chơi

        # Thêm vòng lặp này để di chuyển các mục thức ăn trên màn hình
        for food in self.foods:
            food.move(4)
            if food.off_screen(item.HEIGHT):
                self.foods.remove(food)


    def move_food(self, vel, objs):
        self.cooldown()
        for food in self.foods:
            food.move(vel)
            if food.off_screen(item.HEIGHT):
                self.foods.remove(food)
            elif food.collision(self):  # Kiểm tra va chạm giữa thức ăn và người chơi
                self.foods.remove(food)  # Nếu có va chạm, xóa thức ăn
    def shoot(self):
        if self.cool_down_counter == 0:
            weapon = Weapon(self.x + self.character_img.get_width()/2 - 12.5,self.y,self.weapon_img)
            self.weapons.append(weapon)
            self.cool_down_counter = 1

