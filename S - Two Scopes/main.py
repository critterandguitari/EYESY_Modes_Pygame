import os
import pygame
import time
import random
import math

def setup(screen, etc) :
    pass

def draw(screen, etc) :
	
	etc.color_picker_bg(etc.knob5)
	xr = etc.xres
	yr = etc.yres
	w100 = ((100*yr)/720)
	for i in range (0,50) :
		x0 = int(etc.knob1*xr) 
		x1 = x0 + (etc.audio_in[i] / 35)
		y = i * (yr/48)
		color = etc.color_picker(etc.knob4)
		
		if etc.knob4 >= 1 :
		    color = (int(127 + 127 * math.sin(i * .1 + time.time())),
                    int(127 + 127 * math.sin(i * .05 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())))

		pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob3*w100+1))
		
	for i in range (51,100) :
		x0 = int(etc.knob2*xr)
		x1 = x0 + (etc.audio_in[i] / 35)
		y = (i - 50) * (yr/48)
		color = etc.color_picker(etc.knob4)
		
		if etc.knob4 >= 1 :
		    color = (int(127 + 127 * math.cos(i * .1 + time.time())),
                    int(127 + 127 * math.cos(i * .05 + time.time())),
                    int(127 + 127 * math.cos(i * .01 + time.time())))

		pygame.draw.line(screen, color, [x0, y], [x1, y], int(etc.knob3*w100+1))
