import os
import pygame
import time
import random
import math

size = 400
count = 0
R = 1
avg = 0
color = (0,0,0)
A=B=C=D=E=F=G=H=I=J=K=5


def setup(screen, etc):
    pass

def draw(screen, etc):
    global size, count, avg, color
    etc.color_picker_bg(etc.knob5)    
    for i in range(0, 100) :
        avg = abs(etc.audio_in[i]) + avg
    avg = avg / 100

    arcs = int(etc.knob1*9+1) #number of layers
    form = int(etc.knob3*6) #shape selector
    sel = int(etc.knob4*7) #color selector
    offset = etc.knob2 #layer offset on knob2, see below
    
    scaler = ((1000*etc.xres)/1280)
    
    
    for i in range(arcs):
        
        if 6 <= sel : #full spectrum
            if arcs < 2 : i = 1
            color =    (int(127 + 127 * math.sin((i*36) * .1 + time.time())),
                        int(127 + 127 * math.sin((i*36) * .05+ time.time())),
                        int(127 + 127 * math.sin((i*36) * .01 + time.time())))
    
        if 1 <= sel < 2 : #red range
            red = 127
            green = 15
            blue = 5
            color =    (int(red+red * math.sin((i*6) * .01 + time.time())),
                        int(green + green * math.cos((i*6) * .03 + time.time())),
                        int(blue + blue * math.sin((i*6) * .01 + time.time())))
        
        if 2 <= sel < 3 : #yellow range
            color =    (int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(115+115 * math.sin((i*6) * .03 + time.time())),
                        int(25 + 25 * math.cos((i*6) * .01 + time.time())))
        
        if 3 <= sel < 4 : #green range
            color =    (int(35+35 * math.cos((i*6) * .01 + time.time())),
                        int(115+115 * math.sin((i*6) * .01 + time.time())),
                        int(25 + 25 * math.sin((i*6) * .01 + time.time())))
                        
        if 4 <= sel < 5 : #blue range
            color =    (int(5+5 * math.tan((i*6) * .01 + time.time()))%75,
                        int(45+45 * math.cos((i*6) * .01 + time.time())),
                        int(115 + 115 * math.sin((i*6) * .01 + time.time())))                
                        
        if 5 <= sel < 6 : #violet range
            color =     (int(100+100 * math.sin((i*6) * .01 + time.time())),
                        int(5+5 * math.sin((i*6) * .01 + time.time())),
                        int(75 + 75 * math.cos((i*6) * .01 + time.time())))
                        
        if sel < 1 : #grayscale
            color =     (int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(127+127 * math.sin((i*6) * .01 + time.time())),
                        int(127 + 127 * math.sin((i*6) * .01 + time.time())))                
    
        if form < 1 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
    
        if 1<=form< 2 :
        
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.sin(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.sin(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))

        if 2 <= form < 3 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
    
        if 3<=form< 4 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.cos(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.sin(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.cos(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            
        if 4<=form < 5 :
            A = abs(avg* 0.026) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.tan(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.sin(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.sin(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.tan(i * .5 + time.time()))
   
        if 5<=form  :
            A = abs(avg* 0.026) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            B = abs(avg* 0.05) + abs(scaler*offset*math.tan(i * .5 + time.time()))    
            C = abs(avg* 0.071)   + abs(scaler*offset*math.cos(i * .5 + time.time())) 
            D = abs(avg* 0.087) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            E = abs(avg* 0.097)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            F = abs(avg* 0.1) + abs(scaler*offset*math.tan(i * .5 + time.time()))
            G = abs(avg* 0.097) + abs(scaler*offset*math.cos(i * .5 + time.time()))
            H = abs(avg*0.087)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            I = abs(avg* 0.071)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            J = abs(avg* 0.05)  + abs(scaler*offset*math.tan(i * .5 + time.time()))
            K = abs(avg* 0.026)+ abs(scaler*offset*math.cos(i * .5 + time.time()))
            
            
        corner = abs(int(etc.audio_in[1]* (etc.knob3*2-1)/2))
    
        x = etc.xres
        y = etc.yres
        
        x22 = ((22*etc.xres)/1280)
        x86 = ((86*etc.xres)/1280)
        x187 = ((187*etc.xres)/1280)
        x320 = ((320*etc.xres)/1280)
        x474 = ((474*etc.xres)/1280)
        x640 = ((640*etc.xres)/1280)
        x806 = ((806*etc.xres)/1280)
        x960 = ((960*etc.xres)/1280)
        x1093 = ((1093*etc.xres)/1280)
        x1194 = ((1194*etc.xres)/1280)
        x1258 = ((1258*etc.xres)/1280)
        
        y12 = ((12*etc.yres)/720)
        y48 = ((48*etc.yres)/720)
        y105 = ((105*etc.yres)/720)
        y180 = ((180*etc.yres)/720)
        y267 = ((267*etc.yres)/720)
        y360 = ((360*etc.yres)/720)
        y453 = ((453*etc.yres)/720)
        y540 = ((540*etc.yres)/720)
        y615 = ((615*etc.yres)/720)
        y672 = ((672*etc.yres)/720)
        y708 = ((708*etc.yres)/720)
       
    #top arc
        pygame.draw.aalines(screen, color, False, [[0, corner], [x22, A], [x86, B], [x187, C], [x320, D], [x474, E], [x640, F], [x806, G], [x960, H], [x1093, I], [x1194, J], [x1258, K], [x, corner]], 1)
    #bottom arc
        pygame.draw.aalines(screen, color, False, [[0, y-corner], [x22, y-A], [x86, y-B], [x187, y-C], [x320, y-D], [x474, y-E], [x640, y-F], [x806, y-G], [x960, y-H], [x1093, y-I], [x1194, y-J], [x1258, y-K], [x,y-corner]], 1)

    #right arc
        pygame.draw.aalines(screen, color, False, [[x+corner, 0], [x-A, y12], [x-B, y48], [x-C, y105], [x-D, y180], [x-E, y267], [x-F, y360], [x-G, y453], [x-H, y540], [x-I, y615], [x-J, y672], [x-K, y708], [x-corner, y]], 1)
    
    #left arc
        pygame.draw.aalines(screen, color, False, [[corner, 0], [A, y12], [B, y48], [C, y105], [D, y180], [E, y267], [F, y360], [G, y453], [H, y540], [I, y615], [J, y672], [K, y708], [corner, y]], 1)
    
    
