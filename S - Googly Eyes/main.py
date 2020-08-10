import os
import pygame
import time
import random
import math

rad = 5
xpos = 300
ypos = 300
color = (0,0,0)
last_point = [320, 0]
last_point1 = [320, 0]

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

lfo1 = LFO(-200,200,1)
lfo2 = LFO(-300,300,1)

def setup(screen, etc) :
    pass

def draw(screen, etc) : 
    global rad, xpos, ypos, color, last_point, last_point1
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    
    lfo1.start = ((xr*-200)/1280)
    lfo1.max = ((xr*200)/1280)
    lfo2.start = ((xr*-300)/1280)
    lfo2.max = ((xr*300)/1280)
    
    xhalf = ((640*xr)/1280)
    x720 = ((720*xr)/1280) #720
    x1116 = ((11*xr)/16)
    
    y3d = (yr/3)
    y600 = ((yr*600)/720)
    y640 = ((640*yr)/720)
    
    color = etc.color_picker(etc.knob4)
    audio1 = etc.audio_in[0] /450
    audio2 = etc.audio_in[1] /450
    widthmod = ((xr*25)/1280)
    linewidth= int(etc.knob1*widthmod)+1
    
    #mouth
    for i in range(0, 100) :
        
        xscale = (xhalf/99*i)
        xoffset = int(xhalf+xscale)*etc.knob2*i/100 + (x720-etc.knob2*xhalf) #mouth width
        yoffset = y600 - etc.audio_in[2]/y640
        auDio = etc.audio_in[i] / (500-int(etc.knob2*499))
        color = etc.color_picker(etc.knob4)
        
        if i == 0 : last_point = [(0*etc.knob2+ -auDio)+ (x720-etc.knob2*xhalf), (yoffset+ auDio)]
        
        pygame.draw.line(screen, color, last_point, [xoffset + -auDio, yoffset + auDio], linewidth)
        last_point = [(xoffset + -auDio),(yoffset + auDio)]
    
    #eyes
    radrat = ((125*xr)/1280)
    rad = int(etc.knob1*radrat)+20 #eye size
    xpos1 = (2*radrat)+audio1
    ypos1 = y3d-audio1
    xpos2 = x1116-audio2
    ypos2 = y3d-audio2
    xrad = (rad/2) * math.sin((etc.audio_in[20]*.0001)) 
    yrad = (rad/2) * math.cos((etc.audio_in[25]*.0001))
    
    step1mod = ((xr*30)/1280)
    step2mod = ((xr*40)/1280)
    lfo1.step = etc.knob3*step1mod #eye bounce speed
    lfo2.step = etc.knob3*step2mod
    roll1 = int(lfo1.update())
    roll2 = -int(lfo1.update())
    slide1 = int(lfo2.update())
    slide2 = -int(lfo2.update())
    
    pygame.draw.circle(screen, color, [xpos1+slide1,ypos1+roll1], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos1+int(xrad)+slide1,ypos1-int(yrad)+roll1], rad/2)
    pygame.draw.circle(screen, color, [xpos2+slide2,ypos2+roll2], rad)
    pygame.draw.circle(screen, (245,200,255), [xpos2+int(xrad)+slide2,ypos2-int(yrad)+roll2], rad/2)
