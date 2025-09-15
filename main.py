import pygame
from sys import exit


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run for life')
clock = pygame.time.Clock()

#Fonts
#test_font = pygame.font.Font(font type, font size)
test_font = pygame.font.Font('fonts/MedodicaRegular.otf', 50)

#Surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ghost_surface = pygame.image.load('graphics/ghost.png').convert_alpha()

#text_surface = test_font.render(text info, anti alias, color )
text_surface = test_font.render('Run for life', False, 'Black')
ghost_x_position = 30


player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (100,25))
    ghost_x_position -= 4

    if ghost_x_position < -100 : ghost_x_position = 800
    screen.blit(ghost_surface, (ghost_x_position, 230))
    print(player_rect.left) #20

    screen.blit(player_surface, player_rect)


    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)
