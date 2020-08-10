import os
import pygame
import time
import random
import math
import pygame.gfxdraw

def setup(screen, etc):
    pass

note_down = False
lx = 0
ly = 0

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 50) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    global lx, ly
    
    xr = etc.xres
    x200 = ((200*xr)/1280)
    x640 = ((640*xr)/1280)
    x960 = ((960*xr)/1280)
    x800 = ((800*xr)/1280)
    xran = ((78*xr)/1280)
    yr = etc.yres
    y260 = ((260*yr)/720)
    color = etc.color_picker(etc.knob4)
    R = int(etc.knob1 * x800)
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  50.) * 6.28) + x640
    y = R * math.sin((i /  50.) * 6.28) + y260
    
    if ((i % 2)) :
        pygame.gfxdraw.filled_trigon(screen, int(x), int(y), int(x) + int(etc.knob2*x200) + random.randrange(0,xran), int(y) + int(etc.knob2*x200), int(x) - int(etc.knob3*x200), int(y) + int(etc.knob3*x200), color)
    else :
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.gfxdraw.trigon(screen, int(x), int(y), int(x) + int(etc.knob2*x200) + random.randrange(0,xran), int(y) + int(etc.knob2*x200), int(x) - int(etc.knob3*x200), int(y) + int(etc.knob3*x200), color)
