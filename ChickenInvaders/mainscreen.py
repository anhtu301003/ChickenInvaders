import pygame
import sys
from ButtonMenu import Button
import importitem as item

pygame.init()

#create screen
SCREEN = pygame.display.set_mode((item.WIDTH, item.HEIGHT))

#set name Screen
pygame.display.set_caption("Menu")


def main_menu(oneplayer_function, twoplayer_function):
    while True:
        SCREEN.blit(item.BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(item.TITLE_GAME, ((item.WIDTH-item.TITLE_GAME.get_width())/2, 0))


        ONEPLAYER_BUTTON = Button(image=None, pos=(500, 400),
                                  text_input="1 Player", font=item.FontGame(75), base_color="#d7fcd4",
                                  hovering_color="White")

        TWOPLAYER_BUTTON = Button(image=None, pos=(500, 500),
                                  text_input="2 Player", font=item.FontGame(75), base_color="#d7fcd4",
                                  hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(500, 600),
                             text_input="QUIT", font=item.FontGame(75), base_color="#d7fcd4", hovering_color="White")


        for button in [ONEPLAYER_BUTTON, TWOPLAYER_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ONEPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    oneplayer_function()
                if TWOPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    twoplayer_function()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()