from pickle import FALSE
import pygame
import random
from enum import Enum
from collections import namedtuple
import time
import numpy as np


#TODO 1 - Make Chaser actually chase - use x and y positions and create actually collision - within BLOCKSIZES

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 10

class newGame:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Chaser')
        self.clock = pygame.time.Clock()
        self.direction = Direction.DOWN
        self.reset()
        

    def reset(self):
        self.player = Point(self.w/2, self.h/2)
        self.chaser = None
        self.create_Chaser()
        self.score = 0
        self.food = None
        self._place_food()
        self.do_x = False
        self.do_y = False


    def create_Chaser(self):
        x = random.randint(0, (self.w-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.chaser = Point(x, y)


    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        
        
    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. move
        self._move(self.direction) # update the head
        self._move_chaser()
        game_over = False
        # 3. check if game over
        if self._is_collision():
            game_over = True
            return game_over
                    
        if self.player == self.food:
            self.score += 1
            self._place_food()
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

    
    def _is_collision(self):
        # hits boundary
        if self.player.x > self.w - BLOCK_SIZE or self.player.x < 0 or self.player.y > self.h - BLOCK_SIZE or self.player.y < 0:
            return True
        # hits itself
        if self.chaser_hits():
            return True
        return False
        
        
        
    def _update_ui(self):
        self.display.fill(BLACK)
        
        pygame.draw.rect(self.display, BLUE1, pygame.Rect(self.player.x, self.player.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.chaser.x, self.chaser.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        

    def _move(self, direction):
        x = self.player.x
        y = self.player.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.player = Point(x, y)
            

    
    def _move_chaser(self):
        x = self.chaser.x
        direction = 0
        y = self.chaser.y
        if np.abs(self.chaser.x - self.player.x) > np.abs(self.chaser.y - self.player.y):
            self.do_x = True
        elif np.abs(self.chaser.y - self.player.y) > np.abs(self.chaser.x - self.player.x):
            self.do_y = True
        if self.do_x: 
            if self.chaser.x - self.player.x < 0:
                direction = 1 # right
            else:
                direction = 2 #left 
        if self.do_y:
            if self.chaser.y - self.player.y < 0:
                direction = 3 #up
            else:
                direction = 4 #down
        
        if direction == 1:
            x += 10
        elif direction == 2:
            x -= 10
        elif direction == 3:
            y += 10
        else:
            y -= 10
        


        self.chaser = Point(x, y)
            



    def chaser_hits(self):
        if np.abs(self.chaser.x - self.player.x) == BLOCK_SIZE and np.abs(self.chaser.y - self.player.y) == BLOCK_SIZE:
            print("Chaser hit")
            return True

if __name__ == '__main__':
    game = newGame()
    
    # game loop
    while True:
        time.sleep(0.3)
        game_over = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', game.score)
        
        
    pygame.quit()
