import pygame

pygame.init()

#class displayHints:
#	def __init__(self, x_pos, y_pos, color, thickness):
#		self.x_pos = x_pos
#		self.y_pos = y_pos
#		self.color = color
#		self.start_pos = pygame.math.Vector2(self.x_pos, self.y_pos)
#		self.end_pos = pygame.math.Vector2(self.x_pos + 50, self.y_pos)
#		self.thickness = thickness
#
#	def drawLines(self, surface, word):
#			pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.thickness)

class displayFonts:
	def __init__(self, x_pos, y_pos, color, size):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.color = color
		self.size = size
		self.setSurface = pygame.Surface((35, 50))

	def drawText(self, surface, words):
		hints = "_ " * len(words) 

		createFont = pygame.font.SysFont("Arial.ttf", self.size)
		renderFont = createFont.render(hints, False, self.color)
		surface.blit(renderFont, (self.x_pos, self.y_pos))

	def drawSurface(self, surface, words):
		surface.blit(self.setSurface, (self.x_pos, self.y_pos))
		self.setSurface.fill("white")	
