import sys

import pygame
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
	ship = Ship(screen)

	# start the main loop for the game
	while True:
		# watch for keyboard and mouse events
		gf.check_events(ship)

		# update ship
		ship.update()
		
		# Redraw the scrren during each pass through the game loop
		gf.update_screen(ai_settings, screen, ship)


# run game
run_game()
print('Done playing game!')