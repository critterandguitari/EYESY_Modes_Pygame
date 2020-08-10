import os
import pygame
import time
import math

def setup(screen, etc):
    global last_point, first_point, xr,yr,x200, x110,a75,x15
    xr = etc.xres
    yr = etc.yres
    last_point = [0, (yr/2)]
    first_point = []
    x200 = int((200*xr)/1280)
    x110 = int((25*xr)/1280)
    a75 = int((500*xr)/1280)
    x15 = int((xr/50)+1)
    pass

def draw(screen, etc):
    global last_point, first_point, xr,yr,x200, x110, a75,x15
    etc.color_picker_bg(etc.knob5)    
    #Lines
    for i in range(0, 50) :
        lineseg(screen, etc, i)

def lineseg(screen, etc, i):
    global last_point, first_point, xr,yr,x200, x110, a75,x15
    
    linewidth = int(etc.knob1*x110)+1
    y1 = int((etc.knob2 * yr) + ((etc.audio_in[i]* 0.00003058)* a75))
    x = i * x15
    color = etc.color_picker(etc.knob4)

    if i == 0 : 
        last_point = [(x110*-1), (yr/2)]
    else :
        last_point = last_point
    
    pygame.draw.line(screen, (int(etc.knob3*255),int(etc.knob3*255),int(etc.knob3*255)), [last_point[0]-150*etc.knob3 , last_point[1]-150*etc.knob3], [x-150*etc.knob3 , y1-150*etc.knob3], linewidth)
    pygame.draw.line(screen, color, last_point, [x , y1], linewidth)
    last_point = [x , y1]
