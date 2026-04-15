import pygame
from gameEnviroment import displayHints

pygame.init()

# SCREEN
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hang Man")

# WORD
answer = "apple"

# DISPLAY HINTS
hints = displayHints(300, 100, "black", 3)

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("wheat")
	
	hints.drawLines(screen)	

	pygame.display.flip()

pygame.quit()
