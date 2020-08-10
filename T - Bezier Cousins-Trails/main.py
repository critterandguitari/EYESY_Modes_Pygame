import os
import pygame
import random
import pygame.gfxdraw

pointNumber = 20
pOints = [(random.randrange(0,1200), random.randrange(0,600)) for i in range(1, pointNumber)]
trigger = False
pOints.append(pOints[0])
pOints1 = [(640,640), (45,760), (90,90)]
xr = 50
yr = 50

def setup(screen, etc):
	global pOints, trigger, pointNumber, pOints1, xr, yr
	xr = etc.xres
	yr = etc.yres
	x640 = int((640*xr)/1280)
	x45 = int((45*xr)/1280)
	x760 = int((760*xr)/1280)
	x90 = int((90*xr)/1280)
	pointNumber = 20
	pOints = [(random.randrange(0,int((1200*xr)/1280)), random.randrange(0,int((600*yr)/720))) for i in range(1, pointNumber)]
	trigger = False
	pOints.append(pOints[0])
	pOints1 = [(x640,x640), (x45,x760), (x90,x90)]
	pass

def draw(screen, etc):
    
    global pOints, trigger, pointNumber, pOints1, xr, yr
    etc.color_picker_bg(etc.knob5) 
    number = int(etc.knob2*5)
    smooth = 6
    place = int(etc.knob3*((180*xr)/1280)) +10
    
    pOints1 = [(pOints[i][0] - place, pOints[i][1] - place) for i in range(1,pointNumber)]
    pOints1.append(pOints1[0])
    
    pOints2 = [(pOints1[i][0] + place+(place/4), pOints1[i][1] + place+(place/4)) for i in range(1,pointNumber)]
    pOints2.append(pOints2[0])
    
    pOints3 = [(pOints2[i][0] + place+(place/2), pOints2[i][1] - place+(place/2)) for i in range(1,pointNumber)]
    pOints3.append(pOints3[0])
    
    pOints4 = [(pOints3[i][0] - place+(place/1), pOints3[i][1] + place+(place/1)) for i in range(1,pointNumber)]
    pOints4.append(pOints4[0])
    
    
    color = etc.color_picker(etc.knob4)
    if etc.audio_trig or etc.midi_note_new :
        trigger = True
        
    if trigger == True :
        pointNumber = int(etc.knob1*16)+4
        pOints = [(random.randrange(20,int((1240*xr)/1280)), random.randrange(20,int((680*yr)/720))) for i in range(1,pointNumber)]
        pOints.append(pOints[0])
        pOints1 = [(pOints[i][0] + place, pOints[i][1] + place) for i in range(1,pointNumber)]
        pOints1.append(pOints1[0])
        
    trigger = False
    
    pygame.gfxdraw.bezier(screen, pOints, smooth, color)
    if number>1 : 
        pygame.gfxdraw.bezier(screen, pOints1, smooth, color)
    if number>2 : 
        pygame.gfxdraw.bezier(screen, pOints2, smooth, color)
    if number>3 :
        pygame.gfxdraw.bezier(screen, pOints3, smooth, color)
    if number>4 :
        pygame.gfxdraw.bezier(screen, pOints4, smooth, color)
    
    
   #Trails
    #veil = pygame.Surface((1280,720))
    veil = pygame.Surface((xr,yr))  
    veil.set_alpha(int(etc.knob3 * 200))
    veil.fill((etc.bg_color[0],etc.bg_color[1],etc.bg_color[2])) 
    screen.blit(veil, (0,0))
