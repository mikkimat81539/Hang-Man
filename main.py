import pygame
from gameEnviroment import displayFonts

pygame.init()

# SCREEN
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hang Man")

# WORD
answer = "basketball"

# DISPLAY HINTS
hints = displayFonts(50, 300, "black", 90)

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			print(mouse)

	screen.fill("wheat")
	
	hints.drawText(screen, answer)

	pygame.display.flip()

pygame.quit()
