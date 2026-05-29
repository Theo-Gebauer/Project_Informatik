from pgzero.actor import Actor
import global_var
import random


#Actors


#Methods
    #action on mouse
def mouse_alchemy(button,pos):
    if button == 1 and global_var.button_pressed(pos,665 + global_var.absolutex,630 + global_var.absolutey,180,100):
        global_var.scene = 3
    pass

    #update
def update_alchemy():
    pass

    #draw
def draw_alchemy():
    pass

