import pygame, string

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Surface Test")

# CLASS
class displaySurface:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.setSurface = pygame.Surface((self.width, self.height))
	
	def drawSurface(self, surface):
		surface.blit(self.setSurface, (self.x_pos, self.y_pos))
		self.setSurface.fill(self.color)

	def displayFont(self, activeString):
		createFont = pygame.font.SysFont("Arial.ttf",50)
		renderFont = createFont.render(activeString, False, "black")
		self.setSurface.blit(renderFont, (4, 10))

# SURFACE OBJECT
surface1 = displaySurface(20, 200, 30, 50, "white")

# WORDS
letters = string.ascii_lowercase
activeString = "" # userInput
# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.unicode.lower() in letters:
				activeString += event.unicode.lower() # adding char
				if len(activeString) != 1:
					activeString = activeString[:-1]

			if event.key == pygame.K_BACKSPACE and len(activeString) > 0:
				activeString = activeString[:-1] # deleting char

	screen.fill("wheat")

	surface1.drawSurface(screen)
	surface1.displayFont(activeString)
	pygame.display.flip()

pygame.quit()
