import os
import pygame
import time
import random
import math

lx = 0
ly = 0

def setup(screen,etc) :
    pass

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 60) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    global lx, ly
    
    Rmod1 = ((etc.xres*400)/1280)
    Rmod2 = ((etc.xres*200)/1280)
    xhalf = (etc.xres/2)
    yhalf = (etc.yres/2)
    lwidth = ((20*etc.xres)/1280)
    crad = ((20*etc.xres)/1280)
    color = etc.color_picker(etc.knob4)
    R = etc.knob2*Rmod1-Rmod2
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  60.) * 6.28) + xhalf
    y = R * math.sin((i /  60.) * 6.28) + yhalf
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(etc.knob3*lwidth)+1)
    ly = y
    lx = x
    
    pygame.draw.circle(screen,color,[int(x), int(y)], int(etc.knob1 *crad), 0)
