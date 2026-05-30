from pgzero.actor import Actor
import global_var
import random


#Actors
background = Actor('greenhouse_background', center = (global_var.WIDTH//2, global_var.HEIGHT//2))
button_leave = Actor('startknopf', bottomleft = (20, 910), anchor = ('center', 'center'))

#Methods
    #action on mouse
def mouse_greenhouse(button,pos):
    if button == 1 and global_var.button_pressed(pos, button_leave.x, button_leave.y, 130, 60):
        global_var.scene = 1

    #update
def update_greenhouse():
    pass

    #draw
def draw_greenhouse():
    background.draw()
    button_leave.draw()


