import os
import ChickenInvaders.Resource.Music.importmusic as itemMusic
import pygame,sys
from ChickenInvaders.Menu.ButtonMenu import Button
import ChickenInvaders.importitem as item
from pygame import mixer
pygame.init()

#create screen
SCREEN = pygame.display.set_mode((item.WIDTH, item.HEIGHT))

#set name Screen
pygame.display.set_caption("Menu")
def main_menu(oneplayer_function, twoplayer_function):
    mixer.init()
    mixer.music.load(itemMusic.musicwinner)
    mixer.music.play()
    def redraw_window():
        SCREEN.blit(item.BG, (0, 0))


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