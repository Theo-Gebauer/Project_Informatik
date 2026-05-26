import pgzrun
import random
#import hintergrund
#import startmenu
import global_var

WIDTH = 1420
HEIGHT = 930 

startbutton = Actor('startknopf', center=(global_var.WIDTH//2, global_var.HEIGHT//2), anchor=('center', 'center'))
endbutton = Actor('startknopf', topright=(global_var.WIDTH-30, 30), anchor=('center', 'center'))

clouds = [
    Actor('cloud1', topleft=(0,global_var.max_height+ 10)),
    Actor('cloud2', topleft=(200,global_var.max_height+50)),
    Actor('cloud3', topleft=(500,global_var.max_height+25)),
    Actor('cloud4', topleft=(500,global_var.max_height+60))
]

tower = Actor('turm', midbottom=(global_var.WIDTH//2, global_var.HEIGHT)) 

background = Actor('hintergrund_tag', bottomright=(global_var.WIDTH, global_var.HEIGHT), anchor=('left', 'bottom'))

for i in range(4):
    clouds[i].vx = i+1

#Method for testing if Button is pressed
def button_pressed(pos_cursor, pos_button_x, pos_button_y, width_button, height_button):
    if pos_button_x - width_button < pos_cursor[0] < pos_button_x + width_button and pos_button_y - height_button < pos_cursor[1] < pos_button_y + height_button:
        return True
    else:
        return False


#Mausabtastung
def on_mouse_down(button,pos):

    if not global_var.game_started and button_pressed(pos, startbutton.x, startbutton.y, 130, 60):         #startbutton
        if not (button == mouse.WHEEL_UP or button == mouse.WHEEL_DOWN):
            global_var.autoscroll = True
            global_var.scroll_y = 10
            global_var.game_started = True
        
    elif (button == mouse.WHEEL_UP or button == mouse.WHEEL_DOWN) and global_var.game_started:             #scrolling with mousewheel
        if button == mouse.WHEEL_UP and background.y < 1680 and global_var.autoscroll == False:
            global_var.scroll_y = 30
        elif button == mouse.WHEEL_DOWN and background.y > global_var.HEIGHT and global_var.autoscroll == False:
            global_var.scroll_y = -30

    else:    
        if button_pressed(pos, endbutton.x, endbutton.y, 130, 60):                              #endbutton
            global_var.autoscroll = True
            global_var.scroll_y = -10
            global_var.game_started = False


#Update
def update():

    background.y += global_var.scroll_y
    tower.y += global_var.scroll_y

    for cloud in clouds:
        if cloud.left <= global_var.WIDTH:
            cloud.left += cloud.vx
        else:
            cloud.left = -450
            cloud.vx = random.randint(1,3)
        cloud.y += global_var.scroll_y

    if not global_var.autoscroll or not (global_var.HEIGHT < background.y < 1680):
       global_var.scroll_y = 0
       global_var.autoscroll = False
     
#Draw

def draw():

    background.draw()

    for i in range(2,4):
        clouds[i].draw()

    tower.draw()

    for i in range(0,2):
        clouds[i].draw()

    if not global_var.game_started:
        startbutton.draw()
    else:
        endbutton.draw()

pgzrun.go()
