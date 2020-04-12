

import pygame, sys, os


SCREEN_DIMENSIONS = screenX, screenY = (720, 480)
BG_COLOR = (0,0,0)
PADDLE_COLOR = (255, 147, 79)
BALL_COLOR = (34, 170, 161)
RADIUS = 10
BRICK_COLOR_1 = (178,34,34)


pygame.init()
pygame.display.set_caption("Brick Breaker")
screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)


class Paddle:
	"""docstring for Paddle"""
	def __init__(self, X, Y, velX, width, height):
		self.x = X
		self.y = Y
		self.velX = velX
		self.width = width
		self.height = height
		self.paddleRect = pygame.draw.rect(screen, PADDLE_COLOR, (int(self.x), int(self.y), int(self.width), int(self.height)))
		# self.isLocked = False

	def draw(self):
		self.paddleRect = pygame.draw.rect(screen, PADDLE_COLOR, (int(self.x), int(self.y), int(self.width), int(self.height)))

	def update_velocity(self, direction):

		# if self.isLocked:
		# 	return

		if direction == "LEFT":
			self.x -= self.velX
		elif direction == "RIGHT":
			self.x += self.velX
		else:
			return

		if self.x < 0:
			self.x = 0
		if self.x + self.width > screenX:
			self.x = screenX - self.width



playerPaddle = Paddle(	X = screenX//2 - screenX*0.2//2, 
						Y = 0.95 * screenY, 
						velX = 15,
						width = screenX*0.2,
						height = screenY*0.02
					)


class Ball:
	"""docstring for Ball"""
	def __init__(self, x, y, velX, velY, radius):
		self.x = x
		self.y = y
		self.velX = velX
		self.velY = velY
		self.radius = radius
		self.currVelX = self.velX
		self.currVelY = self.velY
		self.bodyRect = pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), int(self.radius))

	def draw(self):
		self.bodyRect = pygame.draw.circle(screen, BALL_COLOR, (int(self.x), int(self.y)), int(self.radius))

	def update_position(self):

		if self.x + self.radius > screenX:
			self.currVelX = -self.velX

		if self.x - self.radius < 0:
			self.currVelX = self.velX

		if self.y + self.radius > screenY or self.bodyRect.colliderect(playerPaddle.paddleRect) or self.bodyRect.colliderect(brick.brickRect):
			self.currVelY = -self.velY

		if self.y - self.radius < 0:
			self.currVelY = self.velY


		self.x += self.currVelX
		self.y += self.currVelY

	def set_velocity(self, velX, velY):
		self.velX = velX
		self.velY = velY
		self.currVelX = self.velX
		self.currVelY = self.velY


gameBall = Ball(playerPaddle.x + playerPaddle.width//2, playerPaddle.y - RADIUS, 0, 0, RADIUS)

class Brick(pygame.sprite.Sprite):
	def __init__(self, X, Y,width, height):
		pygame.sprite.Sprite.__init__(self)
		self.x = X
		self.y = Y
		self.width = width
		self.height = height
		self.brickRect = pygame.draw.rect(screen, BRICK_COLOR_1, (int(self.x), int(self.y), int(self.width), int(self.height)))
		# self.isLocked = False

	def draw(self):
		self.paddleRect = pygame.draw.rect(screen, BRICK_COLOR_1, (int(self.x), int(self.y), int(self.width), int(self.height)))


brick = Brick(	X = screenX//2 - 50//2,
				Y = 0.2 * screenY,
				width = 50,
				height = 20
			)

# bricks = pygame.sprite.Group()
# bricks.add(Brick(10,10,50,25))



def playGame():

	#playerPaddle.isLocked = True

	while True:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keyPressed = pygame.key.get_pressed()

		if keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]:
			playerPaddle.update_velocity("LEFT")
		elif keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]:
			playerPaddle.update_velocity("RIGHT")
		elif keyPressed[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
				# if event.key == pygame.K_SPACE:
				# 	playerPaddle.isLocked = False
		gameBall.update_position()
		screen.fill(BG_COLOR)
		gameBall.draw()
		playerPaddle.draw()
		brick.draw()
		pygame.display.update()
		clock.tick(60)

def main():
	while True:
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keyPressed = pygame.key.get_pressed()

		if keyPressed[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()

		if keyPressed[pygame.K_SPACE]:
			gameBall.set_velocity(8, 8)
			playGame()

		gameBall.update_position()
		screen.fill(BG_COLOR)
		gameBall.draw()
		playerPaddle.draw()
		brick.draw()
		pygame.display.update()
		clock.tick(60)


if __name__ == '__main__':
	main()
