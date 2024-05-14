import os
import ChickenInvaders.Resource.Music.importmusic as itemMusic
import pygame,sys

from ChickenInvaders.Menu import OnePlayer, TwoPlayer
from ChickenInvaders.Menu.ButtonMenu import Button
import ChickenInvaders.importitem as item
from pygame import mixer

from ChickenInvaders.Menu.OnePlayer import oneplayer
from ChickenInvaders.Menu.Option import Option, game_modes
from ChickenInvaders.Menu.TwoPlayer import twoplayer

pygame.init()

#create screen
SCREEN = pygame.display.set_mode((item.WIDTH, item.HEIGHT))

#set name Screen
pygame.display.set_caption("Menu")
def main_menu():
    mixer.init()
    mixer.music.load(itemMusic.musicwinner)
    mixer.music.play()
    def redraw_window():
        BG = pygame.image.load('Resource/Background/Background.png').convert()
        SCREEN.blit(BG, (0, 0))

        SCREEN.blit(item.TITLE_GAME, ((item.WIDTH - item.TITLE_GAME.get_width()) / 2, 0))

    while True:
        redraw_window()
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #tạo các lựa chọn
        ONEPLAYER_BUTTON = Button(image=None, pos=(500, 400),
                                  text_input="1 Player", font=item.FontGame(75), base_color="#d7fcd4",
                                  hovering_color="White")

        TWOPLAYER_BUTTON = Button(image=None, pos=(500, 500),
                                  text_input="2 Player", font=item.FontGame(75), base_color="#d7fcd4",
                                  hovering_color="White")

        OPTION_BUTTON = Button(image=None, pos=(500, 600),
                                  text_input="Option", font=item.FontGame(75), base_color="#d7fcd4",
                                  hovering_color="White")

        QUIT_BUTTON = Button(image=None, pos=(500, 700),
                             text_input="QUIT", font=item.FontGame(75), base_color="#d7fcd4", hovering_color="White")


        for button in [ONEPLAYER_BUTTON, TWOPLAYER_BUTTON,OPTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ONEPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if 'selected_game_mode' not in locals():
                        selected_game_mode = game_modes[0]  # Chế độ chơi mặc định
                    oneplayer(selected_game_mode)
                if TWOPLAYER_BUTTON.checkForInput(MENU_MOUSE_POS):
                    twoplayer()
                if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    selected_game_mode = Option()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

