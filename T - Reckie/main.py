import os
import pygame
import random

trigger = False
myRect = pygame.Rect(640-25,360-25,50,50)
xr = 320
yr = 240

def setup(screen, etc) :
	global xr, yr
	xr = etc.xres
	yr = etc.yres
	
	pass

def draw(screen, etc) :
    global trigger, myRect, xr, yr
    etc.color_picker_bg(etc.knob5)    
    size100 = ((100*xr)/1280)
    xhalf = xr/2
    yhalf = yr/2
    
    color = etc.color_picker(etc.knob4) 
    myRect = pygame.Rect(myRect.topleft, (int(etc.knob1*2*size100)-size100, int(etc.knob2*2*size100)-size100))
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        
        set = random.randrange(0,7)
        
        if set == 0 :
            #up
            myRect.bottom = myRect.top             
        
        if set == 1 :
            #upright
            myRect.bottomleft = myRect.topright    
        
        if set == 2 :
            #upleft
            myRect.bottomright = myRect.topleft    
        
        if set == 3 :
            #left
            myRect.right = myRect.left             
        
        if set == 4 :
            #right
            myRect.left = myRect.right             
        
        if set == 5 :
            #downright
            myRect.topleft = myRect.bottomright    
        
        if set == 6 :
            #down
            myRect.top = myRect.bottom             
        
        if set == 7 :
            #downleft
            myRect.topright = myRect.bottomleft  
        
    trigger = False    
    
    if myRect.center[0] <= 0 : myRect.center = (xhalf, yhalf)
    if myRect.center[0] >= xr : myRect.center = (xhalf, yhalf)
    if myRect.center[1] <= 0 : myRect.center = (xhalf, yhalf)
    if myRect.center[1] >= yr : myRect.center = (xhalf, yhalf)
    
    pygame.draw.rect(screen, color, myRect, int(etc.knob3 * size100))
