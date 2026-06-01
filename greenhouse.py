from pgzero.actor import Actor
import global_var
from patches import Patch

patches = []

#Actors
background = Actor('greenhouse/greenhouse_background', center = (global_var.WIDTH//2, global_var.HEIGHT//2))
button_leave = Actor('startknopf', bottomleft = (20, 910), anchor = ('center', 'center'))

for i in range(4):
    patches.append(Patch(300 + i*250, 785))

#Methods
    #action on mouse
def mouse_greenhouse(button, pos):
    if button == 1 and global_var.button_pressed(pos, button_leave.x, button_leave.y, 130, 60):
        global_var.scene = 1
    else:
        for patch in patches:
            patch.mouse(button, pos)

    #update
def update_greenhouse():
    for patch in patches:
        patch.update()

    #draw
def draw_greenhouse(screen):
    background.draw()
    button_leave.draw()
    for patch in patches:
        patch.draw(screen)

