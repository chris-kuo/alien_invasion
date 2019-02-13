import sys

# pygame imports
import pygame

# game class imports
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to key presses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# set movement flag
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# unset movement flag
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False	


def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	# redraw all bullets behind ship and alien
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)

	# Make the most recently drawn screen visible
	pygame.display.flip()

def update_bullets(bullets):
	"""Update positions of bullets and get rid of old bullets"""
	# update bullets
	bullets.update()

	# Get rid of bullets that have moved offscreen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
	available_space = ai_settings.screen_width - (2 * alien_width)
	number_aliens_x = int(available_space / (2 * alien_width))
	return number_aliens_x	

def create_alien(ai_settings, screen, aliens, alien_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + alien_number * alien_width * 2
	alien.rect.x = alien.x
	aliens.add(alien)	

def create_fleet(ai_settings, screen, aliens):
	'''Create a full fleet of aliens'''
	# Create an alien and find the number of aliens in a row
	# Spacing between each alien is equal to one alien width
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

	# Create first row of aliens
	for alien_number in range(number_aliens_x):
		# create alien and place in row
		create_alien(ai_settings, screen, aliens, alien_number)
