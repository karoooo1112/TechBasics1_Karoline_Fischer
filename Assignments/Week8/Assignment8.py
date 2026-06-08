import pygame 
import random 
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0,0,0) #black 

class Ghost: 
    def __init__(self, center_x, center_y, radius, speed, start_angle=0):
        img = pygame.image.load ("Ghost.png")
        self.img = pygame.transform.scale (img, (100,100))
        
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.speed = speed
        self.angle = start_angle

        self.pos_x = center_x + radius * math.cos(math.radians(self.angle))
        self.pos_y = center_y + radius * math.sin(math.radians(self.angle))
    

    def animate (self):
        self.angle += self.speed

        self.pos_x = self.center_x + self.radius * math.cos(math.radians(self.angle))
        self.pos_y = self.center_y + self.radius * math.sin(math.radians(self.angle)) 
        
    def draw (self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption ('Circle Animation')
clock = pygame.time.Clock()

ghosts = []

for i in range (5):
    ghost = Ghost (
        center_x=random.randint(200, 600), 
        center_y=random.randint(200, 600), 
        radius=random.randint(50, 250), 
        speed=random.uniform(0.5, 5.0), 
        start_angle=random.randint(0, 360)
    )
    ghosts.append(ghost)

flag = True
while flag:
    clock.tick(60)

    ghost.animate()

    screen.fill(BACKGROUND_COLOR)

    ghost.draw()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)

