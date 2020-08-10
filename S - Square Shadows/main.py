import os
import pygame
import time
import random
import math

def setup(screen, etc):
    pass

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 25) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :

    xr = etc.xres
    yr = etc.yres
    x = int(etc.knob2*xr) + (etc.audio_in[i * 4] / 35)
    y = i * ((29*yr)/720)+5
    size125 = ((125*xr)/1280)
    squaresize = int(etc.knob1*size125)+1
    shad25 = ((25*xr)/1280)
    
    #Shadow Squares
    color = (0,0,0)
    pygame.draw.line(screen, color, [x + (shad25-int(etc.knob3*2*shad25)), y+(shad25-int(etc.knob3*2*shad25))], [x + (shad25-int(etc.knob3*2*shad25)), y+squaresize], squaresize)

    sel = etc.knob4*8
    
    if sel >= 7 :
        color = (int(127 + 127 * math.sin(i * .1 + time.time())),
                int(127 + 127 * math.sin(i * .05 + time.time())),
                int(127 + 127 * math.sin(i * .01 + time.time())))
    if 1 <= sel < 2 :
        color = (int(127+127 * math.sin(i * .1 + time.time())),0,45)
    if 2 <= sel < 3 :
        color = (255,int(155 + 100 * math.sin(i * .1 + time.time())),30)
    if 3 <= sel < 4 :
        color = (0,75,int(127 + 127 * math.sin(i * .1 + time.time())))
    if 4 <= sel < 5 :
        color = (int(200 + 55 * math.sin(i * .1 + time.time())),255,100)
    if 5 <= sel < 6 :
        color = (127,int(127 + 127 * math.sin(i * .1 + time.time())),127)
    if 6 <= sel < 7 :
        color = ((i*50*time.time())%127,(15*i*time.time())%127,int(100 + 100 * math.sin(i *3* .1 + time.time())))    
    if 1 > sel :
        color = (int(127 + 127 * math.sin((i*14) * .1 + time.time())),
                int(127 + 127 * math.sin((i*14) * .1 + time.time())),
                int(127 + 127 * math.sin((i*14) * .1 + time.time())))
                
    pygame.draw.line(screen, color, [x, y], [x, y+squaresize], squaresize)
