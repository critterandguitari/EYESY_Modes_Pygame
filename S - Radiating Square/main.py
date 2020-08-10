import os
import pygame
import time
import random
import math

note_down = False
# knob 1 = x origin point LFO rate ; knob 2 = line width ; knob3 = endpoint LFO rate ; knob4 = color

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
    global sqmover, adjust1, adjust2, xr,yr
    etc.color_picker_bg(etc.knob5)
    xr = etc.xres
    yr = etc.yres
    sqmover = LFO(-1*(yr/2),yr/2,0.01)
    adjust1 = LFO(-50,50,0.01)
    adjust2 = LFO(-100,100,0.01)
    pass

def draw(screen, etc) :
    global sqmover, adjust1, adjust2, xr,yr
    for i in range(0, 100) :
        width = int(etc.knob2*((15*xr)/1280))+1
        #LFOs
        adjuster1 = adjust1.update()
        adjust1.step = etc.knob1/50
        adjuster2 = adjust2.update()
        adjust2.step = etc.knob1+.001
        if etc.knob1 == 0 : adjuster1 = adjuster2 = 0
        sqmover.step = etc.knob3 + .01
        angle = sqmover.update()
        if etc.knob3 == 0 : angle = 0
        
        #color
        color = etc.color_picker(etc.knob4)
        if .9 <= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*1) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*1) * .01 + time.time())))
        if .1 >= etc.knob4 :
            color = (int(127 + 127 * math.sin((i*3) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*3) * .1+ time.time())),
                    int(127 + 127 * math.sin((i*3) * .1 + time.time())))
        
        #lines
        if  i < 25:  
            x0 = (((490  + adjuster1*i)*xr)/1280)%xr
            x1 = x0 - int(etc.audio_in[i] / 100)
            y = (((210 + i * 12 + adjuster2)*yr)/720)%yr
            pygame.draw.line(screen, color, [x0, y], [x1, (y - angle)], width)
    
        if i >= 25 and i < 50:
            x = (((190 + i * 12 + adjuster2)*xr)/1280)%xr
            y0 = (((510 + adjuster1*i)*yr)/720)%yr
            y1 = y0 + int(etc.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x + angle), y1], width)        
                
        if i >= 50 and i < 75:
            x0 = (((790 + adjuster1*i)*xr)/1280)%xr
            x1 = (x0 + int(etc.audio_in[i] / 100))
            y = (((1110 - i * 12 + adjuster2)*yr)/720)%yr
            pygame.draw.line(screen, color, [x0, y], [x1, (y + angle)], width)
                        
        if i >= 75 and i < 100:
            x = (((1690 - i * 12 + adjuster2)*xr)/1280)%xr
            y0 = (((210 + adjuster1*i)*yr)/720)%yr
            y1 = y0 - abs(etc.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x - angle), y1], width)
        
        if i == 1:
            x = (((490 + adjuster2)*xr)/1280)%xr
            y0 = (((210 + adjuster1*i)*yr)/720)%yr
            y1 = y0 - int(etc.audio_in[i] / 100)
            pygame.draw.line(screen, color, [x, y0], [(x - angle), y1], width)
