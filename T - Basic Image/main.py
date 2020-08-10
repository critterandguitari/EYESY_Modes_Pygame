import os
import pygame
import glob

#important! make sure images are scaled to display resolution beforehand; smaller is faster
images = []
image_index = 0
fall = 0
scoot = 0
bg = pygame.Surface((656,416))
waiting = 0 
xr = 320
yr = 240

def setup(screen, etc) :
    global images, fall, bg, xr, yr
    xr = etc.xres
    yr = etc.yres
    
    bg = pygame.Surface((xr,yr))

    for filepath in sorted(glob.glob(etc.mode_root + '/Images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)

def draw(screen, etc) :
    global images, image_index, fall, bg, scoot, waiting, xr, yr
    etc.color_picker_bg(etc.knob5)    
    above = False
    
    if waiting == 0 :
        for i in range(0, 100) :
            if abs(etc.audio_in[i]) > 1000 :
                above = True
                waiting = 4
    else :
        waiting -= 1
  
    if etc.audio_trig or etc.midi_note_new :
        image_index += 1
        if image_index == len(images) : image_index = 0
        img = images[image_index]
        ximg = int(img.get_width() * etc.knob3)
        yimg = int(img.get_height() * etc.knob3)
        img = pygame.transform.scale(img, (ximg, yimg) )
        
        img.fill((255, 255, 255, etc.knob4 * 255), None, pygame.BLEND_RGBA_MULT)

        y = int(etc.knob2 * yr) - int(img.get_height() * .5)
        x = int(etc.knob1 * xr) - int(img.get_width() * .5)
        screen.blit(img, (x,y))
