import pygame
from player import Player
from constants import *

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    return screen, clock

def load_intro_screen():
    game_name = FONT.render(GAME_NAME, False, TURQUOISE)
    game_name_rect = game_name.get_rect(center=GAME_TITLE_INTRO_CORD)
    player_stand = load_image(PLAYER_STAND_PATH)
    player_stand = expand_surface(player_stand)
    player_stand_rect = player_stand.get_rect(center=PLAYER_STAND_INTRO_CORD)
    game_message_surface = FONT.render(GAME_MESSAGE_INTRO, False, 'black')
    game_message_rect = game_message_surface.get_rect(center=GAME_MESSAGE_INTRO_CORD)
    game_instructions_surface = FONT.render(GAME_INSTRUCTIONS_INTRO, False, 'black')
    game_instructions_rect = game_instructions_surface.get_rect(center=(player_stand_rect.centerx, player_stand_rect.bottom + 50))
    return game_name, game_name_rect, player_stand, player_stand_rect, game_message_surface, game_message_rect, game_instructions_surface, game_instructions_rect
    
def load_resources():
    game_active = False
    score = 0
    start_time = 0
    bg_music = load_sounds(MUSIC_PATH)
    sky_surface = load_image(SKY_PATH)
    ground_surface = load_image(GROUND_PATH)
    return bg_music, sky_surface, ground_surface, game_active, score, start_time

def setup_groups():
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    obstacles_group = pygame.sprite.Group()
    return player, obstacles_group

def setup_timer():
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, OBSTACLE_SPAWN_TIME)
    return obstacle_timer

def display_score(screen, font, start_time):
    current_time = int(pygame.time.get_ticks() // 1000) - start_time
    timer_surface = font.render('Score : ' + str(current_time), False, 'black')
    timer_rect = timer_surface.get_rect(topleft=(10, 10))
    screen.blit(timer_surface, timer_rect)
    return current_time

def collision_Sprite(player, obstacles_group):
    if pygame.sprite.spritecollide(player.sprite, obstacles_group, False):
        obstacles_group.empty()
        return False
    else:
        return True

def render_intro_screen(screen, game_name, game_name_rect, player_stand, player_stand_rect, game_message_surface, game_message_rect, game_instructions_surface, game_instructions_rect):
    screen.fill((94, 129, 162))
    screen.blit(game_name, game_name_rect)
    screen.blit(player_stand, player_stand_rect)
    screen.blit(game_message_surface, game_message_rect)
    screen.blit(game_instructions_surface, game_instructions_rect)

def render_game_over_screen(screen, game_name, game_name_rect, game_message_surface, font):
    screen.fill((94, 129, 162))
    screen.blit(game_name, game_name_rect)
    game_over_surface = font.render('Game Over', False, 'black')
    game_over_rect = game_over_surface.get_rect(center=(400, 120))
    game_message_rect = game_message_surface.get_rect(center=(400, 280))
    screen.blit(game_message_surface, game_message_rect)
    screen.blit(game_over_surface, game_over_rect)

def render_score(screen, score, font):
    score_surface = font.render(f'Score : {score}', False, 'black')
    score_rect = score_surface.get_rect(center=(395, 200))
    screen.blit(score_surface, score_rect)

def load_image(path):
    try:
        image = pygame.image.load(path).convert_alpha()
        return image
    except pygame.error as e:
        raise FileNotFoundError(f"Unable to load the image at {path}: {e}")

def expand_surface(surface):
    return pygame.transform.rotozoom(surface, 0, 2)

def load_sounds(path):
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error as e:
        raise FileNotFoundError(f"Unable to load the sound at {path}: {e}")