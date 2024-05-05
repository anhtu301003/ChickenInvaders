import pygame,sys
from ChickenInvaders.Menu.ButtonMenu import Button
import ChickenInvaders.Menu.mainscreen as mainscreen
import ChickenInvaders.importitem as item

def twoplayer():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        mainscreen.SCREEN.fill("white")

        OPTIONS_TEXT = mainscreen.get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        mainscreen.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=mainscreen.get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(mainscreen.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    mainscreen.main_menu()

        pygame.display.update()
