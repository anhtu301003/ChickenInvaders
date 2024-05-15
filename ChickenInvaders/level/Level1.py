import time

import pygame, sys, os
from pygame import font
from pygame import mixer

import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
from ChickenInvaders.Entities.Enemyweapon import Enemyweapon
from ChickenInvaders.Entities.Gitfbox import Gift
import random

from ChickenInvaders.Resource.Music import importmusic
from ChickenInvaders.level.Level2 import Level2


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	mainscreen.SCREEN.blit(img, (x, y))

def Level1(game_mode):
    # create sprite groups
    Player_group = pygame.sprite.Group()
    Player_Weapon_group = pygame.sprite.Group()
    Enemy_group = pygame.sprite.Group()
    Enemy_weapon_group = pygame.sprite.Group()
    Food_group = pygame.sprite.Group()
    Explosion_group = pygame.sprite.Group()
    Gift_group = pygame.sprite.Group()

    win = False

    clock = pygame.time.Clock()
    fps = 60
    running = True
    rows = 2
    cols = 5
    Enemy_cooldown = game_mode["Enemy_countdown"] # bullet cooldown in milliseconds
    last_Enemy_shot = pygame.time.get_ticks()
    countdown = 3
    last_count = pygame.time.get_ticks()
    gift_created = False

    def create_Enemies():
        # generate aliens
        for row in range(rows):
            for item in range(cols):
                enemy = En.Enemy(100 + item * 150, 100 + row * 100,100)
                Enemy_group.add(enemy)

    player = Pl.Player(int(item.WIDTH / 2), item.HEIGHT - 100, 100)
    Player_group.add(player)


    create_Enemies()
    font = item.FontGame(50)
    while running:
        clock.tick(fps)

        mainscreen.SCREEN.blit(item.BG, (0, 0))




        if countdown == 0:
            time_now = pygame.time.get_ticks()
            if time_now - last_Enemy_shot > Enemy_cooldown and len(Enemy_weapon_group) < 5 and len(Enemy_group) > 0:
                attacking_enemy = random.choice(Enemy_group.sprites())
                enemy_weapon = Enemyweapon(attacking_enemy.rect.centerx, attacking_enemy.rect.bottom)
                Enemy_weapon_group.add(enemy_weapon)
                last_Enemy_shot = time_now


            if not Enemy_group and not gift_created:
                gift = Gift(item.WIDTH / 2, 0)
                Gift_group.add(gift)
                gift_created = True


            player.update(Player_Weapon_group,Gift_group,Enemy_group,Enemy_weapon_group,Food_group)
            Player_Weapon_group.update(Enemy_group, Food_group,Explosion_group,Gift_group)
            Enemy_group.update()
            Enemy_weapon_group.update(Player_group)
            Food_group.update(Player_group)
            Gift_group.update(Player_group)

            if not Enemy_group and not win:
                win = True
                mixer.init()
                mixer.music.load(importmusic.musicwinner)
                mixer.music.play()
                win_timer = pygame.time.get_ticks()

            if win:
                draw_text('YOU WIN!', item.FontGame(40), (255, 255, 255), int(item.WIDTH / 2 - 70),
                          int(item.HEIGHT / 2))
                time_elapsed = (pygame.time.get_ticks() - win_timer) / 1000
                if time_elapsed >= 5:
                    # Chuyển sang màn 2 hoặc làm gì đó khác ở đây
                    Level2(game_mode,player.get_attribute())
                    break





        if countdown > 0:
            draw_text('GET READY!', item.FontGame(40), (255,255,255), int(item.WIDTH / 2 - 70), int(item.HEIGHT / 2 + 50))
            draw_text(str(countdown), item.FontGame(40), (255,255,255), int(item.WIDTH / 2), int(item.HEIGHT / 2 + 100))
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count > 1000:
                countdown -= 1
                last_count = count_timer

        if player.health <= 0:
            mixer.init()
            mixer.music.load(importmusic.musicgameover)
            mixer.music.play()
            draw_text('GAME OVER!', item.FontGame(40), (255, 255, 255), int(item.WIDTH / 2 - 90),
                      int(item.HEIGHT / 2))
            pygame.display.update()
            pygame.time.delay(3000)  # Dừng một thời gian trước khi thoát
            mainscreen.main_menu()

        Explosion_group.update()

        Player_group.draw(mainscreen.SCREEN)
        Player_Weapon_group.draw(mainscreen.SCREEN)
        Enemy_group.draw(mainscreen.SCREEN)
        Enemy_weapon_group.draw(mainscreen.SCREEN)
        Food_group.draw(mainscreen.SCREEN)
        Explosion_group.draw(mainscreen.SCREEN)
        Gift_group.draw(mainscreen.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ScorePlayer = font.render("Score: " + str(player.score), True, "White")
        mainscreen.SCREEN.blit(ScorePlayer, (10, 10))

        pygame.display.update()
