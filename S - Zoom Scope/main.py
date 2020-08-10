import os
import pygame
import math
import time

def setup(screen, etc) :
    global xr,yr,f,x2
    xr = etc.xres
    yr = etc.yres
    x2 = (2*xr)/1280
    if x2 <= 1 : x2 = 1
    f=2
    pass

def draw(screen, etc) :
    global xr,yr,f
    etc.color_picker_bg(etc.knob5)
    f = int(etc.knob1 * 94)+6
    for i in range(0, f) :
        seg(screen, etc, i)    

def seg(screen, etc, i) :
    global xr,yr,f,x2
    
    s1 = int((etc.audio_in[i]*0.00003058)*(yr/2))
    xs = int(xr/(f-4))

    sel = etc.knob4*7
    
    if sel >= 6 :
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
    if 1 > sel :
        color = (int(127 + 127 * math.sin(i * .1 + time.time())),
                int(127 + 127 * math.sin(i * .1 + time.time())),
                int(127 + 127 * math.sin(i * .1 + time.time())))
                
    offx = int((etc.knob2 * xr)-(xr/2)) 
    offy = int(etc.knob3 * yr)
    
    pygame.draw.circle(screen,color,((i*xs)+offx, offy+s1),(5*xr)/1280, 0)
    pygame.draw.line(screen, color, [(i*xs)+offx, offy], [(i*xs)+offx, s1+offy], x2)
