import os
import pygame
import math
import time

last_point = [240, 160]
y1 = 640
x = 640
width = 25
XR = 320
YR = 240

def setup(screen, etc):
    global XR, YR
    XR = etc.xres
    YR = etc.yres
    pass

def draw(screen, etc):
    global last_point, x, y1, width, XR, YR
    etc.color_picker_bg(etc.knob5) 
    for i in range(0, 10) :
        seg(screen, etc, i)   

def seg(screen, etc, i):
    global last_point, x, y1, width, XR, YR
    
    audioraty = ((100*720)/YR)
    audioratx = ((150*1280)/XR)
    speedrat = ((20*XR)/1280)
    y1 = int(etc.knob2 * YR) + (etc.audio_in[i] / audioraty)
    width = (etc.audio_in[i] / audioratx)+3
    sel = etc.knob4*9
    Cmod = etc.knob3
    
    if 1 > sel :
        color = (int(127 + 127 * math.sin(i * 1*Cmod + time.time())),
                int(127 + 127 * math.sin(i * 1*Cmod + time.time())),
                int(127 + 127 * math.sin(i * 1*Cmod + time.time())))
    if 1 <= sel < 2 :
        color = (int(127+127 * math.sin(i * 1*Cmod + time.time())),0,45)
    if 2 <= sel < 3 :
        color = (255,int(155 + 100 * math.sin(i * 1*Cmod + time.time())),30)
    if 3 <= sel < 4 :
        color = (0,75,int(127 + 127 * math.sin(i * 1*Cmod + time.time())))
    if 5 > sel >= 4 :
        color = (int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())),
                int(127 + 127 * math.sin(i * (Cmod+.05) + time.time())),
                int(127 + 127 * math.sin(i * (Cmod+.01) + time.time())))
    if 6 > sel >= 5 :
        color = (127*Cmod,
                127*Cmod,
                int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())))
    if 7 > sel >= 6 :
        color = (127*Cmod,
                int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())),
                127*Cmod)
    if 8 > sel >= 7 :
        color = (int(127 + 127 * math.sin(i * (Cmod+.1) + time.time())),
                127*Cmod,
                127*Cmod)
    if  sel >= 8 :
        color = (int(127 + 127 * math.sin((i+30) * (1*Cmod+.01) + time.time())),
                int(127 + 127 * math.sin((i+30) * (.5*Cmod+.005) + time.time())),
                int(127 + 127 * math.sin((i+15) * (.1*Cmod+.001) + time.time())))

    pygame.draw.line(screen, color, last_point, [x, y1], width)
    
    speed = int(etc.knob1 * (2*speedrat)) - speedrat
    x = x + speed
    if x >= XR: x = 0
    if 0 > x : x = XR
    last_point = [x, y1]
