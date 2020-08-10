import os
import pygame
import glob
import pygame.gfxdraw
import math
import time
bkgrnd = pygame.Surface((1280, 720))
trot = 0
x1 = 640
y1 = 360
trigger = False

def setup(screen, etc):
    global bkgrnd, x1, y1
    x1 = etc.xres/2
    y1 = etc.yres/2
    bkgrnd = pygame.Surface((etc.xres, etc.yres))
    pass

def draw(screen, etc) :
    global bkgrnd, shape, trot, trigger, x1, y1
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    rotrate = 15-etc.knob3*30

    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        trot = trot + rotrate
    trigger = False    
    p100 = ((100*xr)/1280)
    p200 = ((200*xr)/1280)
    p400 = ((400*xr)/1280)
    sel = etc.knob4*8
    
    for i in range(1,2) :
        
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
        
        shape = pygame.Surface((p200,p400))
        pygame.gfxdraw.filled_trigon(shape, 0,p400,p100,0,p200,p400, color)    
        shape = pygame.transform.scale(shape, (p200, p400))
        shape.set_colorkey ((0,0,0))
        shape = pygame.transform.rotate(shape, trot)
        new_width = shape.get_width()
        new_height = shape.get_height()
        x = (0 + new_width / 2)
        y = (0 + new_height / 2)
        speedx = (etc.knob1 * 50 - 25)
        speedy = (etc.knob2 * 50 - 25)
        screen.blit(shape, (x1-x, y1-y ))
    
    x1 = x1 + speedx
    y1 = y1 + speedy
    if x1 < 0 : x1 = xr
    if x1 > xr : x1 = 0
    if y1 < 0 : y1 = yr
    if y1 > yr : y1 = 0
