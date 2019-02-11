import sys

# pygame imports
import pygame

# game class imports
from bullet import Bullet

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
		# Create a new bullet and add it to the bullets group
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# unset movement flag
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False	


def update_screen(ai_settings, screen, ship, bullets):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	# redraw all bullets behind ship and alien
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

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