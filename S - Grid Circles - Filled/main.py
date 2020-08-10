import os
import pygame
xr = 0
yr = 0
x8 = 0
y5 = 0

def setup(screen, etc) :
    global xr, yr, x8, y5
    xr = etc.xres
    yr = etc.yres
    x8 = xr/8
    y5 = yr/5
    pass

def draw(screen, etc) :
	global xr, yr, x8, y5
	etc.color_picker_bg(etc.knob5)
    
	for i in range(0, 7) :
		xoffset = int(etc.knob1*(x8))
		yoffset = int(etc.knob2*(y5))
         
		for j in range(0, 10) :
			x = (j*(x8))-(x8)
			y = (i*(y5))-(y5)
			rad = ((abs(etc.audio_in[j+i] / 300)) * xr)/1280
			restRad = int(etc.knob3*((30*xr)/1280))+1
			color = etc.color_picker(etc.knob4)
			if (i%2) == 1 : 
				x = j*(x8)-(x8)+xoffset
			if (j%2) == 1 : 
				y = i*(y5)-(y5)+yoffset
            
			pygame.draw.circle(screen, color, [x, y], rad+restRad) 
