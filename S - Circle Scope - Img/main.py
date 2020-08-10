import os
import pygame
import time
import random
import glob
import math

last_point = []
lx = 0
ly = 0
images = []
image_index = 0

def setup(screen, etc):
    global images,xr,yr,last_point
    xr =etc.xres
    yr =etc.yres
    last_point = [0, (yr/2)]
    
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert_alpha()
        images.append(img)

def draw(screen, etc):
    global last_point,xr,yr
    etc.color_picker_bg(etc.knob5)
    for i in range(0, 50) :
        seg(screen, etc, i)   
    
def seg(screen, etc, i):
    global last_point, images, lx, ly,xr,yr
    
    xoffset = 0
    y1 = int(etc.knob2 * yr) + ((etc.audio_in[i]* 0.00003058)*(yr/2))
    x = i * (xr/98)#13
    color = etc.color_picker(etc.knob4)

    R = (etc.knob2*((400*xr)/1280))-((200*xr)/1280)
    R = R + (etc.audio_in[i] / 100)
    x = R * math.cos((i /  50.) * 6.28) + (xr/2)
    y = R * math.sin((i /  50.) * 6.28) + (yr/2)
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], int(etc.knob3*10)+1)
    ly = y
    lx = x

    image = images[0]
    image = pygame.transform.scale(image, (int(image.get_width() * etc.knob1), int(image.get_height() * etc.knob1)) )
    screen.blit(image, (x, y))
