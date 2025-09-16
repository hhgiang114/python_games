import pygame
from sys import exit

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Run for life')
clock = pygame.time.Clock()

# Fonts
# test_font = pygame.font.Font(font type, font size)
test_font = pygame.font.Font('fonts/MedodicaRegular.otf', 50)

# Surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ghost_surface = pygame.image.load('graphics/ghost.png').convert_alpha()
ghost_rect = ghost_surface.get_rect(bottomright=(600, 300))

score_surface = test_font.render('Score:', False, 'Black')
score_rect = score_surface.get_rect(center = (670,50))

# text_surface = test_font.render(text info, anti alias, color )
text_surface = test_font.render('Run for life', False, 'Black')
ghost_x_position = 30

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50, 300))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #mouse motion to click on the player
        #player_rect.bottom >= 300 -> make sure the player can only jump when he's on the ground
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20



    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (100, 25))

    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 6)
    screen.blit(score_surface,score_rect)

    ghost_rect.x -= 4
    if ghost_rect.right <= 0: ghost_rect.left = 800
    screen.blit(ghost_surface, ghost_rect)

    # Player
    player_gravity += 1
    player_rect.y += player_gravity     #apply the gravity variable to move the player downwards

    #300 is the position of the ground
    #as long as the player exceed in the ground, set the player on the top of the ground
    if player_rect.bottom >= 300: player_rect.bottom = 300


    screen.blit(player_surface, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:  #space button
    #     print('jump')
    #if player_rect.colliderect(ghost_rect):
    #    print('Collision')

    #if the mouse touch the player_rect
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        pygame.mouse.get_pressed()

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)


#player character
#1. keyboard input
#pygame.key or event loop
#2. jump + gravity