import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render('Score: ' + f'{current_time}', False, 'Black')
    score_rect = score_surface.get_rect(center=(670, 50))
    screen.blit(score_surface, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:  # check if sth in the list first
        for obstacle_rect in obstacle_list:
            # move everything in the rect
            obstacle_rect.x -= 5  # every obstacle moved to the left by a tiny bit on every cycle of game loop

            if obstacle_rect.bottom == 300:
                screen.blit(ghost_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True


def player_animation():
    # play walking animation if the player is on the floor
    # or else play jump surface
    global player_surface, player_index

    if player_rect.bottom < 300:  # if player on the ground or not
        player_surface = player_jump
    else:
        player_index += 0.1  # adding 0.1 to take a little time to change to next index
        if player_index >= len(players): player_index = 0
        player_surface = players[int(player_index)]


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

# Obstacles
ghost_frame_1 = pygame.image.load('graphics/ghost1.png').convert_alpha()
ghost_frame_2 = pygame.image.load('graphics/ghost2.png').convert_alpha()
ghost_frames = [ghost_frame_1, ghost_frame_2]
ghost_frame_index = 0
ghost_surface = ghost_frames[ghost_frame_index]

fly_frame_1 = pygame.image.load('graphics/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

# score_surface = test_font.render('Score:', False, 'Black')
# score_rect = score_surface.get_rect(center = (670,50))

# text_surface = test_font.render(text info, anti alias, color )
text_surface = test_font.render('Run for life', False, 'Black')
ghost_x_position = 30

# Player
player_1 = pygame.image.load('graphics/player1.png').convert_alpha()
player_2 = pygame.image.load('graphics/player2.png').convert_alpha()
players = [player_1, player_2]
player_index = 0
player_jump = pygame.image.load('graphics/jump.png').convert_alpha()

player_surface = players[player_index]
player_rect = player_surface.get_rect(midbottom=(50, 300))

player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/player1.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Run for life', False, 'Black')
game_name_rect = game_name.get_rect(center=(400, 60))

game_message = test_font.render('Press space to run', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

ghost_animation_timer = pygame.USEREVENT +2
pygame.time.set_timer(ghost_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                # ghost_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):  # output 0 or 1 -> false or true
                    obstacle_rect_list.append(ghost_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(ghost_surface.get_rect(bottomright=(randint(900, 1100), 200)))
            if event.type == ghost_animation_timer:
                if ghost_frame_index == 0: ghost_frame_index = 1
                else: ghost_frame_index = 0
                ghost_surface = ghost_frames[ghost_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (100, 25))

        # pygame.draw.rect(screen, 'Pink', score_rect)
        # pygame.draw.rect(screen, 'Pink', score_rect, 6)
        # screen.blit(score_surface,score_rect)
        score = display_score()

        # ghost_rect.x -= 4
        # if ghost_rect.right <= 0: ghost_rect.left = 800
        # screen.blit(ghost_surface, ghost_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity  # apply the gravity variable to move the player downwards

        # 300 is the position of the ground
        # as long as the player exceed in the ground, set the player on the top of the ground
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collision(player_rect, obstacle_rect_list)

    else:
        screen.fill('Yellow')
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

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
