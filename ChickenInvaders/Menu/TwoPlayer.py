import pygame
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl
import ChickenInvaders.Entities.Enemy as En
from ChickenInvaders.Menu.Collide import collide
import random

def twoplayer():
    # variable
    pygame.display.set_caption("Option two player")
    running = True
    FPS = 60
    lives = 1
    enemies = []

    # khai báo đối tượng
    player1 = Pl.Player(300, 650)
    player2 = Pl.Player(600, 700)

    # thời gian ra đạn của enemy
    ENEMY_COOLDOWN = 1000

    # velocity
    player_vel = 5
    hero_weapon_vel = 17
    enemy_weapon_vel = 4
    enemy_vel = 1

    # hàng và cột cho enemies
    rows = 5
    columns = 8

    last_enemy_shot = pygame.time.get_ticks()

    clock = pygame.time.Clock()

    def redraw_windowtwoplayer():
        mainscreen.SCREEN.blit(item.BG, (0, 0))
        for en in enemies:
            en.draw(mainscreen.SCREEN)
        player1.draw(mainscreen.SCREEN)
        player2.draw(mainscreen.SCREEN)
        pygame.display.update()

    # tạo danh sách các enemy
    def create_enemies():
        for row in range(rows):
            for col in range(columns):
                enemy = En.Enemy(100 + col * 100, 100 + row * 70)
                enemies.append(enemy)

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
        if keys[pygame.K_a] and player1.x - player_vel > 0:
            player1.x -= player_vel
        if keys[pygame.K_d] and player1.x + player_vel+ player1.get_width() < item.WIDTH:
            player1.x += player_vel
        if keys[pygame.K_w] and player1.y - player_vel > 0:
            player1.y -= player_vel
        if keys[pygame.K_s] and player1.y + player_vel + player1.get_height() < item.HEIGHT:
            player1.y += player_vel
        if keys[pygame.K_SPACE]:
            player1.shoot()


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
            if (player1.health == 0): lives -= 1  # nếu player hết máu thì thua
            if collide(en, player1):  # nếu player va chạm với enemy thì hết máu luôn
                lives -= 1
                enemies.remove(en)
            if (player2.health == 0): lives -= 1  # nếu player hết máu thì thua
            if collide(en, player2):  # nếu player va chạm với enemy thì hết máu luôn
                lives -= 1
                enemies.remove(en)

        # random bắn của enemy
        if time_now - last_enemy_shot > ENEMY_COOLDOWN:
            random.choice(enemies).shoot()
            last_enemy_shot = time_now

        for en in enemies:
            if en.x + en.get_width() >= item.WIDTH or en.x <= 0:
                for en in enemies:
                    en.direction *= -1  # Đảo hướng di chuyển của enemy
                break

        player1.move_weapons(-hero_weapon_vel, enemies)
        player2.move_weapons(-hero_weapon_vel, enemies)

        redraw_windowtwoplayer()