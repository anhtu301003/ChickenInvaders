import pygame
import sys
from ButtonMenu import Button

pygame.init()

SCREEN = pygame.display.set_mode((1400, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Resource/Background/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def main_menu(oneplayer_function, twoplayer_function):
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        ONEPLAYER_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                                  text_input="1 Player", font=get_font(75), base_color="#d7fcd4",
                                  hovering_color="White")
        TWOPLAYER_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                  text_input="2 Player", font=get_font(75), base_color="#d7fcd4",
                                  hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

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