import os
import pygame
import time
import random
import math

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
    global lfo1, xr, yr
    xr = etc.xres
    yr = etc.yres
    lfo1 = LFO(-1*(xr*0.75),xr*0.75,1)
    pass

def draw(screen, etc):
    global lfo1, xr, yr
    etc.color_picker_bg(etc.knob5)
    avg = 0
    unistr = unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56) + unichr(56)   #"88888888"...use unicode value for each character
    size = int(etc.knob1 * ((100*xr)/1280)) + 5    
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    textpos = (0,0)
    phrase = 6
    lfo1.step = etc.knob2*((5*xr)/1280)+0.01
    cycle = (etc.knob2*time.time())%1
    if etc.knob2 == 0 : cycle = 0
    
    for i in range(0, 100) :
        scalar = int(etc.knob2*((20*xr)/1280))+2
        avg = etc.audio_in[i] + avg
        avg = scalar*avg / (i + 1)
    
    for i in range(phrase) :
    
        color = etc.color_picker(etc.knob4)
        if .9 <= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .01 + time.time())))
        if .1 >= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .1+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .1 + time.time())))
    
        text = font.render(unistr, True, (color))   
        R = 1
        R = (R + (avg / 10)) * (i * .5)
        newcenterX = math.sin(cycle*6.28)*(xr/2)*(-etc.knob3)
        newcenterY = math.cos(cycle*6.28)*(yr/2)*(etc.knob3)

        x = (R * math.cos((lfo1.update() /  (xr*0.75)) * 6.28)) + (xr/2)
        y = (R * math.sin((lfo1.update() /  (xr*0.75)) * 6.28)) + (yr/2)
        
        textpos = text.get_rect(center = (x+newcenterX,y+newcenterY))
        screen.blit(text, textpos)
