import os
import pygame
import time
import random
import math

count = 0

def setup(screen, etc):
    global xr, yr, x128, x8th
    xr = etc.xres
    yr = etc.yres
    x128 = int((128*xr)/1280)
    x8th = (8*xr)/1280
    pass
    
def draw(screen, etc):
    global count, xr, yr, x128, x8th 
    etc.color_picker_bg(etc.knob5)
    speed = etc.knob1*((20*xr)/1280)
    count = int(count + speed)
    thick = int(etc.knob3*((100*xr)/1280))+1
    peak = 0
    sel = int(etc.knob4*x8th)
    lines = 5
    
    for i in range(lines) : 
        if sel >= 7 :
            color = (int(127 + 127 * math.sin((i*51) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*51) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*51) * .01 + time.time())))
        if 1 <= sel < 2 :
            color = (int(127 + 127 * math.sin((i*51) * .1 + time.time())),42,75)
        if 2 <= sel < 3 :
            color = (75,int(127 + 127 * math.sin((i*51) * .1 + time.time())),42)
        if 3 <= sel < 4 :
            color = (42,75,int(127 + 127 * math.sin((i*51) * .1 + time.time())))
        if 4 <= sel < 5 :
            color = (int(127 + 127 * math.sin((i*51) * .1 + time.time())),255,127)
        if 5 <= sel < 6 :
            color = (255,int(127 + 127 * math.sin((i*51) * .1 + time.time())),127)
        if 6 <= sel < 7 :
            color = (205,200,int(127 + 127 * math.sin((i*51) * .1 + time.time())))    
        if 1 > sel :
            color = (int(127 + 127 * math.sin((i*51) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*51) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*51) * .1 + time.time())))

        for j in range(0,100) :
            if etc.audio_in[j] > peak:
                peak = etc.audio_in[j]
        
        R = 4 * etc.knob2 * (peak / x128)
        x = R * math.cos((count /  1000.) * 6.28) + (xr/2) + i*xr/lines-2*xr/lines
        y = R * math.sin((count /  1000.) * 6.28) + (yr/2)
        pygame.draw.line(screen, color, [(i*xr/lines)+xr/10, (yr/2)], [x, y], thick)
