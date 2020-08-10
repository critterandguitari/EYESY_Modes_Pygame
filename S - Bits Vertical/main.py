import os
import pygame
import random
import math

trigger = False
ypos = []
x = 0
y = 0
linelength = 50
lineAmt = 60
ypos = [random.randrange(-100, 720) for i in range(0, lineAmt + 2)]

def setup(screen, etc):
     pass
     ypos = [random.randrange(((-100*etc.yres)/720), etc.yres) for i in range(0, lineAmt)]

def draw(screen, etc):
    global trigger, x, y, ypos, lineAmt, linelength
    etc.color_picker_bg(etc.knob5)    
    height = (etc.yres+((etc.yres*40)/1280))
    width = etc.xres
    lengthcon = ((600*etc.yres)/720)
    linewidth = ((width + 40)/ lineAmt)
    linelength = int(etc.knob2*lengthcon + 1)
    yrangelow = ((-100*etc.yres)/720)
    color = etc.color_picker(etc.knob4)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
		
        lineAmt = int(etc.knob1*59 + 1)
        ypos = [random.randrange(yrangelow, height) for i in range(0, lineAmt)]
    
    trigger = False           
            
    for j in range(0, lineAmt) :
        
        auDio = int(etc.audio_in[j] / 180)
        diag = ((50*etc.xres)/1280)

        y = ypos[j] + linelength
        x = (j * linewidth) + (linewidth/2)- 1
        pygame.draw.line(screen, color, (x, ypos[j]+(auDio / 4)), (x+ int(etc.knob3 * (diag*2)-diag), y+auDio), linewidth)
