import os
import pygame
import time
import random
import math

lines = 10 
width = 720 / lines
offset = width / 2
xpos = 0
XR = 320
YR = 240
count = 0

def setup(screen, etc):
    global XR, YR
    XR = etc.xres
    YR = etc.yres
    pass

def draw(screen, etc):
    global lines, offset, width, xpos, count
    etc.color_picker_bg(etc.knob5)
    # star distance on knob1 # line width on knob2 # point angle on knob3 # select color range on knob4
    sel = etc.knob4*5 
    width = XR / lines
    xhalf = (XR/2)
    yhalf = (YR/2)
    yrange = ((300*YR)/720)
    bouncedenom = (300*1280)/XR
    gravity = int(2*XR/3-etc.knob3*4*XR/3)
    
    if 0<= sel <1 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .05+ time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (int(127 + 127 * math.cos((i*6) * .1 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .05 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(xhalf * math.sin(i * 1 + time.time()))+gravity
            xpos1 = int(xhalf*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[25]/bouncedenom)
            bounce2 = int(etc.audio_in[75]/bouncedenom)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [XR/2-xpos1, yhalf-bounce1+ypos1], [XR/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [xhalf+xpos1, yhalf-bounce2-ypos1], [xhalf-xpos+xpos1, (offset + (i * width)-ypos2)], thick)
            count = count+1
    if 1<= sel <2 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        0,
                        0)
        
            color1 =    (0,
                        0,
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(xhalf * math.sin(i * 1 + time.time()))+gravity
            xpos1 = int(xhalf*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[25]/bouncedenom)
            bounce2 = int(etc.audio_in[75]/bouncedenom)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [XR/2-xpos1, yhalf-bounce1+ypos1], [XR/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [xhalf+xpos1, yhalf-bounce2-ypos1], [xhalf-xpos+xpos1, (offset + (i * width)-ypos2)], thick)
        
    if 2<= sel <3 :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        255,
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (255,
                        abs(127+127 * math.cos((i*6) * .01 + time.time())),
                        abs(127+127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(xhalf * math.sin(i * 1 + time.time()))+gravity
            xpos1 = int(xhalf*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[25]/bouncedenom)
            bounce2 = int(etc.audio_in[75]/bouncedenom)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [XR/2-xpos1, yhalf-bounce1+ypos1], [XR/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [xhalf+xpos1, yhalf-bounce2-ypos1], [xhalf-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

    if 3<= sel <4 :
        for i in range(0, lines) :
        
            color2 =    (225,
                        int(127+127 * math.cos((i*6) * .01 + time.time())),
                        255)
        
            color1 =    (255,
                        225,
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(xhalf * math.sin(i * 1 + time.time()))+gravity
            xpos1 = int(xhalf*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[25]/bouncedenom)
            bounce2 = int(etc.audio_in[75]/bouncedenom)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [XR/2-xpos1, yhalf-bounce1+ypos1], [XR/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [xhalf+xpos1, yhalf-bounce2-ypos1], [xhalf-xpos+xpos1, (offset + (i * width)-ypos2)], thick)

    if 4<= sel :
        for i in range(0, lines) :
        
            color2 =    (int(127 + 127 * math.sin((i*6) * .01 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .01+ time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))
        
            color1 =    (int(127 + 127 * math.cos((i*6) * .01 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())),
                        int(127 + 127 * math.cos((i*6) * .01 + time.time())))
        
            xpos = int(xhalf * math.sin(i * 1 + time.time()))+gravity
            xpos1 = int(xhalf*(etc.knob1) * math.sin(10 * .2 + time.time()))
            ypos1 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))
            ypos2 = int(yrange*(etc.knob1) * math.sin(10 * .1 + time.time()))*(etc.audio_in[i]/1000+1)
            bounce1 = int(etc.audio_in[25]/bouncedenom)
            bounce2 = int(etc.audio_in[75]/bouncedenom)
            thick = int(etc.knob2*19)+1
            pygame.draw.line(screen, color1, [XR/2-xpos1, yhalf-bounce1+ypos1], [XR/2-xpos-xpos1, (offset + (i * width)+ypos2)], thick)
            pygame.draw.line(screen, color2, [xhalf+xpos1, yhalf-bounce2-ypos1], [xhalf-xpos+xpos1, (offset + (i * width)-ypos2)], thick)
