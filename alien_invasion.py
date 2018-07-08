import pygame

from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()


    # Make an alien
    # alien = Alien(ai_settings, screen)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
