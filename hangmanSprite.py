import pygame

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Sprite Test")

# SPRITES
class HangMan:
	def __init__(self, x_pos, y_pos, width, height, color, filename):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.setSurface = pygame.Surface((self.width, self.height))
		self.filename = filename
		#self.image = pygame.image.load(filename).convert_alpha()
	
	def drawSprite(self, surface):
		surface.blit(self.setSurface, (self.x_pos, self.y_pos))
		self.setSurface.fill(self.color)
		self.image = pygame.image.load(self.filename).convert_alpha()
		self.setSurface.blit(self.image, (self.x_pos, self.y_pos))

spriteList = ['assets/head.png', 'assets/body.png','assets/leftArm.png',
	'assets/rightArm.png','assets/leftLeg.png','assets/rightLeg.png']

sprite_pos = 0
sprites = HangMan(10, 10, 200, 200, "wheat", spriteList[sprite_pos])

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				sprite_pos += 1

				if sprite_pos >= len(spriteList):
					sprite_pos = 0

				sprites.filename = spriteList[sprite_pos]

	screen.fill("wheat")

	sprites.drawSprite(screen)

	pygame.display.flip()

pygame.quit()
