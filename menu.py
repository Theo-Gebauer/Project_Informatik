from pgzero.actor import Actor
import global_var


#Actors
startbutton = Actor('startknopf', center=(global_var.WIDTH//2, global_var.HEIGHT//2), anchor=('center', 'center'))
endbutton = Actor('startknopf', topright=(global_var.WIDTH-30, 30), anchor=('center', 'center'))


#Methods
    #action on mouse
def mouse_menu(button,pos):
    if not global_var.game_started and button == 1 and global_var.button_pressed(pos, startbutton.x, startbutton.y, 130, 60):         #startbutton
        global_var.autoscroll = True
        global_var.scroll_y = 10
        global_var.game_started = True
        global_var.game_start = True
    elif global_var.game_started and button == 1 and global_var.button_pressed(pos, endbutton.x, endbutton.y, 130, 60):     #endbutton
            global_var.autoscroll = True
            global_var.scroll_y = -10
            global_var.game_started = False

    #update
def update_menu():
    pass
     
    #draw
def draw_menu():
    if not global_var.game_started:
        startbutton.draw()
    else:
        endbutton.draw()
