import os
import pygame
import time
import random
import math

x21 = y21 = x2=y2=x3=y3=x11=y11=x1=y1=x4=y4=0
sound = 0
xr = 320
yr = 240

def setup(screen, etc) :
	global xr, yr
	xr = etc.xres
	yr = etc.yres
	pass

def draw(screen, etc) :
    global sound, xr, yr
    etc.color_picker_bg(etc.knob5)    
    if etc.audio_trig or etc.midi_note_new :
        sound = (((2*etc.knob2-1)/10 + sound))

    a = math.pi*sound
    xc = xr/2
    yc = yr/2
    linewidth = xc - int(etc.knob1*(xc-1))
    L1000 = ((1000*xr)/1280)
    L = etc.knob1*L1000 + linewidth
    if L > xr : L = xr
    
    color = etc.color_picker(etc.knob4)
    
    if etc.knob2 < .5 :
        x21 = (L/2)*math.cos(a)
        y21 = (L/2)*math.sin(a)
        x2 = int(xc+x21)
        y2 = int(yc-y21)
        x3 = int(xc-x21)
        y3 = int(yc+y21)
        pygame.draw.line(screen, color, [x2,y2], [x3, y3], linewidth)
    
    if etc.knob2 > .5 :
        x11 = (L/2)*math.cos(a)
        y11 = (L/2)*math.sin(a)
        x1 = xc-x11
        y1 = yc+y11
        x4 = xc+x11
        y4 = yc-y11
        pygame.draw.line(screen, color, [x1,y1], [x4, y4], linewidth)
    
    #Trails
    veil = pygame.Surface((xr,yr))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))
