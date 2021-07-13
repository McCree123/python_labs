# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:30:34 2020

@author: OhThatGuy
"""

import sys, pygame
import math
from random import *
pygame.init()

gravity = 0.4

class Impulse():
    def __init__(self, angle, force):
        # convert angle to coordinats
        self.angle = angle
        self.force = force
        self.x = math.cos(angle) * self.force
        self.y = math.sin(angle) * self.force
        # 
    
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, weight, impulse):
        pygame.sprite.Sprite.__init__(self)
        self.weight = weight
        self.impulse = impulse
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = [self.impulse.x, self.impulse.y]
        print(self.speed[0], ' and ', self.speed[1])    
        
    def move(self):
        # Physic animation here: 
        if impulse.force > 0:
            self.impulse.force = self.impulse.force - 2
            s = 0
        if impulse.force < 0:
            impulse.force = 0
            print('commit: impulse force is empty')
        self.rect = self.rect.move([self.speed[0],self.speed[1]])
#        self.rect = self.rect.move([self.speed[0],self.speed[1]-(abs(self.speed[1]) * 0.1) - self.impulse.force * 0.05])
        # Gravity
        self.speed[1] = self.speed[1] + (gravity * weight)
        # Windage
  #      if self.speed[1] < 0:
  #          self.speed[1] = self.speed[1] + (abs(self.speed[1]) * 0.01)
        # Фиксация столкновения
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0] 
            self.speed[1] = self.speed[1] * 0.8
        if self.rect.top < 0:
            print('top hit')            
            self.speed[1] = -(self.speed[1] * 1.0)

            self.impulse.force = 0
        if self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
            self.impulse.force = self.impulse.force + 100
            print('bottom hit')
            # if ball touches botom border - we give power to his impulse
            # self.impulse.force =self.impulse.force + 10
                
        ######### commment and uncomment for logs ###########
        # print(self.impulse.force)                         
        print(self.speed[0], ' and ', self.speed[1])      
        # print(self.rect)                                    
        #####################################################

def animate(group):
    screen.fill([60,60,60])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
    if pygame.sprite.spritecollide(ball, group, False):
        ball.speed[0] = -ball.speed[0]
        ball.speed[1] = -ball.speed[1]
        print()
    group.add(ball)
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    
    # Window creating
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([60, 60, 60])
    # ball pict init
img_file = "ball.png"
    # Wha?
clock = pygame.time.Clock()
group = pygame.sprite.Group()

for row in range (0, 1):
    for column in range (0, 1):
        location = [column * 180 + 100, row * 180 + 100]
        # speed = [choice([-2, 6]), choice([-10, 5])]
        weight = 1
        angle = 180
        force = 10
        impulse = Impulse(angle, force)
        ball = MyBallClass(img_file, location, weight, impulse)
        group.add(ball) #adding ball into group
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                frame_rate = clock.get_fps()
                print ("frame rate = ", frame_rate)
        animate(group)
        clock.tick(30)
pygame.quit() 