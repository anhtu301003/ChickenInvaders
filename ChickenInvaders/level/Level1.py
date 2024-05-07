import time

import pygame,sys,os
from pygame import font
from pygame import mixer

import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
from ChickenInvaders.Entities.Food import Food
from ChickenInvaders.Menu.Collide import collide
import random

from ChickenInvaders.level.Level2 import Level2
from ChickenInvaders.level.ScreenGameOver import drawGameOver
from ChickenInvaders.level.ScreenWinner import drawWinner

#
ENEMY_COOLDOWN = 1000


# Khai báo biến toàn cục
running = True
lives = 1
lives1 = 1
lives2 = 1
enemies = []
foods =[]
gifts =[]
global_score = 0
global_score1 = 0
global_score2 = 0
# Thiết lập caption cho cửa sổ
pygame.display.set_caption("Option oneplayer")

player1_alive = True
player2_alive = True

# Các hằng số
FPS = 60
player_vel = 5
hero_weapon_vel = 17
enemy_weapon_vel = 4
enemy_vel = 1
rows = 2
columns = 8
last_enemy_shot = pygame.time.get_ticks()
clock = pygame.time.Clock()

font=item.FontGame(32)

# Khởi tạo người chơi
player = Pl.Player(300, 650)

player1 = Pl.Player(300, 650)
player2 = Pl.Player(600, 700)

# Hàm vẽ lại cửa sổ
def redraw_windowplayer(type):
    mainscreen.SCREEN.blit(item.BG, (0, 0))
    for en in enemies:
        en.draw(mainscreen.SCREEN)
    for food in foods:
        food.draw(mainscreen.SCREEN)
    for gift in gifts:
        gift.draw(mainscreen.SCREEN)
    if type == 1:
        player.draw(mainscreen.SCREEN)
        show_score(10, 10,1)
    if type == 2:
        if player1_alive:
            player1.draw(mainscreen.SCREEN)
        if player2_alive:
            player2.draw(mainscreen.SCREEN)
        show_score(10,10,2)
    pygame.display.update()

# Tạo danh sách enemy
def create_enemies():
    for row in range(rows):
        for col in range(columns):
            enemy = En.Enemy(100 + col * 100,100 + row * 70,random.choice([item.Enemy1,item.Enemy2,item.Enemy3]),100)
            enemies.append(enemy)
def show_score(x,y,type):
    if type == 1:
        score = font.render("Score: " + str(player.score_value),True,(255,0,0))
        mainscreen.SCREEN.blit(score, (x, y))
    if type == 2:
        score1 = font.render("Score: " + str(player1.score_value),True,(255,0,0))
        score2 = font.render("Score: " + str(player2.score_value), True, (255, 0, 0))
        mainscreen.SCREEN.blit(score1, (x, y))
        mainscreen.SCREEN.blit(score2, (x, y+50))

# Hàm Level1
def Level1(type):
    global running, lives, enemies, last_enemy_shot, foods,global_score, lives1,lives2,player1_alive,player2_alive,global_score1,global_score2
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
        if type == 1:
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
                if player.health <= 0:
                    lives -= 1
                if collide(en, player):
                    lives -= 1
                    enemies.remove(en)
                if (lives <= 0):
                    break

        if type == 2:

            if player1_alive:
                if keys[pygame.K_a] and player1.x - player_vel > 0:
                    player1.x -= player_vel
                if keys[pygame.K_d] and player1.x + player_vel + player1.get_width() < item.WIDTH:
                    player1.x += player_vel
                if keys[pygame.K_w] and player1.y - player_vel > 0:
                    player1.y -= player_vel
                if keys[pygame.K_s] and player1.y + player_vel + player1.get_height() < item.HEIGHT:
                    player1.y += player_vel
                if keys[pygame.K_SPACE]:
                    player1.shoot()
            if player2_alive:
                if keys[pygame.K_LEFT] and player2.x - player_vel > 0:
                    player2.x -= player_vel
                if keys[pygame.K_RIGHT] and player2.x + player_vel + player2.get_width() < item.WIDTH:
                    player2.x += player_vel
                if keys[pygame.K_UP] and player2.y - player_vel > 0:
                    player2.y -= player_vel
                if keys[pygame.K_DOWN] and player2.y + player_vel + player2.get_height() < item.HEIGHT:
                    player2.y += player_vel
                if keys[pygame.K_l]:
                    player2.shoot()


            for en in enemies:
                en.move(enemy_vel)
                en.move_weapons(enemy_weapon_vel, player1)
                en.move_weapons(enemy_weapon_vel, player2)
                if (player1.health == 0): lives1 -= 1  # nếu player hết máu thì thua
                if collide(en, player1):  # nếu player va chạm với enemy thì hết máu luôn
                    lives -= 1
                    enemies.remove(en)
                if (player2.health == 0): lives2 -= 1  # nếu player hết máu thì thua
                if collide(en, player2):  # nếu player va chạm với enemy thì hết máu luôn
                    lives -= 1
                    enemies.remove(en)

        #enemy random bắn ra đạn
        if enemies:
            if time_now - last_enemy_shot > ENEMY_COOLDOWN:
                random.choice(enemies).shoot()
                last_enemy_shot = time_now
        else:
            break

        # làm cho enemy chạy qua chạy lại
        for en in enemies:
            if en.x + en.get_width() >= item.WIDTH or en.x <= 0:
                for en in enemies:
                    en.direction *= -1
                break


        if type == 1:
            player.move_weapons(-hero_weapon_vel, enemies)

            player.move_foods(4, foods)

        if type == 2:
            player1.move_weapons(-hero_weapon_vel, enemies)

            player1.move_foods(4, foods)

            player2.move_weapons(-hero_weapon_vel, enemies)

            player2.move_foods(4, foods)


        if not enemies:
            drawWinner()  # Hiển thị màn hình chiến thắng
            pygame.display.update()
            time.sleep(3)  # Đợi 3 giây
            global_score = player.score_value
            global_score1 = player1.score_value
            global_score2 = player2.score_value
            Level2(type)
            break

        if (lives <= 0):
            drawGameOver()  # Hiển thị màn hình thất bại
            pygame.display.update()
            time.sleep(3)
            running = False
            break

        if (lives1 <= 0):
            player1_alive = False


        if (lives2 <= 0):
            player2_alive = False

        if(lives1 <= 0 and lives2 <= 0):
            drawGameOver()
            pygame.display.update()
            time.sleep(3)
            running = False
            break
        redraw_windowplayer(type)

# Hàm trả về số mạng
def get_lives():
    return lives

