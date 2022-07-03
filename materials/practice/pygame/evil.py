import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# rect(screen, (255, 0, 255), (100, 100, 200, 200))
# rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
# polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                                (300,100), (100,100)])
# polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                                (300,100), (100,100)], 5)
rect(screen, (217, 217, 217), (0, 0, 400, 400), 0)
circle(screen, (255, 255, 0), (200, 200), 150, 0)
circle(screen, (255, 0, 0), (130, 160), 30, 0)
circle(screen, (255, 0, 0), (270, 160), 20, 0)
circle(screen, (0, 0, 0), (130, 160), 15, 0)
circle(screen, (0, 0, 0), (270, 160), 10, 0)

line(screen, (0, 0, 0), (70, 80), (165, 140),15) # Left eyebrow
line(screen, (0, 0, 0), (330, 95), (235, 150),15) # Right eyebrow
line(screen, (0, 0, 0), (120, 270), (280, 270),15) # mouth



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()