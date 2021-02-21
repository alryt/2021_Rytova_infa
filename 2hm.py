import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill("white")
rect(screen, (154, 205, 50), (0, 200, 400, 400))
rect(screen, (0, 204, 255), (0, 0, 400, 200))
circle(screen, (255, 192, 203), (130, 100), 30)
circle(screen, (255, 192, 203), (250, 100), 30)
pygame.draw.ellipse(screen, (128, 128, 128), (100, 130, 60, 150))
pygame.draw.line(screen, (0, 0, 0), [110, 150], [60, 220], 1)
pygame.draw.line(screen, (0, 0, 0), [150, 150], [180, 220], 1)
pygame.draw.line(screen, (0, 0, 0), [180, 220], [243, 150], 1)
pygame.draw.line(screen, (0, 0, 0), [243, 150], [300, 180], 1)
pygame.draw.line(screen, (0, 0, 0), [300, 180], [330, 140], 1)
pygame.draw.line(screen, (0, 0, 0), [315, 200], [335, 120], 1)

pygame.draw.line(screen, (0, 0, 0), [120, 270], [90, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [90, 350], [70, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [140, 270], [160, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [160, 350], [180, 350], 1)

pygame.draw.line(screen, (0, 0, 0), [260, 280], [260, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [240, 280], [240, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [240, 350], [220, 350], 1)
pygame.draw.line(screen, (0, 0, 0), [260, 350], [280, 350], 1)

poligon_color = (255, 0, 255)
poligon_points = [(200,280),(300,280),(250,130)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)

poligon_color = (255, 0, 0)
poligon_points = [(335,120),(320,90),(355,90)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)
circle(screen, (255, 0, 0), (330, 90), 9)
circle(screen, (255, 0, 0), (345, 90), 9)

poligon_color = (255, 204, 0)
poligon_points = [(60, 220),(65,170),(40,180)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)
circle(screen, (255, 0, 0), (59, 165), 9)
circle(screen, (128, 0, 0), (43, 170), 9)
circle(screen, (255, 255, 255), (50, 160), 9)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()