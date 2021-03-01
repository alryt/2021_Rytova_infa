from modules.circle import circle_middle, circle_right, circle_left, heads, ellipse
from modules.fill import fill, FPS, pygame
from modules.line import line, right_legs_man, right_legs_woman, left_legs_man, left_legs_woman, left_arm_man, \
    left_arm_woman
from modules.poligon import magenta_dress_right, magenta_dress_left, golden_smt, poligon_left_red


def image():
    pygame.init()

    fill()
    ellipse()
    magenta_dress_right()
    magenta_dress_left()
    left_legs_man()
    left_legs_woman()
    right_legs_woman()
    right_legs_man()
    left_arm_man()
    left_arm_woman()
    golden_smt()
    circle_middle()
    line()
    circle_right()
    poligon_left_red()
    circle_left()
    heads()

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


if __name__ == '__main__':
    image()
