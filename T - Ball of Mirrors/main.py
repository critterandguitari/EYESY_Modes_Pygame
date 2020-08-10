import os
import pygame
import glob
import random

image_index = 0
last_screen = pygame.Surface((10, 10))

def setup(screen, etc) :
    global last_screen
    last_screen = pygame.Surface((etc.xres,etc.yres))
    pass

def draw(screen, etc) :
    global last_screen
    etc.color_picker_bg(etc.knob5)    
    cscale = int(((50*etc.xres)/1280))
    
    if etc.audio_trig or etc.midi_note_new :
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        x = random.randrange(0,etc.xres)
        y = random.randrange(0,etc.yres)
        pygame.draw.circle(screen,(r,g,b),[x,y],cscale)

    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image, (int(etc.knob3 * etc.xres), int(etc.knob4 * etc.yres) ) )
    thing = pygame.transform.flip(thing, 1,0)
    screen.blit(thing, (int(etc.knob1 * etc.xres), int(etc.knob2 * etc.yres)))
