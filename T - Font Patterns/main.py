import os
import pygame
import time
import random

count = 0
trigger = False
unistr = unichr(random.randint(0x25a0, 0x25ff))
textpos = (0,0)

def setup(screen, etc):
    pass

def draw(screen, etc):
    global count, trigger, unistr, textpos
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    x320 = ((320*xr)/1280)
    x160 = ((160*xr)/1280)
    x260 = ((260*xr)/1280)
    x80 = ((80*xr)/1280)
    y90 = ((90*yr)/720)
    y45 = ((45*yr)/720)
    shift = int(etc.knob1*x320-x160)
    size = int(etc.knob2 * x260) + 5
    font = pygame.font.Font(etc.mode_root + "/font.ttf", size)
    color = etc.color_picker(etc.knob4)
    text = font.render(unistr, True, (color))     
    y = 0
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        unistr = get_unicode_character(int(etc.knob3 * 11)+1)
        
    for j in range(0,10):
        for i in range(0,9) :
        
            odd = i%2
            if odd == 0 :
                x = (i * x160 + x160 + shift) - x160
                y = (j * y90) - y45 #+ (shift-70)
                
            if odd == 1 :
                x = (i * x160 + x160) - x160
                y = (j * y90) - y45
            
            textpos = text.get_rect(center = (x,y))
            screen.blit(text, textpos)
    trigger = False

def get_unicode_character(set) :
    
    if set == 1 :
        # geometric shapes
        return unichr(random.randint(0x25a0, 0x25ff))
        
    if set == 2 :
        # arrows
        return unichr(random.randint(0x219C, 0x21BB))
        
    if set == 3 :
        # math
        return unichr(random.randint(0x223D, 0x224D))
        
    if set == 4 :
        # ogham
        return unichr(random.randint(0x1680, 0x169C))
        
    if set == 5 :
        # box drawing
        return unichr(random.randint(0x2500, 0x257f))
        
    if set == 6 :
        # Brail
        return unichr(random.randint(0x2800, 0x28FF))
        
    if set == 7 :
        # I Ching
        return unichr(random.randint(0x4DC2, 0x4DCF))
        
    if set == 8 :
        # from math -- sharp symbols
        return unichr(random.randint(0x2A80, 0x2ABC))

    if set == 9 :
        # vai syllables
        return unichr(random.randint(0xA500, 0xA62B))
    
    if set == 10 :
        #chess
        return unichr(random.randint(0xE010, 0xE04F))
        
    if set == 11 :
        #different boxes
        return unichr(random.randint(0x2580, 0x25AF))
        
    if set == 12 : 
        #select random glyph from the above subsets
        return unichr(random.choice([
            random.randint(0x2580, 0x25AF), # Different Boxes
            random.randint(0xE010, 0xE04F), # Chess
            random.randint(0xA500, 0xA62B), # Vai syllables
            random.randint(0x2A80, 0x2ABC), # Sharp Symbols
            random.randint(0x4DC2, 0x4DCF), # I Ching
            random.randint(0x2800, 0x28FF), # Brail
            random.randint(0x2500, 0x257f), # Box Drawing
            random.randint(0x1680, 0x169C), # Ogham
            random.randint(0x223D, 0x224D), # Math
            random.randint(0x219C, 0x21BB), # Arrows
            random.randint(0x25a0, 0x25ff)  # Geometric Shapes
            ]))
