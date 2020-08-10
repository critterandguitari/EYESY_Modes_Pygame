import os
import pygame
import random

trigger = False
x = 0
y = 0
height = 720
width = 1340
linelength = 50
lineAmt = 20
displace = 10
ypos = [random.randrange(-200,720) for i in range(0, lineAmt + 2)]
ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]
xr = 360
yr = 240

def setup(screen, etc):
	global trigger, x, y, height, width, ypos, lineAmt, ypos1, linelength, displace, xr, yr
	x = 0
	y = 0
	xr = etc.xres
	yr = etc.yres
	height = yr
	width = xr+20
	linelength = ((50*yr)/720)
	displace = ((10*yr)/720)
	ypos = [random.randrange(int((-200*yr)/720),yr) for i in range(0, lineAmt + 2)]
	ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]
	pass

def draw(screen, etc):
    global trigger, x, y, height, width, ypos, lineAmt, ypos1, linelength, displace, xr, yr 
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    displace = ((10*yr)/720)
    linewidth = (width / lineAmt)
    linelength = int(etc.knob2*((300*yr)/720)+1)
    color = etc.color_picker(etc.knob4)
    minus = (etc.knob3*0.5)+0.5
    shadowColor = (etc.bg_color[0]*minus, etc.bg_color[1]*minus, etc.bg_color[2]*minus)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
		
		lineAmt = int(etc.knob1*((100*xr)/1280) + 2)
		ypos = [random.randrange(int((-200*yr)/720),yr) for i in range(0, lineAmt + 2)]
		ypos1 = [(ypos[i]+displace) for i in range(0, lineAmt + 2)]
		
    for k in range(0, lineAmt + 2) :
       
        y = ypos1[k] + linelength
        x = (k * linewidth) + int(linewidth/2)- 1
        #x = (k * linewidth)# + int(linewidth/2)- 1
        pygame.draw.line(screen, shadowColor, (x+displace, ypos1[k]), (x+displace, y), linewidth)
    for j in range(0, lineAmt + 2) :
       
        y = ypos[j] + linelength
        x = (j * linewidth) + int(linewidth/2)- 1
        pygame.draw.line(screen, color, (x, ypos[j]), (x, y), linewidth)        
    trigger = False
