import pygame

import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
