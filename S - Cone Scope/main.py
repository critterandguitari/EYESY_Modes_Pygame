import os
import pygame
import time
import random

def setup(screen, etc):
    pass

note_down = False

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 50) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    
    color = etc.color_picker(etc.knob4)
    x0 = (int(etc.knob1*etc.xres))
    soundwidth = ((etc.audio_in[i] * etc.xres)/(1280*35))
    x1 = x0 + soundwidth
    linespacing = etc.yres/50#(7*etc.yres)/720
    y = i * linespacing
    newy = (575*etc.yres/720-(int(etc.knob2*1150*etc.yres/720)))
    linewratio = 20*etc.xres/1280
    linewidth = int(etc.knob3*linewratio)
  
    pygame.draw.line(screen, color, [x0, y +i], [x1, y+i+newy], 1+linewidth)
