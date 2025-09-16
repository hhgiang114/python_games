import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render('Score: ' + f'{current_time}', False, 'Black')
    score_rect = score_surface.get_rect(center=(670, 50))
    screen.blit(score_surface, score_rect)
    return current_time


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Run for life')
clock = pygame.time.Clock()

# Fonts
# test_font = pygame.font.Font(font type, font size)
test_font = pygame.font.Font('fonts/MedodicaRegular.otf', 50)

# Game states
game_active = False

start_time = 0
score = 0

# Surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
ghost_surface = pygame.image.load('graphics/ghost.png').convert_alpha()
ghost_rect = ghost_surface.get_rect(bottomright=(600, 300))

# score_surface = test_font.render('Score:', False, 'Black')
# score_rect = score_surface.get_rect(center = (670,50))

# text_surface = test_font.render(text info, anti alias, color )
text_surface = test_font.render('Run for life', False, 'Black')
ghost_x_position = 30

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50, 300))

player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/player.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Run for life', False, 'Black')
game_name_rect = game_name.get_rect(center=(400, 60))

game_message = test_font.render('Press space to run', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 330))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # mouse motion to click on the player
            # player_rect.bottom >= 300 -> make sure the player can only jump when he's on the ground
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                ghost_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (100, 25))

        # pygame.draw.rect(screen, 'Pink', score_rect)
        # pygame.draw.rect(screen, 'Pink', score_rect, 6)
        # screen.blit(score_surface,score_rect)
        score = display_score()

        ghost_rect.x -= 4
        if ghost_rect.right <= 0: ghost_rect.left = 800
        screen.blit(ghost_surface, ghost_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity  # apply the gravity variable to move the player downwards

        # 300 is the position of the ground
        # as long as the player exceed in the ground, set the player on the top of the ground
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # Collision
        if ghost_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:  #space button
    #     print('jump')
    # if player_rect.colliderect(ghost_rect):
    #    print('Collision')

    # if the mouse touch the player_rect
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        pygame.mouse.get_pressed()

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)

# player character
# 1. keyboard input
# pygame.key or event loop
# 2. jump + gravity
