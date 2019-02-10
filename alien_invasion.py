import sys

import pygame
from settings import Settings

def run_game():
	# initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	bg_color = (230, 230, 230)

	# start the main loop for the game
	while True:
		# watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# Redraw the scrren during each pass through the game loop
		screen.fill(ai_settings.bg_color)

		# Make the most recently drawn screen invisible
		pygame.display.flip()


# run game
run_game()
print('Done playing game!')