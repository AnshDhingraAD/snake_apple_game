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
        pygame.display.set_caption("SNAKE AND APPLE GAME")
        pygame.mixer.init()
        self.play_bgm()
        self.surface= pygame.display.set_mode((1000,680))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        self.apple=Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + SIZE) and (y1 >= y2 and y1 < y2 + SIZE):
            return True
        return False

    def play_bgm(self):
        pygame.mixer.music.load(r"C:\Users\DELL\Downloads\Walen - Gameboy (freetouse.com).mp3")
        pygame.mixer.music.play()

    def background(self):
        bg=pygame.image.load(r"C:\Users\DELL\Downloads\background.jpg")
        self.surface.blit(bg,(0,0))  

    def play(self):
        self.background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        
        #snake colliding with apple:
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            sound=pygame.mixer.Sound(r"C:\Users\DELL\Downloads\cartoon-bite-fx_A#_minor.wav")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()

        #snake colliding with itself:
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                sound=pygame.mixer.Sound(r"C:\Users\DELL\Downloads\crash-77686.mp3")
                pygame.mixer.Sound.play(sound)
                raise "GAME OVER!"

        #snake colliding with walls:
        if self.snake.x[0]<0 or self.snake.x[0]>=1000 or self.snake.y[0]<0 or self.snake.y[0]>=680:
            sound=pygame.mixer.Sound(r"C:\Users\DELL\Downloads\crash-77686.mp3")
            pygame.mixer.Sound.play(sound)
            raise "GAME OVER!"



    def show_game_over(self):
        self.background()
        font=pygame.font.SysFont('Courier New',30,bold=True)
        line1=font.render(f"GAME IS OVER! YOUR SCORE IS {self.snake.length*10}",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        line2=font.render(f"TO PLAY AGAIN PRESS ENTER.TO EXIT PRESS ESCAPE!",True,(255,255,255))
        self.surface.blit(line2,(100,350))
        pygame.display.flip()
        pygame.mixer.music.pause()
        

    def display_score(self):
        font=pygame.font.SysFont('Courier New',30,bold=True)
        score=font.render(f"Score: {self.snake.length*10}",True,(255,255,255))
        self.surface.blit(score,(800,10))

    def reset(self):
        self.snake = Snake(self.surface,1)
        self.apple=Apple(self.surface)

    def run(self):
        running = True
        pause=False

        while running:
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_RETURN:
                        pause=False
                        pygame.mixer.music.unpause()
                    if not pause:
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
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause=True
                self.reset()
            
            time.sleep(0.3)
            


if __name__ == "__main__":
    game=Game()
    game.run()

#event loop is used to run the window until users quit it,instead of using time of 5 seconds.

