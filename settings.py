class Settings():
	"""A class to store all settings for Alien Invasion"""

	def __init__(self):
		"""initialize the game's settings"""
		# Screen settings
		self.screen_width = 800
		self.screen_height = 600

		# ship settings
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5