import os
import pygame
import math
import time

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
        
def setup(screen, etc) :
    global xr, yr, x8, y5, hund, otwen, drei, acht, sqmover
    etc.color_picker_bg(etc.knob5)
    xr = etc.xres
    yr = etc.yres
    x8 = xr/8
    y5 = yr/5
    hund = (99*xr)/1280
    otwen = (120*xr)/1280
    drei = (3*xr)/1280
    acht = (8*xr)/1280
    sqmover = LFO(otwen*-1,otwen,10)
    if drei == 0 : 
        drei =1
    pass

def draw(screen, etc) :
    global xr, yr, x8, y5, hund, otwen, drei, acht, sqmover
    for i in range(0, 7) :
        
        sqmover.step = etc.knob1*drei
        sqmover.max = int(etc.knob2*otwen)
        sqmover.start = int(etc.knob2*-otwen)
        xoffset = -sqmover.update()
        yoffset = sqmover.update()*0.8
         
        for j in range(0, 10) :
            x = (j*(x8))-(x8)
            y = (i*(y5))-(y5)
            
            rad = abs(etc.audio_in[j-i] / hund)
            width = int(etc.knob3*hund)+1
            sel = int(etc.knob4*acht)
            if sel >= 7 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*7) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*7) * .01 + time.time())))
            if 1 <= sel < 2 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),42,75)
            if 2 <= sel < 3 :
                color = (75,int(127 + 127 * math.sin((i*7) * .1 + time.time())),42)
            if 3 <= sel < 4 :
                color = (42,75,int(127 + 127 * math.sin((i*7) * .1 + time.time())))
            if 4 <= sel < 5 :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),255,127)
            if 5 <= sel < 6 :
                color = (255,int(127 + 127 * math.sin((i*7) * .1 + time.time())),127)
            if 6 <= sel < 7 :
                color = (205,200,int(127 + 127 * math.sin((i*7) * .1 + time.time())))    
            if 1 > sel :
                color = (int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*7) * .1 + time.time())))
            
            if (i%2) == 1 : 
                x = j*(x8)-(x8)+xoffset
            if (j%2) == 1 : 
                y = i*(y5)-(y5)+yoffset
            
            rect = pygame.Rect(0,0,width,width)
            rect.center = (x,y)
            rect.inflate_ip(rad,rad)
            
            pygame.draw.rect(screen, color, rect, 0)
