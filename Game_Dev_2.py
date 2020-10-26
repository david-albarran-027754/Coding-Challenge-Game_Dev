import pygame
import random

width = 800
height = 600
FPS = 30

#Colors
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > width:
            self.rect.right = 0

#Initialize Variables
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Our Game")
clock = pygame.time.Clock()

#Sprite Group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game Loops
#  Process Events
#  Update
#  Draw
running = True
while running:

    clock.tick(FPS)

    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw
    screen.fill(black)
    all_sprites.draw(screen)

    #Flip after Drawing
    pygame.display.flip()

pygame.quit()
