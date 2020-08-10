import os
import pygame
import time
import random
import glob

last_point = []

def setup(screen, etc):
    global images, xr,yr, last_point
    xr = etc.xres
    yr = etc.yres
    last_point = [0, (yr/2)]

def draw(screen, etc):
    global last_point, xr,yr
    etc.color_picker_bg(etc.knob5)    
    for i in range(0, 50) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point
    
    xoffset = int(xr/48)
    x19 = (10*xr)/1280
    y0 = screen.get_height() // 2
    y1 = int((screen.get_height() // 2) + ((etc.audio_in[i]*0.00003058)*(yr/2)))
    x = int(i * xoffset) 
    color = etc.color_picker(etc.knob4) 
    last_point = [(int(etc.knob1*xr)), (int(etc.knob2*yr))]
    pygame.draw.circle(screen,color,(x, y1),int(etc.knob3 * x19) + 3, 0)
    pygame.draw.line(screen, color, last_point, [x, y1], int(etc.knob3 * x19)+1)
