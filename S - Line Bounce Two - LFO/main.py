import os
import pygame
import math

y1 = y2 = xr = yr = x100 = y20 = 800

class LFO : #uses three arguments: start point, max, and how far each step is.
	
	def __init__(self, start, max, step):
		self.start = start
		self.max = max
		self.step = step
		self.current = 0
		self.direction = 1

	def update(self):
        # when it gets to the top, flip direction
		if (self.current >= self.max) :
			self.direction = -1
			self.current = self.max  # in case it steps above max
        # when it gets to the bottom, flip direction
		if (self.current <= self.start) :
			self.direction = 1
			self.current = self.start  # in case it steps below min
			
		self.current += self.step * self.direction
		
		return self.current

def setup(screen, etc):
	global b1,b2,b3,b4,y,xr,yr,x100, y20
	xr = etc.xres
	yr = etc.yres
	x100 = (100*xr)/1280
	y1 = 0
	y2
	b1 = LFO(x100,(xr-x100),10)
	b2 = LFO(x100,xr-x100,19)
	b3 = LFO(0,yr,2)
	pass
    
def draw(screen, etc):
	global b1,b2,b3,y1, y2,xr,yr,x100
	etc.color_picker_bg(etc.knob5)
	
	y1 = etc.audio_in[50] / 150 #Audio in L
	y2 = etc.audio_in[50] / 150 #Audio in R
	color = etc.color_picker(etc.knob4)
	color2 = etc.color_picker(etc.knob4)
	b1.step = (etc.knob3*(x100/10))+1
	b2.step = (etc.knob3*(x100/5))+2
	b3.step = (etc.knob1*(x100/10))+1
	posx1 = b1.update()
	posx2 = b2.update()
	width = int(etc.knob2*x100)+1
	
	rise = b3.update()+1
    
	pygame.draw.line(screen, color, [posx1, rise/2-y1], [posx1, rise/2+y1], width)
	pygame.draw.line(screen, color2, [posx2, rise-2*y2], [posx2, rise+2*y2], width*2)
