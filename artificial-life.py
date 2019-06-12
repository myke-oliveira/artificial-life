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

NUMINITIALFOOD = 3000
RENEWFOODRATE = 10000
NEWFOODPERPERIOD = 10

REPRODUTIVEVOL = 400

class Life():
    def __init__(self):
        self.pos = (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT))
        self.vel = (random.random(), random.random())
        self.vol = 125
    
    def makeChild(self):
        child = Life()
        child.pos = self.pos
        child.vel = (random.random(), random.random())
        child.vol = self.vol/2
        self.vol /= 2
        return child
    
    def getPos(self):
        return(int(self.pos[0]), int(self.pos[1]))

    def getRadius(self):
        return int(self.vol ** (1/3))
        
    def getVol(self):
        return self.vol
    
    def step(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])
        if self.pos[0] >= WINDOWWIDTH or self.pos[0] <= 0:
            self.vel = (-self.vel[0], self.vel[1])
        if self.pos[1] >= WINDOWHEIGHT or self.pos[1] <= 0:
            self.vel = (self.vel[0], -self.vel[1])
        print(self.pos)
        
    def eat(self, food):
        foodsystem.remove(food)
        self.vol += 30


class Food():
    def __init__(self):
        self.pos = (random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT))
        self.vol = 8
    
    def getPos(self):
        return(int(self.pos[0]), int(self.pos[1]))
    
    def getRadius(self):
        return int(self.vol ** (1/3))

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
    global ecosystem, time, foodsystem, foodPeriod
    time = 0
    somebody = Life()
    ecosystem = [somebody]
    foodsystem = []
    growFood(NUMINITIALFOOD)
    foodPeriod = RENEWFOODPERIOD
    

def growFood(num):
    for i in range(num):
        newFood = Food()
        foodsystem.append(newFood)

def timestep():
    global time, foodPeriod
    time += 1
    foodPeriod -= 1
    displaySurf.fill(BGCOLOR)
    for anybody in ecosystem:
        anybody.step()
        pygame.draw.circle(displaySurf, GREEN, anybody.getPos(), anybody.getRadius())
    for food in foodsystem:
        pygame.draw.circle(displaySurf, RED, food.getPos(), food.getRadius())
    for anybody in ecosystem:
        for food in foodsystem:
            if meet(anybody, food):
                anybody.eat(food)
        if anybody.getVol() > REPRODUTIVEVOL:
            ecosystem.append(anybody.makeChild())
    if foodPeriod <= 0:
        growFood(NEWFOODPERPERIOD)
        foodPeriod = RENEWFOODRATE

def meet(o1, o2):
    return (o1.getRadius() + o2.getRadius())**2 >= (o1.pos[0] - o2.pos[0])**2 + (o1.pos[1] - o2.pos[1])**2

if __name__ == '__main__':
    main()