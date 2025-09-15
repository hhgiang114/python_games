import pygame
from sys import exit


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run for life')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/sky.jpg')
#test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))



    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)
