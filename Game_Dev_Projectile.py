import pygame
import random
import os

width = 800
height = 600
fps = 30

#Colors
white = (255,255,255)
yellow = (255, 255, 0) 
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
        self.radius = 20
        print("Player Init")

        #pygame.draw.circle(self.image, white, self.rect.center, self
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = 0
        #self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            #bullets.add(bullet)
            #shoot_sound.play()
                
        
    def update(self):

        self.speedx = 0
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

        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx

        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0



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

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "bullet_img.gif"))
        self.image.set_colorkey(black)
        self.image.set_colorkey(yellow)

        
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

        hits = pygame.sprite.groupcollide(platinum, Bullet, True, True)
        for hit in hits:
            score += 50 - hit.radius
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
        

            
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
    #draw_text(screen, str(score), 18, width / 2, 10)
    #draw.shield_bar(screen, 5, 5, player.shield)
    #Flip after drawing
    pygame.display.flip()
    print("Mine!")
pygame.quit()

