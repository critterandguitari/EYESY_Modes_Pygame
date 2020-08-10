import os
import pygame
import pygame.gfxdraw

triangles = 10

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

yposr = LFO(-100,830,10)
tris = LFO(2,70,1)

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    etc.color_picker_bg(etc.knob5)    
    color = etc.color_picker(etc.knob4) #on knob4
    yposr.max = ((830*etc.xres)/1280)
    tris.max = ((60*etc.xres)/1280)
    tris.step = int(etc.knob1*((15*etc.xres)/1280))
    triangles = tris.update()+2
    space = (etc.xres/(triangles))
    offset = int((etc.knob2*2-1)*space*4)
    yposr.step = int(etc.knob3*((72*etc.yres)/720))
    y = yposr.update()
    
    for i in range (0,triangles) :
        
        auDio = int(etc.audio_in[i] / 65)
        ax = i * space
        pygame.gfxdraw.filled_trigon(screen, ax, y, ax+int((space/2)+offset),auDio+y, ax + space, y, color)
