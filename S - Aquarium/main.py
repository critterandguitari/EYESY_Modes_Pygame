import os
import pygame
import random

speedList = [random.randrange(-1,1)+.1 for i in range(0,20)]
yList = [random.randrange(-50,770) for i in range(0,20)]
widthList = [random.randrange(20,200) for i in range(0,20)]
countList = [i for i in range(0,20)]
xden = 1
yden = 1
trigger = False

def setup(screen, etc) :
    pass

def draw(screen, etc) :
    global trigger, yList, widthList, countList, speedList, xden, yden
    etc.color_picker_bg(etc.knob5)    
    color = etc.color_picker(etc.knob4) #on knob4
    widthmax = int((200*etc.xres)/1280)
    
    if yden != (int(etc.knob1 * 19) + 1) :
        yden = (int(etc.knob1 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,(etc.yres+50)) for i in range(0,20)]
        widthList = [random.randrange(20,widthmax) for i in range(0,20)]

    if xden != (int(etc.knob2 * 19) + 1) :
        xden = (int(etc.knob2 * 19) + 1)
        speedList = [random.randrange(-2,2)+.1 for i in range(0,20)]
        yList = [random.randrange(-50,(etc.yres+50)) for i in range(0,20)]
        widthList = [random.randrange(20,widthmax) for i in range(0,20)]
        
    for i in range (0,yden) :
        
        y0 = yList[i]
        ymod = ((500*720)/etc.yres)
        
        for j in range (0,xden) :
            width = widthList[i]
            y1 = y0 + (etc.audio_in[j+i] / ymod)
            countList[i] = countList[i] + speedList[i]
            modSpeed = countList[i]%(etc.xres+width*2)
            x = (j * (width/5)) + (modSpeed-width)
            pygame.draw.line(screen, color, [x, y1], [x, y0], int(etc.knob3*((100*etc.xres)/1280)+1))
    
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    trigger = False
