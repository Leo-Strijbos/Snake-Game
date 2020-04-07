import pygame
import time
import random

coords = []
eaten_apple = True
apples = 0
x_loc = "empty placeholder"
y_loc = "empty placeholder"
snake_length = 1
class head:
	def __init__(self, x_coord, y_coord, dirnx, dirny):
		global coords
		self.x_coord = x_coord
		self.y_coord = y_coord
		coords.append([self.x_coord, self.y_coord])
		self.dirnx = dirnx
		self.dirny = dirny

	def pos(self):
		global coords
		if (self.dirnx == 1) and (self.x_coord < 320):
			self.x_coord += 20
			coords.append([self.x_coord, self.y_coord])
		elif (self.dirnx == -1) and (self.x_coord > 0):
			self.x_coord -= 20
			coords.append([self.x_coord, self.y_coord])

		elif (self.dirny == 1) and (self.y_coord < 320):
			self.y_coord += 20
			coords.append([self.x_coord, self.y_coord])
		elif (self.dirny == -1) and (self.y_coord > 0):
			self.y_coord -= 20
			coords.append([self.x_coord, self.y_coord])

		return(self.x_coord, self.y_coord)

	def recent(self):
		return coords

class body:
	def __init__(self, coordinates):
		self.coordinates = coordinates

	def draw(self, order):
		self.order = order
		pygame.draw.rect(screen, blue, (self.coordinates[-(self.order)][0], self.coordinates[-(self.order)][1], 20, 20))	

class apple:
	def __init__(self, x_c, y_c):
		self.x_c = x_c
		self.y_c = y_c


	def spawn(self):
		red = (255, 0, 0)
		pygame.draw.rect(screen, red, (self.x_c, self.y_c, 20, 20))	


class snake:
	def __init__(self, recent_coords):
		self.recent_coords = recent_coords

		blue = (3, 44, 252)
	
	def new_head(self, head_x, head_y):
		self.head_x = head_x
		self.head_y = head_y
		pygame.draw.rect(screen, blue, (self.head_x, self.head_y, 20, 20))

	


def main():
	global screen, blue, red, eaten_apple, x_loc, y_loc, snake_length, apples
	background_colour = (0, 0, 0)
	blue = (3, 44, 252)
	
	(width, height) = (340, 340)

	screen = pygame.display.set_mode((width, height))
	

	screen.fill(background_colour)
	pygame.display.flip()
	pygame.display.set_caption("Snake")

	dirnx = 1
	dirny = 0
	x = 0
	y = 0
	

	running = True
	light_green = (0,255,0)
	dark_green = (0, 175, 0)

	while running:
		for i in range(1, 18):
			for l in range(1, 18):
				if (i % 2 == True and l % 2 == False) or (i % 2 == False and l % 2 == True):
					pygame.draw.rect(screen, dark_green, ((i - 1) * 20,(l - 1) * 20, 20, 20))
				else:
					pygame.draw.rect(screen, light_green, ((i - 1) * 20,(l - 1) * 20, 20, 20))
		time.sleep(0.2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			keys = pygame.key.get_pressed()
			if keys[pygame.K_UP]:
				dirnx = 0
				dirny = -1
				print("Up")
			elif keys[pygame.K_DOWN]:
				dirnx = 0
				dirny = 1
				print("Down")
			elif keys[pygame.K_LEFT]:
				dirnx = -1
				dirny = 0
				print("Left")
			elif keys[pygame.K_RIGHT]:
				dirnx = 1
				dirny = 0
				print("Right")
			

		

		h = head(x, y, dirnx, dirny)
		(x, y) = h.pos()
		coords = h.recent()

		s = snake(coords)
		s.new_head(x, y)

		b = body(coords)
		for m in range(snake_length):
				b.draw(m + 2)

	
		if eaten_apple == True:
			rand1 = random.randint(0, 16)
			rand2 = random.randint(0, 16)

			x_loc = rand1 * 20
			y_loc = rand2 * 20

			a = apple(x_loc, y_loc)
			a.spawn()
			eaten_apple = False
		
		else:
			a = apple(x_loc, y_loc)
			a.spawn()

		if (x == x_loc) and (y == y_loc):
			eaten_apple = True
			snake_length += 2
			apples += 1
			print("Apple has been eaten!")

			b.draw(snake_length)
		else:
			eaten_apple = False


		pygame.display.flip()



main()
