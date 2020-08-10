import os
import pygame
import random

trigger = False
pList = [(random.randrange(-100,50),random.randrange(-100,56)) for i in range(0,100)]

def setup(sscreen, etc):
    global pList
    print "FFFFFFFF"
    pList = [(random.randrange(-100,etc.xres+100),random.randrange(-100,etc.yres+100)) for i in range(0,100)]

def draw(screen, etc):
    global trigger, pList
    etc.color_picker_bg(etc.knob5)    
    sizescale = ((200*etc.xres)/1280)
    xhalf = ((640*etc.xres)/1280)
    yhalf = ((360*etc.yres)/720)
    dscale = ((100*etc.xres)/1280)
    fill = int(etc.knob3*4)
    size = int(etc.knob1*sizescale)+1
    xdensity = int(etc.knob2*xhalf+20)
    ydensity = int(etc.knob2*yhalf+20)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True :
        pList = [(random.randrange(-dscale+xdensity,etc.xres+dscale-xdensity+10),random.randrange(-dscale+ydensity,etc.yres+dscale-ydensity+10)) for i in range(0,dscale)]

    for j in range(0, 30) :     
        color = etc.color_picker(etc.knob4)
        pygame.draw.rect(screen, color, [pList[j][0]-(size/2),pList[j][1]-(size/2),size,size], fill)

    trigger = False
