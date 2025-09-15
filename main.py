import pygame
from sys import exit

from pygame.examples.sprite_texture import group

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run for life')
clock = pygame.time.Clock()

#Fonts
#test_font = pygame.font.Font(font type, font size)
test_font = pygame.font.Font('fonts/MedodicaRegular.otf', 50)

#Surfaces
sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
cat_surface = pygame.image.load('graphics/cat.png')

#text_surface = test_font.render(text info, anti alias, color )
text_surface = test_font.render('Run for life', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (100,25))
    screen.blit(cat_surface, (30, 250))



    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)
