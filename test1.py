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
		createFont = pygame.font.SysFont("Arial.ttf",30)
		renderFont = createFont.render(activeString, False, "black")
		self.setSurface.blit(renderFont, (4, 10))

	def displayHints(self, surface, answer, userInput):
		hints = ""

		for i in answer:
			if i in userInput:
				hints += i + " "  # Show letter if guessed
			else:
				hints += "_ " 

	
		createFont = pygame.font.SysFont("Arial.ttf",50)
		renderFont = createFont.render(hints, False, "black")
		surface.blit(renderFont, (self.x_pos, 210))

# SURFACE OBJECT
surface1 = displaySurface(20, 150, 200, 30, "white")

# WORDS
letters = string.ascii_lowercase
userInput = "" # userInput
answer = "basketball"

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.unicode.lower() in letters:
				userInput += event.unicode.lower() # adding char
				#if len(userInput) != 1:
					#userInput = userInput[:-1]

			if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
				userInput = userInput[:-1] # deleting char

	screen.fill("wheat")

	surface1.drawSurface(screen)
	surface1.displayFont(userInput)
	surface1.displayHints(screen, answer, userInput)

	pygame.display.flip()

pygame.quit()
