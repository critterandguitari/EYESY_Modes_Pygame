import os
import pygame
import time
import random
import math

def setup(screen, etc):
    global last_point, last_point1, xr, yr, zehn, y72, x180
    xr = etc.xres
    yr = etc.yres
    last_point = [xr/4, 0]
    last_point1 = [xr/4, 0]
    zehn = (20*xr)/1280
    y72 = int((72*yr)/720)
    x180 = (180*xr)/1280
    pass

def draw(screen, etc):
    global last_point, last_point1, zehn, y72, x180, xr,yr
    etc.color_picker_bg(etc.knob5)    
    linewidth = int(etc.knob1*zehn)+1
    lines = int(y72)
    spacehoriz = (x180*etc.knob2)+18
    spacevert = spacehoriz
    recsize = zehn*etc.knob3
    sel = etc.knob4*8
    
    for j in range(0, lines) :
        
        if sel >= 7 :
            color = (int(127 + 127 * math.sin((j*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((j*1) * .05+ time.time())),
                    int(127 + 127 * math.sin((j*1) * .01 + time.time())))
        if 1 <= sel < 2 :
            color = (int(127 + 127 * math.sin((j*1) * .1 + time.time())),42,75)
        if 2 <= sel < 3 :
            color = (75,int(127 + 127 * math.sin((j*1) * .1 + time.time())),42)
        if 3 <= sel < 4 :
            color = (42,75,int(127 + 127 * math.sin((j*1) * .1 + time.time())))
        if 4 <= sel < 5 :
            color = (int(127 + 127 * math.sin((j*1) * .1 + time.time())),255,127)
        if 5 <= sel < 6 :
            color = (255,int(127 + 127 * math.sin((j*1) * .1 + time.time())),127)
        if 6 <= sel < 7 :
            color = (205,200,int(127 + 127 * math.sin((j*1) * .1 + time.time())))    
        if 1 > sel :
            color = (int(127 + 127 * math.sin((j*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((j*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((j*1) * .1 + time.time())))
        
        space = j*spacehoriz

        pygame.draw.line(screen, color, (0,space), (xr,space), linewidth)
    
    for m in range(0, lines) :
        
        if sel >= 7 :
            color = (int(127 + 127 * math.sin((m*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((m*1) * .05+ time.time())),
                    int(127 + 127 * math.sin((m*1) * .01 + time.time())))
        if 1 <= sel < 2 :
            color = (int(127 + 127 * math.sin((m*1) * .1 + time.time())),42,75)
        if 2 <= sel < 3 :
            color = (75,int(127 + 127 * math.sin((m*1) * .1 + time.time())),42)
        if 3 <= sel < 4 :
            color = (42,75,int(127 + 127 * math.sin((m*1) * .1 + time.time())))
        if 4 <= sel < 5 :
            color = (int(127 + 127 * math.sin((m*1) * .1 + time.time())),255,127)
        if 5 <= sel < 6 :
            color = (255,int(127 + 127 * math.sin((m*1) * .1 + time.time())),127)
        if 6 <= sel < 7 :
            color = (205,200,int(127 + 127 * math.sin((m*1) * .1 + time.time())))    
        if 1 > sel :
            color = (int(127 + 127 * math.sin((m*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((m*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((m*1) * .1 + time.time())))
        
        x = int(m*spacehoriz)+ 2
        y = 0
        auDio = int((etc.audio_in[m] * 0.00003058) * yr)
        #color = etc.color_picker(etc.knob4)
        if auDio < 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y], [x, y + auDio], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize*0.5),y+auDio,recsize,recsize], 0)
    
    for i in range(0, lines) :
        
        if sel >= 7 :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*1) * .05+ time.time())),
                    int(127 + 127 * math.sin((i*1) * .01 + time.time())))
        if 1 <= sel < 2 :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),42,75)
        if 2 <= sel < 3 :
            color = (75,int(127 + 127 * math.sin((i*1) * .1 + time.time())),42)
        if 3 <= sel < 4 :
            color = (42,75,int(127 + 127 * math.sin((i*1) * .1 + time.time())))
        if 4 <= sel < 5 :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),255,127)
        if 5 <= sel < 6 :
            color = (255,int(127 + 127 * math.sin((i*1) * .1 + time.time())),127)
        if 6 <= sel < 7 :
            color = (205,200,int(127 + 127 * math.sin((i*1) * .1 + time.time())))    
        if 1 > sel :
            color = (int(127 + 127 * math.sin((i*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*1) * .1 + time.time())),
                    int(127 + 127 * math.sin((i*1) * .1 + time.time())))
        
        x = int((i*spacehoriz)+1)
        y = int(yr-recsize)
        auDio = int((etc.audio_in[i] * 0.00003058) * yr)
        
        if auDio > 0 : auDio = 0
        pygame.draw.line(screen, color, [x,y], [x, y - (auDio*-1)], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-int((recsize/2)+1),y+auDio,recsize,recsize], 0)
