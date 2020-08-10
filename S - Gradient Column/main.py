import pygame
import random
import time
import math
import pygame.gfxdraw

def setup(screen, etc):
    global xr,yr,x12
    xr = etc.xres
    yr = etc.yres
    x12 = (12*xr)/1280
    pass

def draw(screen, etc):
    global xr,yr,x12
    etc.color_picker_bg(etc.knob5)
    cool = int(etc.knob1*(yr-10))+10 # number of circles and height
    yoff = int((yr/2)-etc.knob1*(yr/2))
    xtra = int(etc.knob2*(xr-2))+2 # width control
    segs = 99 # number of audio data points to look at
    sel  = etc.knob4*5 # color select switch
    swell = etc.knob3*.999 + .001 # radius and scope shape
    
    if 0 <= sel < 1 : #grayscale
        for i in range(cool):
            audiopuff = int((etc.audio_in[i%segs]*0.00003058)*(yr/2))
            Naudiop = audiopuff * -1
            color = (int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())))
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, (i)+yoff, abs(radius), color)            
    
    if 1 <= sel < 2 :    # red
        for i in range(cool):
            audiopuff = int((etc.audio_in[i%segs]*0.00003058)*(yr/2))
            color = (int(127 + 127 * math.sin(i * .005 + time.time())),
                    0,
                    0)
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, i+yoff, abs(radius), color)
    
    if 2 <= sel < 3 :    # green    
        for i in range(cool):
            audiopuff = int((etc.audio_in[i%segs]*0.00003058)*(yr/2))
            color = (0,
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    0)
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, i+yoff, abs(radius), color)
    
    if 3 <= sel < 4 :        # blue
        for i in range(cool):
            audiopuff = int((etc.audio_in[i%segs]*0.00003058)*(yr/2))
            color = (0,
                    0,
                    int(127 + 127 * math.sin(i * .02 + time.time())))
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, i+yoff, abs(radius), color)    
            
    if 4 <= sel :        # rainbow
        for i in range(cool):
            audiopuff = int((etc.audio_in[i%segs]*0.00003058)*(yr/2))
            color = (int(127 + 127 * math.sin(i * .005 + time.time())),
                    int(127 + 127 * math.sin(i * .01 + time.time())),
                    int(127 + 127 * math.sin(i * .02 + time.time())))
            radius = int(x12 + x12 * math.sin(i * .1*swell + time.time()))
            xpos = int(((xr/2) - xtra/144) + (xtra/2) * math.sin(i * 2.5 + time.time()))
            pygame.gfxdraw.filled_circle(screen, xpos+audiopuff, i+yoff, abs(radius), color)
