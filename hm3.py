import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill("white")

rect(screen, (154, 205, 50), (0, 200, 400, 400))
rect(screen, (0, 204, 255), (0, 0, 400, 200))

pygame.draw.ellipse(screen, (128, 128, 128), (40, 120, 60, 130))
pygame.draw.ellipse(screen, (128, 128, 128), (310, 120, 60, 130))

poligon_color = (255, 0, 255)
poligon_points = [(220,250),(280,250),(250,130)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)

poligon_color = (255, 0, 255)
poligon_points = [(130,250),(190,250),(160,130)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)

pygame.draw.line(screen, (0, 0, 0), [55, 240], [40, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [20, 320], [40, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [85, 240], [90, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [90, 320], [110, 320], 1)

pygame.draw.line(screen, (0, 0, 0), [150, 250], [150, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [170, 250], [170, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [130, 320], [150, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [170, 320], [190, 320], 1)

pygame.draw.line(screen, (0, 0, 0), [240, 250], [240, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [260, 250], [260, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [220, 320], [240, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [260, 320], [280, 320], 1)

pygame.draw.line(screen, (0, 0, 0), [325, 240], [310, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [290, 320], [310, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [355, 240], [370, 320], 1)
pygame.draw.line(screen, (0, 0, 0), [370, 320], [390, 320], 1)

pygame.draw.line(screen, (0, 0, 0), [20, 220], [45, 150], 1)
pygame.draw.line(screen, (0, 0, 0), [20, 220], [15, 120], 1)

pygame.draw.line(screen, (0, 0, 0), [95, 150], [120, 190], 1)
pygame.draw.line(screen, (0, 0, 0), [120, 190], [155, 150], 1)
pygame.draw.line(screen, (0, 0, 0), [165, 150], [195, 180], 1)
pygame.draw.line(screen, (0, 0, 0), [195, 180], [245, 150], 1)
pygame.draw.line(screen, (0, 0, 0), [195, 180], [195, 70], 1)

poligon_color = (255, 215, 0)
poligon_points = [(195, 70),(170,40),(215,40)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)
circle(screen, (255, 0, 0), (205, 33), 11)
circle(screen, (128, 0, 0), (185, 35), 11)
circle(screen, (255, 255, 255), (195, 25), 11)

pygame.draw.line(screen, (0, 0, 0), [255, 150], [285, 190], 1)
pygame.draw.line(screen, (0, 0, 0), [285, 190], [315, 150], 1)
pygame.draw.line(screen, (0, 0, 0), [365, 150], [380, 190], 1)
pygame.draw.line(screen, (0, 0, 0), [380, 190], [385, 140], 1)

poligon_color = (255, 215, 0)
poligon_points = [(385, 140),(378, 90),(397, 90)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)

circle(screen, (255, 0, 0), (397, 90), 11)
circle(screen, (128, 0, 0), (378, 90), 11)
circle(screen, (255, 255, 255), (382, 83), 11)

poligon_color = (255, 0, 0)
poligon_points = [(7, 95),(15,120),(25,95)]
poligon_width = 0
pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)

circle(screen, (255, 0, 0), (10, 93), 7)
circle(screen, (255, 0, 0), (23, 93), 7)

circle(screen, (255, 192, 203), (70, 100), 30)
circle(screen, (255, 192, 203), (160, 100), 30)
circle(screen, (255, 192, 203), (250, 100), 30)
circle(screen, (255, 192, 203), (340, 100), 30)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()