import pygame

# SCREEN
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Hang Man")

# MAIN LOOP
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("wheat")

    pygame.display.flip()

pygame.quit()
