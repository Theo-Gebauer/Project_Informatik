WIDTH = 1420
HEIGHT = 930 
scroll_y = 0
max_height = HEIGHT - 1680
autoscroll = False
absolutex = 0
absolutey = 930

scene = 1
wave = 1
game_started = False
game_lost = False
night = False
inventory_open = False
inventory_pos_selected = None
inventory_selected = None

#Methods
    #Method for testing if Button is pressed
def button_pressed(pos_cursor, pos_button_x, pos_button_y, width_button, height_button):
    return pos_button_x - width_button < pos_cursor[0] < pos_button_x + width_button and pos_button_y - height_button < pos_cursor[1] < pos_button_y + height_button



    #action on mouse
def mouse_global_var(button, pos):     
    global scroll_y
    global absolutey
    global inventory_open

    if button == 4 and absolutey < 1680 and scene == 1:
        scroll_y = 30
    elif button == 5 and absolutey > HEIGHT and scene == 1:
        scroll_y = -30

    if button_pressed(pos, 30, 40, 30, 40) and button == 1:
        if inventory_open:
            inventory_open = False
        else:
            inventory_open = True

        

    #update
def update_global_var():
    global scroll_y
    global absolutey
    global autoscroll
    global game_started
    global game_lost
    
    absolutey += scroll_y

    if not autoscroll or not (HEIGHT < absolutey < 1680):
       scroll_y = 0
       autoscroll = False
    
    if game_lost:
        print("Verloren")
        game_started = False
        game_lost = False
    

#button ==
#1 -> left_click
#2 -> middle_click
#3 -> right_click
#4 -> wheel_up
#5 -> wheel_down
