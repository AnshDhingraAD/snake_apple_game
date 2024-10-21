import pygame
#import time
from pygame.locals import *

def draw_block():        #funct to display the block
   # surface.fill((110,110,5))        # Clear the surface (to avoid image trails)
    surface.blit(block,(block_x,block_y))   
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface= pygame.display.set_mode((1000,500))
    surface.fill((110,110,5))

    block=pygame.image.load(r"C:\Users\DELL\Downloads\block.jpg").convert() #to load the image and store it under block.
    block_x=100
    block_y=100
    surface.blit(block,(block_x,block_y)) #co-ordinates

    pygame.display.flip() #to update the changes to the display

    #time.sleep(5)

    #event loop is used to run the window until users quit it,instead of using time of 5 seconds.

    running = True

    while running:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    block_y-=10
                    draw_block()
                if event.key==K_DOWN:
                    block_y+=10
                    draw_block()
                if event.key==K_RIGHT:
                    block_x+=10
                    draw_block()
                if event.key==K_LEFT:
                    block_x-=10
                    draw_block()
            elif event.type== QUIT:
                running = False
            