import os
import pygame
import random

trigger = False
x = 0
y = 0
height = 720
width = 1280
linelength = 50
lineAmt = 20
displace = 10
xpos = [random.randrange(-200,1280) for i in range(0, lineAmt + 2)]
xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]
xr = 360
yr = 240

def setup(screen, etc):
	global trigger, x, y, height, width, xpos, lineAmt, xpos1, linelength, displace, xr, yr
	xr = etc.xres
	yr = etc.yres
	height = yr
	width = xr
	linelength = ((50*xr)/1280)
	lineAmt = ((20*xr)/1280)
	displace = ((10*xr)/1280)
	xpos = [random.randrange(int((-200*xr)/1280),xr) for i in range(0, lineAmt + 2)]
	xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]
	pass

def draw(screen, etc):
    global trigger, x, y, height, width, xpos, lineAmt, xpos1, linelength, displace, xr, yr 
    etc.color_picker_bg(etc.knob5)    
    displace = ((10*xr)/1280)
    linewidth = (height / lineAmt)
    linelength = int(etc.knob2*((300*xr)/1280)+1)
    color = etc.color_picker(etc.knob4)
    minus = (etc.knob3*0.5)+0.5
    shadowColor = (etc.bg_color[0]*minus, etc.bg_color[1]*minus, etc.bg_color[2]*minus)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        
        lineAmt = int(etc.knob1*((100*yr)/720) + 2)
        xpos = [random.randrange(int((-200*xr)/1280),xr) for i in range(0, lineAmt + 2)]
        xpos1 = [(xpos[i]+displace) for i in range(0, lineAmt + 2)]
    
    for k in range(0, lineAmt + 2) :
       
        x = xpos1[k] + linelength
        y = (k * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (xpos1[k], y+displace), (x, y+displace), linewidth)
    for j in range(0, lineAmt + 2) :
       
        x = xpos[j] + linelength
        y = (j * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (xpos[j], y), (x, y), linewidth)        
    trigger = False
