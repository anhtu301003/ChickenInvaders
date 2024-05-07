import pygame
import ChickenInvaders.Resource.Music.importmusic as itemMusic
import ChickenInvaders.importitem as item
import ChickenInvaders.Menu.mainscreen as mainscreen
def drawGameOver():
    mainscreen.SCREEN.fill((0, 0, 0))

    # Tạo font cho chữ Winner
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over", True, (255, 255, 255))  # Chữ Winner màu trắng

    # Lấy kích thước của chữ Winner
    text_rect = text.get_rect()

    # Đặt vị trí của chữ Winner ở giữa màn hình
    text_rect.center = (item.WIDTH // 2, item.HEIGHT // 2)

    # Vẽ chữ Winner lên màn hình
    mainscreen.SCREEN.blit(text, text_rect)
    pygame.mixer.music.load(itemMusic.musicgameover)
    pygame.mixer.music.play()
    # Cập nhật màn hình
    pygame.display.flip()