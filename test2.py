import pygame, string

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 300))

# CLASS
class DisplaySurface:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.setSurface = pygame.Surface((self.width, self.height))

	def drawDisplay(self, surface):
		surface.blit(self.setSurface, (self.x_pos, self.y_pos))
		self.setSurface.fill(self.color)
	
	def createText(self, userInput):
		createFont = pygame.font.SysFont("Arial", 30)
		renderFont = createFont.render(userInput, False, "black")
		self.setSurface.blit(renderFont, (5, 10))

# HINT FUNCTION
answer = "apple"

hint = "_ " * len(answer)

def displayHint(answer, hint):
	hintJoined = " ".join(hint)
	createFont = pygame.font.SysFont("Arial", 50)
	renderFont = createFont.render(hintJoined, False, "black")
	screen.blit(renderFont, (10, 100))
	return hint

# OBJECT
surface1 = DisplaySurface(10, 90, 30, 50, "white")
userInput = ""
cursor_pos = 0

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
				userInput = userInput[:-1]

			elif event.unicode in string.ascii_lowercase:
				userInput += event.unicode

				if userInput[-1] == answer[surface1.x_pos]:
					hint[surface1.x_pos] = userInput[-1]
					surface1 += 1

				if len(userInput) != 1:	
					userInput = userInput[:-1]

				#userInput = "" # Reset user input after a guess

	screen.fill("wheat")

	surface1.drawDisplay(screen)
	surface1.createText(userInput)
	displayHint(answer, hint)

	pygame.display.flip()

pygame.quit()
