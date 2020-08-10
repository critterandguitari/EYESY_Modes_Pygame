import os
import pygame
import time
import random

def setup(screen, etc):
    pass

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 100) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :

    x0 = int(etc.knob2 * etc.yres)
    x1 = (int(etc.knob1 * etc.xres) ) + (etc.audio_in[i] / 64)
    circlespace = 12*etc.xres/1280
    circlebuff = 40*etc.xres/1280
    circlerad = etc.xres/100
    y = i * circlespace
    bw = random.randrange(0,255)
    color = etc.color_picker(etc.knob4)
    
    pygame.draw.circle(screen,color,(x1, y + circlebuff),int(etc.knob3 * circlerad), 0)
    pygame.draw.line(screen, color, [y + circlebuff, x0], [x1, y + circlebuff], 2)
