from modules.fill import screen, pygame

MAGENTA = (255, 0, 255)
RED = (255, 0, 0)


def magenta_dress_right():
    """
    рисует правое платье
    """
    poligon_points = [(220, 250), (280, 250), (250, 130)]
    poligon_width = 0
    pygame.draw.polygon(screen, MAGENTA, poligon_points, poligon_width)


def magenta_dress_left():
    """
    рисует левое платье
    """
    poligon_points = [(130, 250), (190, 250), (160, 130)]
    poligon_width = 0
    pygame.draw.polygon(screen, MAGENTA, poligon_points, poligon_width)


def golden_smt():
    """
    рисует золотые выемки для шариков
    """
    GOLDEN = (255, 215, 0)
    poligon_points = [(195, 70), (170, 40), (215, 40)]
    poligon_width = 0
    pygame.draw.polygon(screen, GOLDEN, poligon_points, poligon_width)

    poligon_points_1 = [(385, 140), (378, 90), (397, 90)]
    poligon_width_1 = 0
    pygame.draw.polygon(screen, GOLDEN, poligon_points_1, poligon_width_1)


def poligon_left_red():
    """
    рисует справа красную выемку для шариков
    """
    poligon_points = [(7, 95), (15, 120), (25, 95)]
    poligon_width = 0
    pygame.draw.polygon(screen, RED, poligon_points, poligon_width)
