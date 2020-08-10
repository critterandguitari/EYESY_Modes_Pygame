import os
import pygame
import random

trigger = False
pos = [(random.randrange(640,642),random.randrange(360,362)) for i in range(0,12)]
xr = 320
yr = 240
xhalf = 160
yhalf = 120

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

denser = LFO(1,360,10)

def setup(screen, etc):
	global xr, yr, xhalf, yhalf
	xr = etc.xres
	yr = etc.yres
	xhalf = (xr/2)
	yhalf = (yr/2)
	pos = [(random.randrange(xhalf,xhalf+2),random.randrange(yhalf,yhalf+2)) for i in range(0,12)]
	denser.max = yhalf
	pass

def draw(screen, etc):
    global trigger, pos, xr, yr, xhalf, yhalf
    etc.color_picker_bg(etc.knob5)   
    balls = int(etc.knob2*10)+1
    denser.step = int(etc.knob3*12)
    x20 = ((20*xr)/1280)
    xdensity = denser.update()*2
    ydensity = denser.update()
    size = abs(int(etc.knob1*x20)*denser.update()/30+1)
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True :
        pos = [(random.randrange(abs(xhalf-xdensity),abs((xhalf+2)+xdensity+10)),random.randrange(abs(yhalf-ydensity),abs((yhalf+2)+ydensity+10))) for i in range(0,12)]
    
    for i in range (0, balls):
        color = etc.color_picker(etc.knob4)
        pygame.draw.circle(screen,color,pos[i],size, 0)

    trigger = False
