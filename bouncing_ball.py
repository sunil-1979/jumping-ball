# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:51:36 2022

@author: sunil
"""

import pygame

pygame.init()
timer=pygame.time.Clock()

RED = (255,0,0)
green=(0,255,0)


height=600
width=350
x=350
y=15
dx=0
dy=2

x1=400
y1=335
dx1=0
dy1=2
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Bouncing Balls")

bg=pygame.image.load("bg1.jpg").convert()


carryOn = True



while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    # first ball movement
    x+=dx
    y+=dy
    
    # check boundary of canvas
    if y<0 or y>width-15:
        dy*=-1
        if x<0 or x>height -15:
            dx*=-1
            
    # second ball movement
    
    x1+=dx1
    y1+=dy1
     
    # check boundry for second ball
    if y1<0 or y1>width-15:
        dy1*=-1
        if x1<0 or x1>height-15:
            dx1*=-1
        
    screen.blit(bg,(0,0))
    
    pygame.draw.circle(screen,green,(x,y),15)
    pygame.draw.circle(screen,RED,(x1,y1),15)
    timer.tick(300)
    pygame.display.update()       
pygame.quit( )
    
            
