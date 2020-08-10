import os
import pygame
import time
import math

y = 240
x = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global y, x
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    xhalf = xr/2
    yhalf = yr/2
    yspeed = ((etc.knob2*40 - 20)*yr)/720
    xspeed = ((etc.knob3*60 - 20)*xr)/1280
    thick = int(etc.knob1*(yr-1))+1
    peak = 0
    sel = etc.knob4*8
    
    for i in range(0,1) :
        peak = etc.audio_in[i]
    
        if 1 > sel :
            color = (int(127 + 127 * math.sin(i * .1 + time.time())),
                    int(127 + 127 * math.sin(i * .1 + time.time())),
                    int(127 + 127 * math.sin(i * .1 + time.time())))
        if 1 <= sel < 2 :
            color = (int(127+127 * math.sin(i * .1 + time.time())),0,45)
        if 2 <= sel < 3 :
            color = (255,int(155 + 100 * math.sin(i * .1 + time.time())),30)
        if 3 <= sel < 4 :
            color = (0,200,int(127 + 127 * math.sin(i * .1 + time.time())))
        if 5 > sel >= 4 :
            color = (0,
                    0,
                    int(127 + 127 * math.sin(i * .1 + time.time())))
        if 6 > sel >= 5 :
            color = (0,
                    int(127 + 127 * math.sin(i * .1 + time.time())),
                    0)
        if 7 > sel >= 6 :
            color = (int(127 + 127 * math.sin(i * .1 + time.time())),
                    0,
                    0)
        if  sel >= 7 :
            color = (int(127 + 127 * math.sin((i+30) * .1 + time.time())),
                    int(127 + 127 * math.sin((i+30) * .05 + time.time())),
                    int(127 + 127 * math.sin((i+15) * .01 + time.time())))
    
    L =  peak/6+1
    x1 = x - L
    x2 = x + L
    
    pygame.draw.line(screen, color, [x1, y], [x2, y], thick)
    
    y = y + yspeed
    x = x + xspeed
    if y > yr + thick/2 : y = 0 - thick/2 
    if y < 0 - thick/2 : y = yr + thick/2
    if x > xr : x = 0
    if x < 0 : x = xr
