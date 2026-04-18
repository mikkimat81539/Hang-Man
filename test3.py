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
guessed_letter = []

# if len(answer) > 5 than x_pos and y_pos need to be adjusted accordingly

def displayHints(surface, hints):
	joinHints = " ".join(hints)
	
	cursorPos_x = screen_w // 4
	cursorPos_y = screen_h // 2

	createFont = pygame.font.SysFont("Arial.ttf", 50)
	renderFont = createFont.render(joinHints, False, "black")
	surface.blit(renderFont, (cursorPos_x, cursorPos_y))

def displayGuessed(surface):
	response = "Letter already selected"

	cursorPos_x = screen_w // 4
	cursorPos_y = screen_h // 2

	createFont = pygame.font.SysFont("Arial.ttf", 35)
	renderFont = createFont.render(response, True, "black")
	surface.blit(renderFont, (cursorPos_x , 20))


def displayAnswers(hints, answer, userInput):
	correctLetter = False

	#if userInput in guessed_letter:
		#displayGuessed(screen)

	for i in range(len(answer)):
		if answer[i] in userInput:
			hints[i] = answer[i]
			joinHints = "".join(hints)
			correctLetter = True

	if correctLetter:
		guessed_letter.append(userInput)

		if userInput in guessed_letter:
			displayGuessed(screen)

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.unicode in string.ascii_letters:
				userInput += event.unicode.upper() 
				#if len(userInput) != 1:
					#userInput = userInput[:-1]

			if event.key == pygame.K_BACKSPACE and len(userInput) > 0:
				userInput = userInput[:-1]

	screen.fill("wheat")

	displayHints(screen, hints)
	displayAnswers(hints, answer, userInput)
	
	pygame.display.flip()

pygame.quit()
