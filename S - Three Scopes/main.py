import os
import pygame
import time
import random

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    color = etc.color_picker(etc.knob4) #on knob4
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    yhalf = yr/2
    ythird = yr/3
    y2third = (2*yr)/3
    step16 = ((16*xr)/1280)
    wid = ((xr*42)/1280)
    steppy = int(etc.knob1 * step16)
    leftpoint = int(etc.knob2 * yr)
    linewidth = int(etc.knob3*wid+1)
    screendiv = (xr/60)
    
    for i in range (0,30) :
        ay0 = ythird + leftpoint - (steppy * i)
        ay1 = ythird + leftpoint - (steppy * i) + (etc.audio_in[i] / 128)
        ax = i * screendiv 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    for i in range (30,60) :
        ay0 = y2third - leftpoint + (steppy * (i-30))
        ay1 = y2third - leftpoint + (steppy * (i-30))+ (etc.audio_in[i] / 128)
        ax = (i-30) * screendiv 
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
    
    for i in range (60,94) :
        ay0 = yhalf
        ay1 = yhalf + (etc.audio_in[i] / 80)
        ax = (i-30) * screendiv#21.3
    
        pygame.draw.line(screen, color, [ax, ay1], [ax, ay0], linewidth)
