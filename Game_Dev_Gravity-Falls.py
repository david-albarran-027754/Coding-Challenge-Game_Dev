import pygame
import random
import os

width = 800
height = 600
fps = 30
ground = height - 10
slow = 3
fast = 8

#Constants - Physics
player_acc = 0.9
player_friction = -0.12
player_grav = 0.4
vec = pygame.math.Vector2

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
        
        self.pos = vec(10, ground - 60)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
        print("Player Init")
    def update(self):

        self.acc = vec(0, player_grav)

        #Returns a list, keystate, of all pressed keys
        keystate = pygame.key.get_pressed()

        #Checks to see which keys were in the list(a.k.a pressed)
        if keystate[pygame.K_RIGHT]:
            self.acc.x += player_acc
            print("Right")
        if keystate[pygame.K_LEFT]:
            self.acc.x += -player_acc
            print("Left")
        if keystate[pygame.K_UP]:
            self.acc.y += -2
            print("Up")
        if keystate[pygame.K_DOWN]:
            self.acc.y += 2
            print("Down")
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.vel.y = -20

        #Apply friction in the x direction
        self.acc.x += self.vel.x * player_friction

        #Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #wrap around the screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width

        #simulate the ground
        if self.pos.y > ground:
            self.pos.y = ground + 1
            self.vel.y = 0

        if self.pos.y < 90:
            self.pos.y = 90 + 1
            self.vel.y = 0

        #set the new player pos based on previous code
        self.rect.midbottom = self.pos

        
            
        

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
            self.rect.left = width



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
    
    #Updates
    all_sprites.update()
    
    #Draw
    
    screen.fill(green)
    all_sprites.draw(screen)
    
    #Flip after drawing
    pygame.display.flip()
    
pygame.quit()

