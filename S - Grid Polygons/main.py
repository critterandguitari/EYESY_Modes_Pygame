import os
import pygame
import random
pList = []
raNr = 0
trigger = False

def setup(screen, etc) :
    global xr, yr, x8, y5, pList, raNr, NraNr, ten, hundert, hten
    xr = etc.xres
    yr = etc.yres
    raNr = (20*xr)/1280
    NraNr = raNr* -1
    x8 = xr/8
    y5 = yr/5
    pList = [[(random.randrange(NraNr,raNr),random.randrange(NraNr,raNr)) for i in range(0,6)] for i in range(0,70)]
    ten = (10*xr)/1280
    hten = ten/2
    hundert = (100*xr)/1280
    pass

def draw(screen, etc) :
    global trigger, pList, xr, yr, x8, y5, pList, raNr, NraNr, ten, hundert, hten
    etc.color_picker_bg(etc.knob5)    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    if trigger == True :
        pList = [[(random.randrange(NraNr,raNr),random.randrange(NraNr,raNr)) for i in range(0,6)] for i in range(0,70)]
    trigger = False
    
    for i in range(0, 7) :
        xoffset = int(etc.knob1*x8)
        yoffset = int(etc.knob2*y5)
         
        for j in range(0, 10) :
            x = (j*(x8))-(x8)
            y = (i*(y5))-(y5)
            rad = (etc.audio_in[j+i]*0.00003052)*hundert
            w = (etc.knob3*4)+1
            color = etc.color_picker(etc.knob4)
            if (i%2) == 1 : 
                x = j*(x8)-(x8)+xoffset
            if (j%2) == 1 : 
                y = i*(y5)-(y5)+yoffset
            points = [pList[(i*j)+hten][t] for t in range(0,6) ]
            placePoints = [((points[k][0]*w)+x,(points[k][1]*w)+y) for k in range(0,6)]
            morphPoints = [(placePoints[0][0]-rad,placePoints[0][1]-rad),
                           (placePoints[1][0]+rad,placePoints[1][1]-rad),
                           (placePoints[2][0]+rad,placePoints[2][1]),
                           (placePoints[3][0]+rad,placePoints[3][1]+rad),
                           (placePoints[4][0],placePoints[4][1]-rad),
                           (placePoints[5][0]-rad,placePoints[5][1]+rad)]
            
            pygame.draw.polygon(screen, color, morphPoints, 1)
