import pygame
import random
import os

width = 800
height = 600
fps = 30

#Colors
white = (255,255,255)
black = (0, 0, 0)
green = (0, 255, 0)

#Asset Folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.y_speed = 8
        print("Player Init")
    def update(self):

        #Returns a list, keystate, of all pressed keys
        keystate = pygame.key.get_pressed()

        #Checks to see which keys were in the list(a.k.a pressed)
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
            print("Right")
        if keystate[pygame.K_LEFT]:
            self.rect.x += -5
            print("Left")
        if keystate[pygame.K_UP]:
            self.rect.y += -5
            print("Up")
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
            print("Down")
        print("Player Update")

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "sandwich.png")).convert()
        self.image = pygame.transform.scale(self.image, (300, 175))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 460
        


    def update(self):
        self.rect.x += -10

        if self.rect.right < 0:
            self.rect.left = 800

#Initialize Variables
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Our Game")

clock = pygame.time.Clock()
print("Initial Variables")
#Sprite Group
all_sprites = pygame.sprite.Group()
player = Player()
platinum = Platform()
all_sprites.add(player)
all_sprites.add(platinum)
print("Sprite Group")

#Game Loops:
#Process Events
#Update
#Draw
running = True
while running:

    clock.tick(fps)

    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(".")
    #Updates
    all_sprites.update()

    #Draw
    print("Draw1")
    screen.fill(green)
    all_sprites.draw(screen)
    print("Draw2")
    #Flip after drawing
    pygame.display.flip()
    print("..")
pygame.quit()

