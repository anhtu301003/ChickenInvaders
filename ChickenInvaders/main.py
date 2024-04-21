import pygame

# init
pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Chicken invader")
icon = pygame.image.load("./Resource/chicken_logo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("./Resource/background.png")

playerImg = pygame.image.load("./Resource/hero.png")
playerImg = pygame.transform.scale(playerImg, (110, 200))
playerX = 100
playerY = 100
running = True
playerX_change = 0
playerY_change = 0
def player(x,y):
    screen.blit(playerImg, (x, y))

while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change  = -1
            if event.key == pygame.K_d:
                playerX_change  = 1
            if event.key == pygame.K_w:
                playerY_change  = -1
            if event.key == pygame.K_s:
                playerY_change  = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX,playerY)
    pygame.display.update()
