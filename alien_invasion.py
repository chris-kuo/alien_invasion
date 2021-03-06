import sys

# pygame imports
import pygame
from pygame.sprite import Group

# game class imports
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# make a ship
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets in
	bullets = Group()
	aliens = Group()

	# create fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# start the main loop for the game
	while True:
		# watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)

		# update ship
		ship.update()

		# update the aliens
		gf.update_aliens(ai_settings, aliens)

		# update bullets
		gf.update_bullets(bullets)

		# Redraw the scrren during each pass through the game loop
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


# run game
run_game()
print('Done playing game!')