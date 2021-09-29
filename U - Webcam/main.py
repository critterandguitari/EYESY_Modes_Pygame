"""
ETC Mode that streams a webcam.

Controls:
- Knob 1 and Knob 4 control the colors for masking/keying the picture
- Knob 2 rotates the picture
- Knob 3 controls the movement speed
- Knob 5 controls the background color (default)
- Trigger manipulate the webcam hue and add some wiggling

If camera can not be found or not be opened, it will use a static png instead.

Tested: EYESY OS 2.1 on Organelle M

# Copyright notice:
# This mode is dedicated to the public domain: [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en)
"""
import pygame
import pygame.camera
import time
import random
import subprocess

pygame.camera.init()
CAM = ((pygame.camera.list_cameras() or [""])[0], (160, 120))

BLACK = pygame.Color(0, 0, 0)
X_CENTER = 1280 / 2
Y_CENTER = 720 / 2


def setup(screen, etc):
    etc.capture = Capture(etc)


def draw(screen, etc):
    etc.color_picker_bg(etc.knob5)
    etc.capture.get_and_flip(screen, etc)


class Capture(object):
    def __init__(self, etc):
        self.size = CAM[1]
        self.cam = pygame.camera.Camera(*CAM)
        self.static = None
        self.snapshot = pygame.surface.Surface(self.size, 0)
        self.masked = pygame.surface.Surface(self.size, 0)
        self.out = pygame.surface.Surface((etc.xres, etc.yres), 0)
        self.out.set_colorkey(BLACK) 

        # Count triggers
        self.triggers = 0
        self.scale = (etc.xres / self.size[0]) * 0.3  # full size uses too much cpu
        self.threshold = pygame.Color(0, 0, 0, 255)
        self.thr_color = pygame.Color(0, 0, 0, 255)

        # Start camera
        try:
            self.cam.start()
            self.static = None
        except SystemError:
            # camera not available
            self.static = pygame.image.load(etc.mode_root + 'no_camera.png')
            self.static.convert()
            self.triggers += 1

    def get_and_flip(self, screen, etc):

        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)
        elif self.static is not None:
            self.snapshot = self.static.copy()

        self.threshold.hsla = ((etc.knob4 * 360, 50, 50))
        self.thr_color.hsla = (360, etc.knob1 * 100, 50)
        pygame.transform.threshold(
                self.masked, 
                self.snapshot, 
                self.thr_color,
                self.threshold, 
                etc.bg_color,
                2,
        )
        
        if etc.audio_trig or etc.midi_note_new:
            direction = 1
            self.triggers += 1
            self.triggers %= 8
            if random.random() > .5:
                hue = random.randint(-127, 127)
                if self.static is None:
                    subprocess.Popen(
                        "v4l2-ctl -d {} --set-ctrl=hue={}".format(CAM[0], hue).split()
                    )
        else:
            direction = -1

        if self.triggers == 0:
            self.scale = (etc.xres / self.size[0]) * random.randint(12, 45) / 100.

        rotation = etc.knob2 * 360 * direction

        self.out.fill(etc.bg_color)
        self.out.blit(
            pygame.transform.rotozoom(
                self.masked, 
                rotation, 
                self.scale
            ), 
            (0, 0)
        )

        factor = -1 if self.triggers < 4 else 1
        _time = int(time.time() * (100 * etc.knob3))  # speed of movement
        X = (etc.xres / 2) - self.size[0] * self.scale * .5 - (_time % (etc.xres / 2)) * factor
        Y = (etc.yres / 2) - self.size[1] * self.scale * .5 - (_time % (etc.yres / 2)) * factor
        screen.blit(self.out, (X, Y))
