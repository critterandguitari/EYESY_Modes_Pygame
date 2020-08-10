import os
import pygame
import time
import random
import glob
import math

last_point = []

class LFO : #uses three arguments: start point, max, and how far each step is.
    
    def __init__(self, start, max, step):
        self.start = start
        self.max = max
        self.step = step
        self.current = 0
        self.direction = 1

    def update(self):
        
        # when it gets to the top, flip direction
        if (self.current >= self.max) :
            self.direction = -1
            self.current = self.max  # in case it steps above max
        
        # when it gets to the bottom, flip direction
        if (self.current <= self.start) :
            self.direction = 1
            self.current = self.start  # in case it steps below min
            
        self.current += self.step * self.direction
        
        return self.current

xmover = LFO(0,0,1)
ymover = LFO(0,0,1)

def setup(screen, etc):
    global last_point, xr,yr, xmover, ymover
    xr = etc.xres
    yr = etc.yres
    xmover = LFO(0,xr,(xr/2))
    ymover = LFO(0,yr,1)
    last_point = [0, (yr/2)]

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)    
    for i in range(0, 50) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point, image_index, xr,yr, xmover, ymover
    
    xoffset = int(xr/50)
    fatness = int(xr/120)
    y0 = screen.get_height() // 2
    y1 = int((screen.get_height() // 2) + ((etc.audio_in[i]*0.00003058)*(yr/2)))
    x = int(i * xoffset)
    sel = etc.knob4*8
    Cmod = etc.knob3*2
    
    if 1 > sel :
        color = (int(127 + 127 * math.sin(i * 1*Cmod + time.time())),
                int(127 + 127 * math.sin(i * 1*Cmod + time.time())),
                int(127 + 127 * math.sin(i * 1*Cmod + time.time())))
    if 1 <= sel < 2 :
        color = (int(127+127 * math.sin(i * 1*Cmod + time.time())),0,45)
    if 2 <= sel < 3 :
        color = (255,int(155 + 100 * math.sin(i * 1*Cmod + time.time())),30)
    if 3 <= sel < 4 :
        color = (0,200,int(127 + 127 * math.sin(i * 1*Cmod + time.time())))
    if 5 > sel >= 4 :
        color = ((127*Cmod)%255,
                (127*Cmod)%255,
                int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())))
    if 6 > sel >= 5 :
        color = ((127*Cmod)%255,
                int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())),
                (127*Cmod)%255)
    if 7 > sel >= 6 :
        color = (int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())),
                (127*Cmod)%255,
                (127*Cmod)%255)
    if  sel >= 7 :
        color = (int(127 + 127 * math.sin((i+30) * (1*Cmod+.01) + time.time())),
                int(127 + 127 * math.sin((i+30) * (.5*Cmod+.005) + time.time())),
                int(127 + 127 * math.sin((i+15) * (.1*Cmod+.001) + time.time())))
    
    xmover.step = etc.knob1*((2*xr)/1280)+0.01
    ymover.step = etc.knob2*((2*xr)/1280)+0.01
    xpos = xmover.update()
    ypos = ymover.update()

    last_point = [(int(xpos)), (int(ypos))]
    pygame.draw.circle(screen,color,(x + xoffset, y1),int(etc.knob3 * fatness) + 3, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], int(etc.knob3 * fatness)+1)
