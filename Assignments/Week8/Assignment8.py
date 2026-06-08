import pygame
import random
import math

#seems to be working with those screen sizes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# random background color
# also there's no command to directly get a random color --> has to be done through random.randint
background_color = (random.randint(0, 255), random.randint (0, 255), random.randint (0, 255))  # black


class Ghost:
    def __init__(self, center_x, center_y, radius, speed, start_angle=0):
        img = pygame.image.load("ghost.png")
        self.img = pygame.transform.scale(img, (100, 100))

        # every parameter in the __init__ has to be listed here with self
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.speed = speed
        self.angle = start_angle

        # I can't do math, so this was done by ChatAI Anthropic Claude Sonnet 4.6
        self.pos_x = center_x + radius * math.cos(math.radians(self.angle))
        self.pos_y = center_y + radius * math.sin(math.radians(self.angle))

    #jap, this is the movement of the ghost
    def animate(self):
        self.angle += self.speed

        self.pos_x = self.center_x + self.radius * math.cos(math.radians(self.angle))
        self.pos_y = self.center_y + self.radius * math.sin(math.radians(self.angle))

    # this draws over the last shown picture --> without this the ghost would just replicate and leave a trail
    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

# initiating the pygame engines  or sth
pygame.init()

# setting the screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Circle Animation')
clock = pygame.time.Clock()

# list for the different ghosts, that gets filled by the range statement below
# also the random element is immediately fulfilled by this
ghosts = []

for i in range(5):
    ghost = Ghost(
        center_x=random.randint(100, 400),
        center_y=random.randint(100, 400),
        radius=random.randint(50, 250),
        speed=random.uniform(0.5, 5.0),
        start_angle=random.randint(0, 360)
    )
    ghosts.append(ghost)

# as long as flag is true --> game will run
flag = True
while flag:
    clock.tick(60)

    ghost.animate()

    screen.fill(background_color)

    ghost.draw()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)
