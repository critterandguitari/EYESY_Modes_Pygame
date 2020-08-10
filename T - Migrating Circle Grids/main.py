import os
import pygame

trigger = False

x1=0
y1=0
x2=0
y2=0
x3=0
y3=0
x4=0
y4=0

x_nudge=0
y_nudge=0
x1_nudge=0
y1_nudge=0
x2_nudge=0
y2_nudge=0
x3_nudge=0
y3_nudge=0
x4_nudge=0
y4_nudge=0

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global  x1_nudge, y1_nudge, x2_nudge, y2_nudge, x3_nudge, y3_nudge, x4_nudge, y4_nudge, trigger, x1, y1, x2, y2, x3, y3, x4, y4
    etc.color_picker_bg(etc.knob5)    
    xr = etc.xres
    yr = etc.yres
    xhalf = xr/2
    yhalf = yr/2
    rad50 = ((50*xr)/1280)
    speed60 = ((60*xr)/1280)

    #set different speeds for 4 layers
    x1_nudge = 1*x1_nudge
    y1_nudge = 1*y1_nudge
    x2_nudge = 1.25*x1_nudge
    y2_nudge = 1.25*y1_nudge
    x3_nudge = 1.5*x1_nudge
    y3_nudge = 1.5*y1_nudge
    x4_nudge = 1.75*x1_nudge
    y4_nudge = 1.75*y1_nudge

    x_speed = (speed60*etc.knob1)-(speed60/2) #horizontal speed on knob1
    y_speed = (speed60*etc.knob2)-(speed60/2) #vertical speed on knob2

    #move circles on audio trigger
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        x1_nudge = (x1_nudge + x_speed)
        y1_nudge = (y1_nudge + y_speed)
        x2_nudge = (x2_nudge + x_speed)
        y2_nudge = (y2_nudge + y_speed)
        x3_nudge = (x3_nudge + x_speed)
        y3_nudge = (y3_nudge + y_speed)
        x4_nudge = (x4_nudge + x_speed)
        y4_nudge = (y4_nudge + y_speed)
        
    trigger = False
    if x1_nudge > xhalf : x1_nudge = -xhalf
    if x2_nudge > xhalf : x2_nudge = -xhalf
    if x3_nudge > xhalf : x3_nudge = -xhalf
    if x4_nudge > xhalf : x4_nudge = -xhalf
    
    if x1_nudge < -xhalf : x1_nudge = xhalf
    if x2_nudge < -xhalf : x2_nudge = xhalf
    if x3_nudge < -xhalf : x3_nudge = xhalf
    if x4_nudge < -xhalf : x4_nudge = xhalf
    
    if y1_nudge > yhalf : y1_nudge = -yhalf
    if y2_nudge > yhalf : y2_nudge = -yhalf
    if y3_nudge > yhalf : y3_nudge = -yhalf
    if y4_nudge > yhalf : y4_nudge = -yhalf
    
    if y1_nudge < -yhalf : y1_nudge = yhalf
    if y2_nudge < -yhalf : y2_nudge = yhalf
    if y3_nudge < -yhalf : y3_nudge = yhalf
    if y4_nudge < -yhalf : y4_nudge = yhalf
    
    #define 4 circle grid layers, circle size on knob3:
    for i in range(0, 3) :
         
        for j in range(0, 5) :
            x1 = (j*(xr/5))+(xr/10)+int(x1_nudge)
            y1 = (i*(yr/3))+(yr/6)+int(y1_nudge)
               
            restRad = int(rad50*etc.knob3)+2
            color = etc.color_picker(etc.knob4)
            if (i%2) == 1 : 
                x1 = j*(xr/5)+(xr/10)+int(x1_nudge)
            if (j%2) == 1 : 
                y1 = i*(yr/3)+(yr/6)+int(y1_nudge)
           
            pygame.draw.circle(screen, color, [x1, y1], restRad)
  
    for i in range(0, 3) :
         
        for j in range(0, 5) :
            x2 = (j*(xr/5))+(xr/10)+int(x2_nudge)
            y2 = (i*(yr/3))+(yr/6)+int(y2_nudge)
            
            restRad = int(rad50*etc.knob3)+2
            color = etc.color_picker(etc.knob4)
            if (i%2) == 1 : 
                x2 = j*(xr/5)+(xr/10)+int(x2_nudge)
            if (j%2) == 1 : 
                y2 = i*(yr/3)+(yr/6)+int(y2_nudge)
        
            pygame.draw.circle(screen, color, [x2, y2], restRad)    
    
    for i in range(0, 3) :
         
        for j in range(0, 5) :
            x3 = (j*(xr/5))+(xr/10)+int(x3_nudge)
            y3 = (i*(yr/3))+(yr/6)+int(y3_nudge)
            
            restRad = int(rad50*etc.knob3)+2
            color = etc.color_picker(etc.knob4)
            if (i%2) == 1 : 
                x3 = j*(xr/5)+(xr/10)+int(x3_nudge)
            if (j%2) == 1 : 
                y3 = i*(yr/3)+(yr/6)+int(y3_nudge)
        
            pygame.draw.circle(screen, color, [x3, y3], restRad)
 
    for i in range(0, 3) :
         
        for j in range(0, 5) :
            x4 = (j*(xr/5))+(xr/10)+int(x4_nudge)
            y4 = (i*(yr/3))+(yr/6)+int(y4_nudge)
            
            restRad = int(rad50*etc.knob3)+2
            color = etc.color_picker(etc.knob4)
            if (i%2) == 1 : 
                x4 = j*(xr/5)+(xr/10)+int(x4_nudge)
            if (j%2) == 1 : 
                y4 = i*(yr/3)+(yr/6)+int(y4_nudge)
        
            pygame.draw.circle(screen, color, [x4, y4], restRad)
