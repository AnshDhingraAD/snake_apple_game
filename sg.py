import pygame
from pygame.locals import *
import time
import random

SIZE=40 #because the length of block is 40

class Apple:
    def __init__(self,parent_screen):
        self.image=pygame.image.load(r"C:\Users\DELL\Downloads\apple.jpg").convert()
        self.parent_screen=parent_screen
        self.x=SIZE*3
        self.y=SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))   
        pygame.display.flip()

    def move(self):
        self.x=random.randint(0,24)*SIZE
        self.y=random.randint(0,16)*SIZE

class Snake:
    def __init__(self,parent_screen,length):
        self.length=length
        self.parent_screen=parent_screen
        self.block=pygame.image.load(r"C:\Users\DELL\Downloads\block.jpg").convert() #to load the image and store it under block.
        self.x=[SIZE]*length #array of length of each segment of snake
        self.y=[SIZE]*length
        self.direction="down" 

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1) #to increase the size of the array as the collision occurs.

    def move_left(self):
        self.direction="left"
    def move_right(self):
        self.direction="right"
    def move_up(self):
        self.direction="up"
    def move_down(self):
        self.direction="down"

    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) #co-ordinates
        pygame.display.flip()

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction == "left":
            self.x[0]-=SIZE
        if self.direction == "right":
            self.x[0]+=SIZE
        if self.direction == "up":
            self.y[0]-=SIZE
        if self.direction == "down":
            self.y[0]+=SIZE
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface= pygame.display.set_mode((1000,700))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + SIZE) and (y1 >= y2 and y1 < y2 + SIZE):
            return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        
        #snake colliding with apple:
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        #snake colliding with itself:
        for i in range(3,self.snake.length):
            if(self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i])):
                

    def display_score(self):
        font=pygame.font.SysFont('Courier New',30,bold=True)
        score=font.render(f"Score: {self.snake.length*10}",True,(255,255,255))
        self.surface.blit(score,(800,10))

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_UP:
                        self.snake.move_up()
                    if event.key==K_DOWN:
                        self.snake.move_down()
                    if event.key==K_RIGHT:
                        self.snake.move_right()
                    if event.key==K_LEFT:
                        self.snake.move_left()
                elif event.type== QUIT:
                    running = False

            self.play()
            time.sleep(0.3)
            


if __name__ == "__main__":
    game=Game()
    game.run()

#event loop is used to run the window until users quit it,instead of using time of 5 seconds.

