import pygame
import random
import time
import math
import pygame.gfxdraw
# knob1 = x pos ; knob2 = y pos ; knob3 = length ; knob4 = color select
def setup(screen, etc):
    pass 

def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    yr = etc.yres
    xr = etc.xres
    sel = etc.knob4*5
    i = ((180*yr)/720)
    
    if 0 <= sel < 1 :    #grayscale
        for i in range(i):
            push = abs(int(etc.knob3*etc.audio_in[i%24]/360))    
            boing = int(etc.knob3*i)+etc.audio_in[1]/500
            i = boing
            color = (int(128 + 127 * math.sin(i * .02 + time.time())),
                    int(127 + 127 * math.sin(i * .02 + time.time())),
                    int(127 + 127 * math.sin(i * .02 + time.time())))
            radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
            xpos = int(((1080*etc.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/1280
            ypos = int(((((2*etc.knob2-1)/2*720+360))-int(i*etc.knob2))*yr)/720-4*i
            pygame.gfxdraw.filled_circle(screen, xpos, ypos-boing, radius+1, color)        
    
    if 1 <= sel < 2 :       #red
        for i in range(i):
            push = abs(int(etc.knob3*etc.audio_in[i%24]/300))    
            boing = int(etc.knob3*i)+(etc.audio_in[1]/500)
            i = boing
            color = (int(128 + 127 * math.sin(i * .02 + time.time())),0,0,)
            radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
            xpos = int(((1080*etc.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/1280
            ypos = int(((((2*etc.knob2-1)/2*720+360))-int(i*etc.knob2))*yr)/720-4*i
            pygame.gfxdraw.filled_circle(screen, xpos, ypos-boing, radius+1, color)
            
    if 2 <= sel < 3 :    #green
        for i in range(i):
            push = abs(int(etc.knob3*etc.audio_in[i%24]/300))    
            boing = int(etc.knob3*i)+etc.audio_in[1]/500
            i = boing
            color = (0, int(127 + 127 * math.sin(i * .012 + time.time())),0)
            radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
            xpos = int(((1080*etc.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/1280
            ypos = int(((((2*etc.knob2-1)/2*720+360))-int(i*etc.knob2))*yr)/720-4*i
            pygame.gfxdraw.filled_circle(screen, xpos, ypos-boing, radius+1, color)        
    
    if 3 <= sel < 4 :    #blue
        for i in range(i):
            push = abs(int(etc.knob3*etc.audio_in[i%24]/300))    
            boing = int(etc.knob3*i)+etc.audio_in[1]/500
            i = boing
            color = (0, 0,int(127 + 127 * math.sin(i * .012 + time.time())))
            radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
            xpos = int(((1080*etc.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/1280
            ypos = int(((((2*etc.knob2-1)/2*720+360))-int(i*etc.knob2))*yr)/720-4*i
            pygame.gfxdraw.filled_circle(screen, xpos, ypos-boing, radius+1, color)
            
    if 4 <= sel :    #all colors
        for i in range(i):
            push = abs(int(etc.knob3*etc.audio_in[i%24]/300))    
            boing = int(etc.knob3*i)+(etc.audio_in[1]/500)
            i = boing
            color = (int(127 + 127 * math.sin(i*4 * .05 + time.time())),
                    int(127 + 127 * math.sin(i*4 * .018 + time.time())),
                    int(127 + 127 * math.sin(i*4 * .012 + time.time())))
            radius = int(10+push + 10 * math.sin(i * .05 + time.time()))
            xpos = int(((1080*etc.knob1 + 100*math.sin(i * .0006 + time.time()))+100)*xr)/1280
            ypos = int(((((2*etc.knob2-1)/2*720+360))-int(i*etc.knob2))*yr)/720-4*i
            pygame.gfxdraw.filled_circle(screen, xpos, ypos-boing, radius+1, color)
