import os
import pygame
import time
import random
import glob
#REMEMBER TO SCALE YOUR IMAGES RELATIVE TO SCREEN RESOLUTION; Large images will cause lag!!
images = []
image_index = 0
image_x=100
image_y=100
image_size_x=100
image_size_y=100
circle_x=100
circle_y=100
circle_size = 50
trigger = False
xr = 320
yr = 240

def setup(screen, etc):
    global images, image_index, xr, yr
    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)
        
        xr = etc.xres
        yr = etc.yres

def draw(screen, etc):
    global trigger, image_x, image_y, circle_x, circle_y, circle_size, image_size_x, image_size_y, images, image_index, xr, yr
    etc.color_picker_bg(etc.knob5)
    color = etc.color_picker(etc.knob4)

    if etc.audio_trig or etc.midi_note_new :
        trigger = True
    
    if trigger == True : 
        image_x=(random.randrange(-((50*xr)/1280),((1080*xr)/1280)))
        image_y=(random.randrange(-((50*xr)/1280),((600*xr)/1280)))
        image_index += 1
        if image_index == len(images) : image_index = 0
    
    image = images[image_index]
        
    image_size_x=int(image.get_width() * etc.knob1)
    image_size_y=int(image.get_height() * etc.knob1)
    
    image = pygame.transform.scale(image,(image_size_x, image_size_y))
        
    circle_size = int(etc.knob2*image_size_x/1.5) #you can change this number if you want max. circle size to be bigger or smaller
    pygame.draw.circle(screen,color,[image_x+(int(image.get_width()/2)),image_y+(int(image.get_height()/2))],circle_size, 0)
    
    image.fill((255, 255, 255, etc.knob3 * 255), None, pygame.BLEND_RGBA_MULT)

    screen.blit(image, (image_x,image_y))
    
    trigger = False
