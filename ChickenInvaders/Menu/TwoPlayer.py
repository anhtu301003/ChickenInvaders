import pygame
from ChickenInvaders.Menu.ButtonMenu import Button
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl

import time
import random

def twoplayer():
    pygame.display.set_caption("Option two player")
    running = True
    FPS = 60
    player1 = Pl.Player(300,650)
    player2 = Pl.Player(600, 700)
    player_vel = 5
    clock = pygame.time.Clock()
    def redraw_windowoneplayer():
        mainscreen.SCREEN.blit(item.BG, (0, 0))
        player1.draw(mainscreen.SCREEN)
        player2.draw(mainscreen.SCREEN)
        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_windowoneplayer()
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

        if keys[pygame.K_LEFT] and player2.x - player_vel > 0:
            player2.x -= player_vel
        if keys[pygame.K_RIGHT] and player2.x + player_vel + player2.get_width() < item.WIDTH:
            player2.x += player_vel
        if keys[pygame.K_UP] and player2.y - player_vel > 0:
            player2.y -= player_vel
        if keys[pygame.K_DOWN] and player2.y + player_vel + player2.get_height() < item.HEIGHT:
            player2.y += player_vel



        pygame.display.update()