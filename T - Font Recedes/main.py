import os
import pygame
import time
import random
import pygame.freetype

size = 1000
gs = 0
charnum = 1
x = 640
y = 360
yo = 255
speed = 1

def setup(screen, etc):
    pygame.freetype.init()
    pass

def draw(screen, etc):
    global size, gs, charnum, x, y, charList, unistr, coloryo, yo, speed
    etc.color_picker_bg(etc.knob5)    
    if etc.audio_trig or etc.midi_note_new :
        gs = 1
        xr = etc.xres
        size500 = ((500*xr)/1280)
        size = size500 * (etc.knob2 + .1)
        unistr = unichr(random.randint(0x1680, 0x169C))
        x = random.randrange(0,screen.get_width())
        y = random.randrange(0,screen.get_height())
        color = etc.color_picker(etc.knob4)
        speed=int(etc.knob1*100+1)
        yo = speed
        
    if gs == 1 and size > 0 :
        
        font = pygame.freetype.Font(etc.mode_root + "/font.ttf", size)
        
        color = etc.color_picker(etc.knob4)
        coloryo = (int(color[0]*speed/yo),int(color[1]*speed/yo),color[2]*speed/yo)
        if coloryo == (1,1,1) : coloryo = (0,0,0)
    
        (text, textpos) = font.render(unistr, coloryo)
        textpos.centerx = x
        textpos.centery = y
    
        screen.blit(text, textpos)
        size = size - 5 * 50*(etc.knob3 + .02)
        yo = yo + 1
        if yo > 255 : yo = 255
        if size < 1 : size = 1
