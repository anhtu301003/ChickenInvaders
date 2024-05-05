import pygame,sys
from ButtonMenu import Button
import mainscreen
import importitem as item

background = pygame.image.load("./Resource/Background/background.png")
background = pygame.transform.scale(background, (item.WIDTH, item.HEIGHT))



def oneplayer():
    running = True

    while running:
        mainscreen.SCREEN.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass
                if event.key == pygame.K_d:
                    pass
                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_s:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                    pass



        pygame.display.update()
