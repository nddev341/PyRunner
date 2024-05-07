import pygame
from sys import exit
from random import randint, choice
from Player import Player
from Obstacle import Obstacle

def display_score():
    current_time = int(pygame.time.get_ticks() // 1000) - start_time
    timer_surface = font.render('Score : ' + str(current_time), False, 'black')
    timer_rect = timer_surface.get_rect(topleft=(10, 10))
    screen.blit(timer_surface, timer_rect)
    return current_time

def collision_Sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacles_group, False):
        obstacles_group.empty()
        return False
    else:
        return True

def render_intro_screen():
    screen.fill((94, 129, 162))
    screen.blit(game_name, game_name_rect)
    screen.blit(player_stand, player_stand_rect)
    screen.blit(game_message_surface, game_message_rect)
    screen.blit(game_instructions_surface, game_instructions_rect)

def render_game_over_screen():
    screen.fill((94, 129, 162))
    screen.blit(game_name, game_name_rect)
    game_over_surface = font.render('Game Over', False, 'black')
    game_over_rect = game_over_surface.get_rect(center=(400, 120))
    game_message_rect = game_message_surface.get_rect(center=(400, 280))
    screen.blit(game_message_surface, game_message_rect)
    screen.blit(game_over_surface, game_over_rect)

def render_score(score):
    score_surface = font.render(f'Score : {score}', False, 'black')
    score_rect = score_surface.get_rect(center=(395, 200))
    screen.blit(score_surface, score_rect)


# Initialize Pygame
pygame.init()
# Set up the screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PyRunner")
# Set up the clock
clock = pygame.time.Clock()
# Game Variables
game_active = False
start_time = 0
score = 0

# Font
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Music
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(-1).set_volume(0.2)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacles_group = pygame.sprite.Group()

# Intro screen
game_name = font.render('PyRunner', False, (111,196,169))
game_name_rect = game_name.get_rect(center=(400, 50))
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 210))

game_message_surface = font.render('Press Space to Start Game', False, 'black')
game_message_rect = game_message_surface.get_rect(center=(400, 100))
game_instructions_surface = font.render('Press Space to Jump', False, 'black')
game_instructions_rect = game_instructions_surface.get_rect(center=(player_stand_rect.centerx, player_stand_rect.bottom + 50))

# Surfaces
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
surfaces = []
surfaces.append([sky_surface, (0, 0)])
surfaces.append([ground_surface, (0, 300)])

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:      
            if event.type == obstacle_timer:
                obstacles_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() // 1000)

    if game_active:
        # Draw the screen
        for surface in surfaces:
            screen.blit(surface[0], surface[1])
        score = display_score()

        # Player
        player.draw(screen)
        player.update()

        # Obstacles
        obstacles_group.draw(screen)
        obstacles_group.update()

        # Collisions detection
        game_active = collision_Sprite()

    else:
        if score == 0: 
            render_intro_screen()
        else: 
            render_game_over_screen()
            render_score(score)

    # Update the screen
    pygame.display.update()
    clock.tick(60)  # 60 FPS