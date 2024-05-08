import pygame
from sys import exit
from random import choice
from obstacle import Obstacle
from constants import *
from actions import *


def main():
    screen, clock = init_pygame()

    game_name, game_name_rect, player_stand, player_stand_rect, game_message_surface, game_message_rect, game_instructions_surface, game_instructions_rect = load_intro_screen()

    bg_music, sky_surface, ground_surface, game_active, score, start_time = load_resources()

    player, obstacles_group = setup_groups()

    obstacle_timer = setup_timer()

    surfaces = []
    surfaces.append([sky_surface, SKY_CORD])
    surfaces.append([ground_surface, GROUND_CORD])

    bg_music.play(-1).set_volume(MUSIC_VOLUME)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:      
                if event.type == obstacle_timer:
                    obstacles_group.add(Obstacle(choice(OBSTACLES_TYPES)))
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() // 1000)

        if game_active:
            # Draw the screen
            for surface in surfaces:
                screen.blit(surface[0], surface[1])
            score = display_score(screen, FONT, start_time)

            # Player
            player.draw(screen)
            player.update()

            # Obstacles
            obstacles_group.draw(screen)
            obstacles_group.update()

            # Collisions detection
            game_active = collision_Sprite(player, obstacles_group)

        else:
            if score == 0: 
                render_intro_screen(screen, game_name, game_name_rect, player_stand, player_stand_rect, game_message_surface, game_message_rect, game_instructions_surface, game_instructions_rect)
            else: 
                render_game_over_screen(screen, game_name, game_name_rect, game_message_surface, FONT)
                render_score(screen, score, FONT)

        # Update the screen
        pygame.display.update()
        clock.tick(FPS)  # 60 FPS   

if __name__ == '__main__':
    main()