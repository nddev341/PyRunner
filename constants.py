import pygame

pygame.init()

# game
FPS = 60

# screen
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 400
SCREEN_SIZE = (SCREEN_HEIGHT, SCREEN_WIDTH)

# music
MUSIC_PATH = 'audio/music.wav'
JUMP_SOUND_PATH = 'audio/jump.mp3'
MUSIC_VOLUME = 0.2

# colors
TURQUOISE = (111, 196, 169)
INTRO_SCREEN_COLOR = (94, 129, 162)

# font
FONT_PATH = 'font/Pixeltype.ttf'
FONT_SIZE = 50
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)
GAME_NAME = "PyRunner"

# intro screen
GAME_TITLE_INTRO_CORD = (400, 50)
PLAYER_STAND_INTRO_CORD = (400, 210)
GAME_MESSAGE_INTRO_CORD = (400, 100)
PLAYER_STAND_PATH = 'graphics/Player/player_stand.png'
GAME_MESSAGE_INTRO = 'Press Space to Start Game'
GAME_INSTRUCTIONS_INTRO = 'Press Space to Jump'

# player
PLAYER_CORD = (80, 300)
GRAVITY = -20

# obstacles
OBSTACLE_SPAWN_TIME = 1500
OBSTACLES_TYPES = ['fly', 'snail', 'snail', 'snail']

# surfaces
SKY_CORD = (0, 0)
SKY_PATH = 'graphics/sky.png'
GROUND_CORD = (0, 300)
GROUND_PATH = 'graphics/ground.png'