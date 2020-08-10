import os
import pygame
import time
import random

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
        
def setup(screen, etc):
    global xr,yr, fanner, pointer
    xr = etc.xres
    yr = etc.yres
    fanner = LFO(1,yr/2,1)
    pointer = LFO(1,yr/2,1)
    pass

def draw(screen, etc):
    global xr,yr
    etc.color_picker_bg(etc.knob5)    
    lines = int(etc.knob1*29)+1
    color = etc.color_picker(etc.knob4) #knob4
    fanner.step = int(etc.knob2*10)
    pointer.step = int(etc.knob2*10)
    R = (((etc.audio_in[1]*0.00003058)) * (yr/2))+ (yr/2)
    L = (((etc.audio_in[11]*0.00003058)) * (yr/2))+ (yr/2)
    T = (((etc.audio_in[21]*0.00003058)) * (yr/2))+ (yr/2)
    E = (((etc.audio_in[45]*0.00003058)) * (yr/2))+ (yr/2)
    F = (((etc.audio_in[75]*0.00003058)) * (yr/2))+ (yr/2)
    fan=fanner.update()*((((etc.knob3*100))/100)/8)
    point=pointer.update()*(((((etc.knob3*100)+50)%100)/100)/8)
    
    for i in range (0,lines) :
        
        modi = i%2
        if modi == 1 :
            pygame.draw.aalines(screen, color, True, [[0, R-(i*point)], [xr/2, L-(i*fan)], [xr, T-(i*point)], [xr*0.75, E-(i*fan)], [yr/2, F-i]], 1)
        if modi == 0 :
            pygame.draw.aalines(screen, color, True, [[0, R+(i*point)], [xr/2, L+(i*fan)], [xr, T+(i*point)], [xr*0.75, E+(i*fan)], [yr/2, F+i]], 1)
