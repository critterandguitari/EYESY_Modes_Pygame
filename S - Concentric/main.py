import os
import pygame
import math
import time

def setup(screen, etc):
    pass

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    x = int(etc.knob1*etc.xres)
    y = int(etc.knob2*etc.yres)
    circles = 10
    sel = etc.knob4*8
    Cmod = etc.knob3*2
    
    for i in range(1,circles) :
        
        x = x+i/3
        R = int(abs(etc.audio_in[i]/100)*etc.yres/720)
        
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
                    int(127 + 127 * math.sin(i * (Cmod) + time.time())))
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

        pygame.draw.circle(screen,color,(x,y),(R))
