import os
import pygame
import random

trigger = False
pointz = [[600,400],[640,340],[680,400]]
superColor = (0,0,0)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, pointz, superColor
    etc.color_picker_bg(etc.knob5)    
    color = etc.color_picker(etc.knob4)
    posx = int(etc.knob1*etc.xres)
    posy = int(etc.knob2*etc.yres)
    density = int(etc.knob3*((600*etc.xres)/1280))
        
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        randColor = random.randrange(50,100)*.01
        superColor = (color[0]*randColor, color[1]*randColor, color[2]*randColor) 
        x = random.randrange(0,3)
        pointz[x] = (random.randrange(posx-density,posx+density+10), random.randrange(posy-density,posy+density+10))
       
    trigger = False    
    
    pygame.draw.polygon(screen, superColor, pointz, 0)
