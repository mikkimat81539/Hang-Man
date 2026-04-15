import pygame

pygame.init()

class displayHints:
	def __init__(self, x_pos, y_pos, color, thickness):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.color = color
		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
		self.end_pos = pygame.math.Vector2(self.x_pos + 50, self.y_pos)
		self.thickness = thickness

	def drawLines(self, surface):
		pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.thickness)
