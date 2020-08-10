import os
import pygame

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    etc.color_picker_bg(etc.knob5)
    xr = etc.xres
    yr = etc.yres
    lineWidth = int(xr/960)
    
    if lineWidth <= 1 :
        lineWidth = 1
        
    for i in range(0, 7) :
        xoffset = int(etc.knob1*(xr/8))
        yoffset = int(etc.knob2*(yr/5))
        
        for j in range(0, 10) :
            x = (j*(xr/8))-(xr/8)
            y = (i*(yr/5))-(yr/5)
            rad = abs( (etc.audio_in[j-i] * 0.00003058) * (xr*0.5) )
            width = int(etc.knob3*(80*xr)/1280)+1
            color = etc.color_picker(etc.knob4)
            
            if (i%2) == 1 : 
                x = j*(xr/8)-(xr/8)+xoffset
            if (j%2) == 1 : 
                y = i*(yr/5)-(yr/5)+yoffset
                
            points = [((x-width)-rad, (y+width)+rad), (x, (y-width)-rad), ((x+width)+rad, (y+width)+rad)]
            pygame.draw.polygon(screen, color, points,lineWidth) 
