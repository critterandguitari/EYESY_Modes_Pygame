import os
import pygame
import random
import math
import time

vertLines = 20
trigger = False
xpos = 0
x = 0
y = 0
height = 0
width = 0

def setup(screen, etc):
    pass

def draw(screen, etc):
    global vertLines, trigger, xpos, x, y, height, width
    etc.color_picker_bg(etc.knob5)    
    sel = etc.knob4*8
    
    for i in range(0,1) : 
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
    
    xr = etc.xres
    yr = etc.yres
    linewidth = int((((etc.knob2*7) + 1)*yr)/720)+1
    lines = int(9*etc.knob1+1)+90
    min200 = ((200*xr)/1280)
    min100 = ((100*xr)/1280)
    max1000 = ((1280*xr)/1280)
    max700 = ((700*yr)/720)
    ran50 = ((50*xr)/1280)
    ran70 = ((70*xr)/1280)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        vertLines = random.randrange(int(etc.knob3*ran50)+2,int(etc.knob3*ran70)+8)
        x = random.randrange(-1*min200, max1000)
        y = random.randrange(-1*min200, max700)
        width = random.randrange(-1*min100, max1000)
        height = random.randrange(-1*min100, max1000)
        for l in range(0, vertLines) :
            xpos = x + (l + 1)*(width/vertLines) 
            
    for k in range(0, vertLines) :
        
        xpos = x + (k + 1)*(width/vertLines)
        pygame.draw.line(screen, color, (xpos, y), (xpos, height), linewidth)
        
    trigger = False   
    
    for j in range(0, lines) :
        
        linespace = yr-(lines-1)*(yr-2)/100
        pygame.draw.line(screen, color, (0,(j*linespace)+linespace/2), (xr,(j*linespace)+linespace/2), linewidth)
