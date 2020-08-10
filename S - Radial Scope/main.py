import os
import pygame
import time
import random
import math

def setup(screen, etc):
    global xr,yr, xr2,yr2,x800, x20
    xr = etc.xres
    yr = etc.yres
    yr2 = yr*0.5
    xr2 = xr*0.5
    x800 = (800*xr)/1280
    x20 = (20*xr)/1280
    pass

def draw(screen, etc):
    global xr,yr, xr2,yr2,x800, x20
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 75) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    global xr,yr, xr2,yr2,x800, x20
    color = etc.color_picker(etc.knob4)
    R = int(etc.knob2*x800)
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  75.) * 6.28) + xr2
    y = R * math.sin((i /  75.) * 6.28) + yr2
    
    pygame.draw.line(screen, color, [xr2, yr2], [x, y], int(etc.knob1*x20)+1)
    pygame.draw.circle(screen,color,(int(x),int(y)),int(etc.knob3*x20), 0)
