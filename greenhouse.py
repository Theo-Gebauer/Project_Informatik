from pgzero.actor import Actor
import global_var
from patches import Patch

#Actors
background = Actor('greenhouse/greenhouse_background', center = (global_var.WIDTH//2, global_var.HEIGHT//2))
button_leave = Actor('startknopf', bottomleft = (20, 910), anchor = ('center', 'center'))


#Methods
    #action on mouse
def mouse_greenhouse(button, pos):
    if button == 1 and global_var.button_pressed(pos, button_leave.x, button_leave.y, 130, 60):
        global_var.scene = 1
    else:
        for patch in global_var.patches:
            patch.mouse(button, pos)

    #update
def update_greenhouse():
    for patch in global_var.patches:
        patch.update()

    #draw
def draw_greenhouse(screen):
    background.draw()
    button_leave.draw()
    for patch in global_var.patches:
        patch.draw(screen)

