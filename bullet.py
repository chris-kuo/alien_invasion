import pygame

from pygame.sprite import sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship."""

	def __init__(self, ai_settings, screen, ship):
		"""Crae a bullet object at the ship's current location"""
		# super(Bullet, selt).__init__() # python 2.7
		super().__init__() # python 3+
		self.screen = screen

		# Create a bullet rect at (0, 0) and then set correct position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the bullet's position as decimal
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		""" Move the bullet up the screen."""
		# update the decimal position of the bullet
		self.y -= self.speed_factor
		# update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)