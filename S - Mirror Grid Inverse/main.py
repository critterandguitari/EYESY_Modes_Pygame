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
    zehn = (10*xr)/1280
    y72 = int((72*yr)/720)
    x180 = (180*xr)/1280
    pass

def draw(screen, etc):
    global last_point, last_point1, zehn, y72, x180, xr,yr
    etc.color_picker_bg(etc.knob5)    
    linewidth = int(etc.knob1*zehn)+1
    lines = int((39*etc.knob2)+1)+4
    
    spacehoriz = int(xr/(lines-2))
    spacevert = int(yr/(lines-2))
    recsize = int(zehn*etc.knob3)*2
    sel = etc.knob4*8
    
    for j in range(0,lines) :

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
                    
        pygame.draw.line(screen, color, (-1,j*spacevert), (xr,j*spacevert), linewidth)
    
    for m in range(0, lines) :
        x = int(m*spacehoriz)
        y = 0
        auDiom = (etc.audio_in[m] * 0.00003058) * yr
        
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
        
        pygame.draw.line(screen, color, [x,y], [x, yr/2 - auDiom], linewidth)
        if recsize >= 1 :
            pygame.draw.rect(screen, color, [x-(recsize*0.5),yr/2-auDiom,recsize,recsize], 0)

    for i in range(0, lines) :
        x = int(i*spacehoriz)
        y = yr/2
        auDio = (etc.audio_in[int(i+(lines*0.5))] * 0.00003058) * yr
        
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
        
        pygame.draw.line(screen, color, [x,yr], [x, (y-auDio)], linewidth)
        if recsize >= 1 and y-auDio > y:
            pygame.draw.rect(screen, color, [x-(recsize*0.5),(y-auDio)-recsize,recsize,recsize], 0)
