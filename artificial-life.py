# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:28:33 2019

@author: myke
"""

import pygame, sys
from pygame.locals import *
import random

FPS = 30

BGCOLOR = (255, 255, 255)
GREEN   = (  0, 150,   0)
RED     = (150,   0,   0)

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

NUMINITIALFOOD = 10
RENEWFOODRATE = 10
RENEWFOODPERIOD = 240

class Life():
    def __init__(self):
        self.pos = (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT))
        self.vel = ( 1, 1)
        self.radius = 5
        print(self.pos)
    
    def step(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        if self.pos[0] >= WINDOWWIDTH or self.pos[0] <= 0:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] >= WINDOWHEIGHT or self.pos[1] <= 0:
            self.vel = (self.vel[0], -self.vel[1])
        print(self.pos)

class Food():
    def __init__(self):
        self.pos = (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT))
        self.radius = 2

def main():
    global fpsClock, displaySurf
    pygame.init()
    fpsClock = pygame.time.Clock()
    
    displaySurf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Artificial Life')
    
    setInitialCondicion()
    
    while True:
        timestep()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick()

def setInitialCondicion():
    global ecosystem, time, foodsystem
    time = 0
    somebody = Life()
    ecosystem = [somebody]
    foodsystem = []
    for i in range(NUMINITIALFOOD):
        newFood = Food()
        foodsystem.append(newFood)

def timestep():
    global time
    time += 1
    displaySurf.fill(BGCOLOR)
    for anybody in ecosystem:
        anybody.step()
        pygame.draw.circle(displaySurf, GREEN, anybody.pos, anybody.radius)
    for food in foodsystem:
        pygame.draw.circle(displaySurf, RED, food.pos, food.radius)

if __name__ == '__main__':
    main()