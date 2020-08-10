import os
import pygame
import random
import pygame.gfxdraw

num = 25
clench = 0
teeth = 1
toff = 1
last_screen = pygame.Surface((1280,720))
r=0
g=0
b=0
counter = 0

def setup(screen, etc) :
    pass

def draw(screen, etc) : 
    global last_screen, r, g, b, counter
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    xrSm = xr - 100*xr/1280
    yr = etc.yres
    yrSm = yr - 100*yr/720
    
    #screengrab feedback loop
    image = last_screen
    last_screen = screen.copy()
    thing = pygame.transform.scale(image,((xrSm),(yrSm))) #scales down screengrab
    screen.blit(thing, (50,50)) #re-centers screengrab
   
    #color shift amount control
    colorshift = int(etc.knob4 * 20)+1
    r= (r+colorshift)%255
    g= (g+colorshift)%255
    b= (b+colorshift)%255
    color = (r,g,b)
    
    #teeth and clench
    teeth = int(etc.knob1 * 10)
    teethwidth = int((1280-128*teeth)*xr)/1280
    if teethwidth == 0 : teethwidth = ((128*xr)/1280)
    clench = int(etc.knob3 * ((200*xr)/1280)) - teethwidth/2
    if teethwidth > xr/2 : clench = int(etc.knob1*((200*xr)/1280))-500
    shape = int(etc.knob2*3)
    if shape < 1 : clench = int(etc.knob1*((200*xr)/1280)) - 100
    
    #top row
    for i in range(0, 10) :
        
        x = (i * teethwidth)+teethwidth/2
        y0 = 0
        audioL = abs(etc.audio_in[i] / 85)      #AUDIO IN L
        y1 = y0 + audioL + clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1+teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)    
    
    #bottom row
    for i in range(10, 20) :
        x = ((i-10) * teethwidth) + teethwidth/2
        y0 = yr
        audioR = abs(etc.audio_in[i] / 85)      #AUDIO IN R
        y1 = y0 - audioR - clench
        pygame.draw.line(screen, color, [x, y0], [x, y1], teethwidth)
        if shape == 1 :
            pygame.gfxdraw.filled_trigon(screen, x-teethwidth/2, y1, x, y1-teethwidth/2, x+teethwidth/2, y1, color)
        if shape >= 2 :
            pygame.gfxdraw.filled_circle(screen, x, y1, teethwidth/2, color)
    
    #counter for color shift
    counter+=1
    if counter == 75:
        r = random.randrange(0,254)
        g = random.randrange(0,254)
        b = random.randrange(0,254)
        counter = 0
