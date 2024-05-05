import pygame
from ChickenInvaders.Menu.ButtonMenu import Button
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item
import ChickenInvaders.Entities.Player as Pl

import time
import random

def oneplayer():
    pygame.display.set_caption("Option oneplayer")
    running = True
    FPS = 60
    player = Pl.Player(300,650)
    player_vel =5;
    clock = pygame.time.Clock()
    def redraw_windowoneplayer():
        mainscreen.SCREEN.blit(item.BG, (0, 0))
        player.draw(mainscreen.SCREEN)
        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_windowoneplayer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel+ player.get_width() < item.WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < item.HEIGHT:
            player.y += player_vel



        pygame.display.update()
