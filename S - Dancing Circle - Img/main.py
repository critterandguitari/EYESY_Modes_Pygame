import os
import pygame
import time
import random
import glob
import math

last_point = [0, 360]
i = 0
images = []
image_index = 0
lx = 0
ly = 0

def setup(screen, etc):
    global images, xr, yr, last_point
    xr = etc.xres
    yr = etc.yres
    last_point = [0, yr/2]
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point, images, i, lx, ly, xr,yr
    etc.color_picker_bg(etc.knob5)
    x300 = int((300*xr)/1280)
    x30 = int((30*xr)/1280)
    xoffset = 0
    y1 = int(etc.knob2 * yr) + ((etc.audio_in[i]*0.00003058) *(yr/2))
    x = i * (xr/100)
    color = etc.color_picker(etc.knob4)

    R = (etc.knob2*x300)-(x300/2)
    R = R + ((etc.audio_in[i]*0.00003058)*(yr/2))
    x = R * math.cos((i /  100.) * 6.28) + (xr/2)
    y = R * math.sin((i /  100.) * 6.28) + (yr/2)
    
    max_circle = x300
    image_size = 1
    circle_size = 0
    line_width = 0
    if etc.knob3 <=.5 :
        circle_size = int(etc.knob3 * max_circle)
        line_width = 0
    if etc.knob3 >.501 :
        circle_size = abs(max_circle-int(etc.knob3 * max_circle)) 
        line_width =  abs(x30-int(etc.knob3 * x30))
    
    pygame.draw.circle(screen,color,(int(x),int(y)), circle_size, line_width)
    image = images[0]
    image = pygame.transform.scale(image, (int(image.get_width() * etc.knob1), int(image.get_height() * etc.knob1)) )
    screen.blit(image, (x, y))
    
    i = (i + 1) % 100
