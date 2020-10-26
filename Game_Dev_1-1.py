import pygame
import random

width = 360
height = 480
fps = 30

#Color
white = (255,255,255)
black = (0,0,0)
red = (255, 0,0)
green = (0,255,0)
blue = (0,0,255)



#Variables

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("insert creative name.exe")

clock = pygame.time.Clock()

print("28%")

#Game Loops
#  Process events
#  Update
#  Draw
running = True
while running:

    #Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #Update

    #Draw
    screen.fill(green)

    #Flip after Drawing
    pygame.display.flip()

    
pygame.quit()
