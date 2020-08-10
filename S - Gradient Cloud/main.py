import pygame
import random
import time
import math
import pygame.gfxdraw

#knob1 = cloud x position ; knob2 = cloud y position ; knob3 = pattern shape and swell range ; knob4 = gradient select

def setup(screen, etc):
    pass

def draw(screen, etc):
	etc.color_picker_bg(etc.knob5)
	xr = etc.xres
	x240 = ((240*xr)/1280)
	xhalf = xr/2
	yr = etc.yres
	yhalf = yr/2
	y480 = ((480*yr)/720)
	xpos1 = int(etc.knob1*4*x240)-2*x240
	cool = yhalf
	sel = etc.knob4*5
    
	if sel < 1 : #grayscale
		for i in range(cool): 
			xpos = x240 + int(xhalf*math.sin(.5 + time.time())*etc.knob3)
			ypos = int(etc.knob2*y480) + etc.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time()))
			color = (int(128 + 127 * math.sin(i * .02 + time.time())),
					int(127 + 127 * math.sin(i * .02 + time.time())),
					int(127 + 127 * math.sin(i * .02 + time.time())))
			radius = int((30 + 20 * math.sin(i*etc.knob3 * 3 + time.time()))*yr)/720
			xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
			pygame.gfxdraw.filled_circle(screen, xpos+xpos1, i+ypos, radius, color)   
            
	if 1 <= sel < 2 : #red
		for i in range(cool):
			xpos = x240 + int(xhalf*math.sin(.5 + time.time())*etc.knob3)
			ypos = int(etc.knob2*y480) + etc.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time()))
			color = (int(128 + 127 * math.sin(i * .02 + time.time())), 0, 0)
			radius = int((30 + 20 * math.sin(i*etc.knob3 * 3 + time.time()))*yr)/720
			xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
			pygame.gfxdraw.filled_circle(screen, xpos+xpos1, i+ypos, radius, color)
            
	if 2 <= sel < 3 : #green
		for i in range(cool):
			xpos = x240 + int(xhalf*math.sin(.5 + time.time())*etc.knob3)
			ypos = int(etc.knob2*y480) + etc.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time()))
			color = (0, int(127 + 127 * math.sin(i * .012 + time.time())), 0)
			radius = int((30 + 20 * math.sin(i*etc.knob3 * 3 + time.time()))*yr)/720
			xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
			pygame.gfxdraw.filled_circle(screen, xpos+xpos1, i+ypos, radius, color)        
    
	if 3 <= sel < 4 : #blue
		for i in range(cool):
			xpos = x240 + int(xhalf*math.sin(.5 + time.time())*etc.knob3)
			ypos = int(etc.knob2*y480) + etc.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time()))
			color = (0, 0, int(127 + 127 * math.sin(i * .012 + time.time())))
			radius = int((30 + 20 * math.sin(i*etc.knob3 * 3 + time.time()))*yr)/720
			xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
			pygame.gfxdraw.filled_circle(screen, xpos+xpos1, i+ypos, radius, color)
            
	if 4 <= sel : #rainbow
		for i in range(cool):
			xpos = x240 + int(xhalf*math.sin(.5 + time.time())*etc.knob3)
			ypos = int(etc.knob2*y480) + etc.audio_in[i%99]/100 + int(30* math.cos(1 * 1 + time.time()))
			color = (int(128 + 127 * math.sin(i * .02 + time.time())),
					int(127 + 127 * math.sin(i * 1 + time.time())),
					int(127 + 127 * math.sin(i * .012 + time.time())))
			radius = int((30 + 20 * math.sin(i*etc.knob3 * 3 + time.time()))*yr)/720
			xpos = int(xr / 2 + xpos * math.sin(i * 1 + time.time()))
			pygame.gfxdraw.filled_circle(screen, xpos+xpos1, i+ypos, radius, color)
