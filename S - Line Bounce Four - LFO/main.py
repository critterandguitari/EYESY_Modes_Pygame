import os
import pygame
import math

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
	global b1,b2,b3,b4,y,xr,yr,x100
	xr = etc.xres
	yr = etc.yres
	x100 = (100*xr)/1280
	b1 = LFO(x100,(xr-x100),10)
	b2 = LFO(x100,(xr-x100),19)
	b3 = LFO(0,(yr/2),2)
	b4 = LFO((yr/2),yr,2)
	y = 0
	pass
    
def draw(screen, etc):
    global b1,b2,b3,b4,y,xr,yr,x100
    etc.color_picker_bg(etc.knob5)    
    y = etc.audio_in[50] / 150
    
    #create many so the random colors are different....
    color = etc.color_picker(etc.knob4)
    color2 = etc.color_picker(etc.knob4)
    color3 = etc.color_picker(etc.knob4)
    color4 = etc.color_picker(etc.knob4)
    
    size1 = int(etc.knob1 * x100) +1
    size2 = int(etc.knob2 * (x100/2)) +1
    
    b1.step = int(etc.knob3 * ((15*xr)/1280))+5
    b2.step = int(etc.knob3 * ((30*xr)/1280))+5
    b3.step = int(etc.knob3 * (x100/20))+2
    b4.step = int(etc.knob3 * (x100/20))+2

    posx1 = b1.update()
    posx2 = b2.update()
    posy1 = b3.update()
    posy2 = b4.update()
    
    pygame.draw.line(screen, color3, [0, posy1], [xr, posy1], size2)
    pygame.draw.line(screen, color4, [0, posy2], [xr, posy2], size2) 
    pygame.draw.line(screen, color, [posx1, (yr/4)-y], [posx1, (yr/2)], size1)
    pygame.draw.line(screen, color2, [posx2, (yr/2)], [posx2, (yr*0.75)+y], size1)
