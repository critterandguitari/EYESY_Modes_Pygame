import os
import pygame
import glob
import random

last_screen = pygame.Surface((1280,720))
xr = 320
yr = 240

def setup(screen, etc) :
    global last_screen, xr, yr
    
    xr = etc.xres
    yr = etc.yres
    last_screen = pygame.Surface((xr,yr))
    pass

def draw(screen, etc) :
    global last_screen
    etc.color_picker_bg(etc.knob5)    
    if etc.audio_trig or etc.midi_note_new :
        if etc.knob4 < .5 :
            r=g=b= int(etc.knob4*509+1) # first half of knob4 is graycale
        
        if etc.knob4 >= .5 :
            r = random.randrange(10,int(244*etc.knob4+11)) # second half of knob4 is color
            g = random.randrange(10,int(244*etc.knob4+11))
            b = random.randrange(10,int(244*etc.knob4+11))
        
        x = random.randrange(0,xr)
        y = random.randrange(0,yr)
        pygame.draw.circle(screen,(r,g,b),[x,y],int(((100*xr)/1280)*etc.knob1+10)) # ball size on knob1

    image = last_screen
    last_screen = screen.copy()
    thingX = int((xr-50)*etc.knob2)
    thingY = int((yr-50)*etc.knob2)
    placeX = (xr/2)-int(etc.knob2*((615*xr)/1280))
    placeY = (yr/2)-int(etc.knob2*((335*yr)/720))
    thing = pygame.transform.scale(image, (thingX, thingY)) # mirror screen scale
    thing.set_alpha(int(etc.knob3 * 180)) # adjust transparency on knob3
    screen.blit(thing, (placeX, placeY)) # mirror screen scale
