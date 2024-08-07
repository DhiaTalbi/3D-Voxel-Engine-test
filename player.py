import pygame as pg
from camera import Camera
from settings import *

class Player(Camera):
    def __init__(self,app,position=PLAYER_POS,yaw=-90,pitch=0):
        self.app = app
        super().__init__(position,yaw,pitch)

    def update(self):
        self.keyboard_controls()
        self.mouse_controls()
        super().update()

    def mouse_controls(self):
        mouse_dx, mouse_dy, = pg.mouse.get_rel()
        if mouse_dx :
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENS)
        if mouse_dy :
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENS)

    def keyboard_controls(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_SPEED * self.app.delta_time

        if key_state[pg.K_z]:
            self.move_forward(vel)
        if key_state[pg.K_q]:
            self.move_left(vel)
        if key_state[pg.K_s]:
            self.move_backward(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
