from pgzero.actor import Actor
import global_var
import random


#Actors


#Methods
    #action on mouse
def mouse_greenhouse(button,pos):
    if button == 1 and global_var.button_pressed(pos,975 + global_var.absolutex,-20 + global_var.absolutey,125,110):
        global_var.scene = 2

    #update
def update_greenhouse():
    pass

    #draw
def draw_greenhouse():
    pass


