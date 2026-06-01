from pgzero.actor import Actor
import global_var
from brewing import Brew_potions

#Actors
background = Actor('alchemy/alchemy_background', center = (global_var.WIDTH//2, global_var.HEIGHT//2))
button_leave = Actor('startknopf', bottomleft = (20, 910), anchor = ('center', 'center'))
potions = Brew_potions(660, 450)


#Methods
    #action on mouse
def mouse_alchemy(button,pos):
    if button == 1 and global_var.button_pressed(pos, button_leave.x, button_leave.y, 130, 60):
        global_var.scene = 1
    else:
        potions.mouse(button, pos)

    #update
def update_alchemy():
    pass

    #draw
def draw_alchemy(screen):
    background.draw()
    button_leave.draw()
    potions.draw(screen)

