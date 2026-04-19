import pygame, string

pygame.init()

# SCREEN
screen_w = 500
screen_h = 300

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Hang Man")

# HINTS
answer = "basketball".upper()
hints = ["_"] * len(answer)
userInput = ""
guessed_letter = set()
showMsg = False

def displayHints(surface, hints):
	joinHints = " ".join(hints)
	
	cursorPos_x = screen_w // 4
	cursorPos_y = screen_h // 2

	createFont = pygame.font.SysFont("Arial.ttf", 50)
	renderFont = createFont.render(joinHints, False, "black")
	surface.blit(renderFont, (cursorPos_x, cursorPos_y))

def displayResponse(surface, screen_w, screen_h):
	response = "Letter already selected"

	cursorPos_x = screen_w // 4
	cursorPos_y = screen_h // 2

	createFont = pygame.font.SysFont("Arial.ttf", 35)
	renderFont = createFont.render(response, True, "black")
	surface.blit(renderFont, (cursorPos_x , 20))

	return response


def displayAnswers(hints, answer, userInput):
	for i in range(len(answer)):
		if answer[i] in userInput:
			hints[i] = answer[i]
			joinHints = "".join(hints)
# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			showMsg = False

			if event.unicode in string.ascii_letters:
				letter = event.unicode.upper()
			
				if letter not in guessed_letter:
					userInput += letter
					guessed_letter.add(letter)
					showMsg = False
	
				else:
					showMsg = True

			if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
				userInput = userInput[:-1]
	
	screen.fill("wheat")
	
	if showMsg:
		displayResponse(screen, screen_w, screen_h)

	displayHints(screen, hints)
	displayAnswers(hints, answer, userInput)
	
	pygame.display.flip()

pygame.quit()
