from fill import screen, pygame

BLACK = (0, 0, 0)


def line():
    """
    создает руки правой пары и нитку шарика
    """
    pygame.draw.line(screen, BLACK, [255, 150], [285, 190], 1)
    pygame.draw.line(screen, BLACK, [285, 190], [315, 150], 1)
    pygame.draw.line(screen, BLACK, [365, 150], [380, 190], 1)
    pygame.draw.line(screen, BLACK, [380, 190], [385, 140], 1)
    pygame.draw.line(screen, BLACK, [195, 180], [195, 70], 1)


def left_legs_man():
    """
    ноги левого мужчины
    """
    pygame.draw.line(screen, BLACK, [55, 240], [40, 320], 1)
    pygame.draw.line(screen, BLACK, [20, 320], [40, 320], 1)
    pygame.draw.line(screen, BLACK, [85, 240], [90, 320], 1)
    pygame.draw.line(screen, BLACK, [90, 320], [110, 320], 1)


def right_legs_man():
    """
    ноги правого мужчины
    :return:
    """
    pygame.draw.line(screen, BLACK, [325, 240], [310, 320], 1)
    pygame.draw.line(screen, BLACK, [290, 320], [310, 320], 1)
    pygame.draw.line(screen, BLACK, [355, 240], [370, 320], 1)
    pygame.draw.line(screen, BLACK, [370, 320], [390, 320], 1)


def left_legs_woman():
    """
    ноги левой женщины
    """
    pygame.draw.line(screen, BLACK, [150, 250], [150, 320], 1)
    pygame.draw.line(screen, BLACK, [170, 250], [170, 320], 1)
    pygame.draw.line(screen, BLACK, [150, 320], [130, 320], 1)
    pygame.draw.line(screen, BLACK, [170, 320], [190, 320], 1)
    pygame.draw.line(screen, BLACK, [195, 180], [245, 150], 1)


def right_legs_woman():
    """
    ноги правой женщины
    """
    pygame.draw.line(screen, BLACK, [240, 250], [240, 320], 1)
    pygame.draw.line(screen, BLACK, [260, 250], [260, 320], 1)
    pygame.draw.line(screen, BLACK, [220, 320], [240, 320], 1)
    pygame.draw.line(screen, BLACK, [260, 320], [280, 320], 1)


def left_arm_man():
    """
    руки левого мужчины
    """
    pygame.draw.line(screen, BLACK, [20, 220], [45, 150], 1)
    pygame.draw.line(screen, BLACK, [20, 220], [15, 120], 1)
    pygame.draw.line(screen, BLACK, [95, 150], [120, 190], 1)


def left_arm_woman():
    """
    руки левой женщины
    """
    pygame.draw.line(screen, BLACK, [120, 190], [155, 150], 1)
    pygame.draw.line(screen, BLACK, [165, 150], [195, 180], 1)
