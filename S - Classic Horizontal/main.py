import os
import pygame
import math
import time

lines = 100

def setup(screen,etc) :
    pass

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, lines) :
        seg(screen, etc, i)
        
def seg(screen, etc, i) :
    
    space = etc.xres/(lines-2)
    y0 = 0
    y1 = (etc.audio_in[i] / 90)
    x = i*space
    linewidth = int(etc.knob1*etc.xres/(lines-75))
    position = etc.yres/2
    ballSize = int(etc.knob2*etc.xres/(lines-75))
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
    
    pygame.draw.circle(screen,color,(x, y1+position),ballSize, 0)
    pygame.draw.line(screen, color, [x, y0+position], [x, y1+position], linewidth)
