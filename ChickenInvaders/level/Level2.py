import pygame
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
from ChickenInvaders.Menu.Collide import collide
import random


#
ENEMY_COOLDOWN = 500

# Khai báo biến toàn cục
running = True
lives = 1
enemies = []

# Thiết lập caption cho cửa sổ
pygame.display.set_caption("Option oneplayer")

# Các hằng số
FPS = 60
player_vel = 5
hero_weapon_vel = 17
enemy_weapon_vel = 4
enemy_vel = 1
rows = 1
columns = 7
last_enemy_shot = pygame.time.get_ticks()
clock = pygame.time.Clock()

# Khởi tạo người chơi
player = Pl.Player(300, 650,100)

# Hàm vẽ lại cửa sổ
def redraw_windowoneplayer():
    mainscreen.SCREEN.blit(item.BG, (0, 0))
    for en in enemies:
        en.draw(mainscreen.SCREEN)
    player.draw(mainscreen.SCREEN)
    pygame.display.update()

# Tạo danh sách enemy
def create_enemies():
    for row in range(rows):
        for col in range(columns):
            enemy = En.Enemy(100 + col * 130,100 + row * 70,random.choice([item.Enemy1,item.Enemy2,item.Enemy3]),100)
            enemies.append(enemy)

# Hàm Level2
def Level2():
    global running, lives, enemies, last_enemy_shot
    create_enemies()
    while running:
        clock.tick(FPS)
        time_now = pygame.time.get_ticks()
        if lives <= 0:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < item.WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < item.HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        for en in enemies:
            en.move(enemy_vel)
            en.move_weapons(enemy_weapon_vel, player)
            if(player.health == 0):
                lives -= 1  # nếu player hết máu thì thua
            if collide(en, player): # nếu player va chạm với enemy thì hết máu luôn
                lives -= 1
                enemies.remove(en)
        #random bắn của enemy
        if enemies:
            if time_now - last_enemy_shot > ENEMY_COOLDOWN:
                random.choice(enemies).shoot()
                last_enemy_shot = time_now
        else:
            break
        for en in enemies:
            if en.x + en.get_width() >= item.WIDTH or en.x <= 0:
                for en in enemies:
                    en.direction *= -1  # Đảo hướng di chuyển của enemy
                break
        player.move_weapons(-hero_weapon_vel, enemies)
        redraw_windowoneplayer()

# Hàm trả về số mạng
def get_lives():
    return lives
