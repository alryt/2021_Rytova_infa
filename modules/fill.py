import pygame

FPS = 30
screen = pygame.display.set_mode((400, 400))
GREEN = (154, 205, 50)
BLUE = (0, 204, 255)


def fill():
    """
    создает экран с задним фоном из зеленого и голубого цвета

    """
    screen.fill("white")
    pygame.draw.rect(screen, GREEN, (0, 200, 400, 400))
    pygame.draw.rect(screen, BLUE, (0, 0, 400, 200))
