import time

import pygame,sys,os
from pygame import font
from pygame import mixer

import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item

from ChickenInvaders.Menu.ButtonMenu import Button

import ChickenInvaders.level.Level1 as lv1


game_modes = [
    {"Enemy_countdown":2000},
    {"Enemy_countdown":1000},
    {"Enemy_countdown":500}
]


game_mode_images=[item.easymode,item.mediummode,item.hardmode]
current_mode_index=0
def change_game_mode(direction):
    global current_mode_index
    if direction == "left":
        current_mode_index = max(0, current_mode_index - 1)
    elif direction == "right":
        current_mode_index = min(len(game_modes) - 1, current_mode_index + 1)

def display_game_mode_image():
    current_image = game_mode_images[current_mode_index]
    mainscreen.SCREEN.blit(current_image, (570, 500))

def Option():
    global game_running
    selected_game_mode = game_modes[0]  # Chế độ chơi mặc định
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        mainscreen.SCREEN.blit(item.BG, (0, 0))
        OPTIONS_TEXT = item.FontGame(100).render("OPTIONS", True, "White")
        OPTION_TEXT_WIDTH = OPTIONS_TEXT.get_width()
        mainscreen.SCREEN.blit(OPTIONS_TEXT, ((item.WIDTH-OPTION_TEXT_WIDTH)/2, 100))
        display_game_mode_image()
        GamemodeText = item.FontGame(50).render("GAME MODE:", True, "White")
        GamemodeText_WIDTH = GamemodeText.get_width()
        mainscreen.SCREEN.blit(GamemodeText, (250, 500))
        mainscreen.SCREEN.blit(item.NextLeft, (500, 500))
        mainscreen.SCREEN.blit(item.NextRight, (700, 500))
        OPTIONS_BACK = Button(image=None, pos=(500, 650),
                              text_input="BACK", font=item.FontGame(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(mainscreen.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return selected_game_mode
                elif pygame.Rect(500, 500, item.NextLeft.get_width(), item.NextLeft.get_height()).collidepoint(
                        OPTIONS_MOUSE_POS):
                    change_game_mode("left")
                    selected_game_mode = game_modes[current_mode_index]
                elif pygame.Rect(700, 500, item.NextRight.get_width(), item.NextRight.get_height()).collidepoint(
                        OPTIONS_MOUSE_POS):
                    change_game_mode("right")
                    selected_game_mode = game_modes[current_mode_index]
        pygame.display.update()