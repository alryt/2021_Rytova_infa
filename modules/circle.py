from fill import screen, pygame

RED = (255, 0, 0)
Brown_Raspberry = (128, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)
GREY = (128, 128, 128)


def circle_middle():
    """
    создает кружочки шарика, расположенные по центру
    """
    pygame.draw.circle(screen, RED, (205, 33), 11)
    pygame.draw.circle(screen, Brown_Raspberry, (185, 35), 11)
    pygame.draw.circle(screen, WHITE, (195, 25), 11)


def circle_right():
    """
    создает кружочки шарика, расположенные справа
    """
    pygame.draw.circle(screen, RED, (397, 90), 11)
    pygame.draw.circle(screen, Brown_Raspberry, (378, 90), 11)
    pygame.draw.circle(screen, WHITE, (382, 83), 11)


def circle_left():
    """
    создает кружочки шарика, расположенные слева
    """
    pygame.draw.circle(screen, RED, (10, 93), 7)
    pygame.draw.circle(screen, RED, (23, 93), 7)


def heads():
    """
    создает головы людей
    """
    pygame.draw.circle(screen, PINK, (70, 100), 30)
    pygame.draw.circle(screen, PINK, (160, 100), 30)
    pygame.draw.circle(screen, PINK, (250, 100), 30)
    pygame.draw.circle(screen, PINK, (340, 100), 30)


def ellipse():
    """
    создает тела мужчин
    """
    pygame.draw.ellipse(screen, GREY, (40, 120, 60, 130))
    pygame.draw.ellipse(screen, GREY, (310, 120, 60, 130))
