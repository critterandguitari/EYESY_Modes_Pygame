import os
import pygame
import random
import math

trigger = False
xpos = []
x = 0
y = 0
linelength = 50
lineAmt = 60
xpos = [random.randrange(-200, 1280) for i in range(0, lineAmt+2)]

def setup(screen, etc):
    pass
    xpos = [random.randrange(((-200*etc.xres)/1280), etc.xres) for i in range(0, lineAmt+2)]

def draw(screen, etc):
    global trigger, x, y, xpos, lineAmt, linelength
    etc.color_picker_bg(etc.knob5)    
    height = etc.yres
    width = (etc.xres+((etc.xres*20)/1280))
    lengthcon = ((300*etc.xres)/1280)
    linelength = int(etc.knob2*lengthcon+1)
    linewidth = height / lineAmt
    xrangelow = ((-200*etc.xres)/1280)
    color = etc.color_picker(etc.knob4)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        lineAmt = int(etc.knob1*59 + 1)
        xpos = [random.randrange(xrangelow, etc.xres) for i in range(0, lineAmt+2)]
    
    trigger = False           
            
    for i in range(0, lineAmt) :
        
        auDio = int(etc.audio_in[i] / 180)
        diag = ((50*etc.yres)/720)
        
        x = xpos[i] + linelength
        y = (i * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (xpos[i]+(auDio / 4), y), (x+auDio, y + int(etc.knob3 * (diag*2) - diag)), linewidth)
