from waves import WaveManager
import random
from items import Item
from inventory import Inventory
from layers import Layer

WIDTH = 1420
HEIGHT = 930 
scroll_y = 0
max_height = HEIGHT - 1680
autoscroll = False
absolutex = 0
absolutey = 930

scene = 1
wave = WaveManager()
game_started = False
game_start = False
game_lost = False
time = 0
duration_day = 100
night = False
inventory_player = Inventory(5, 5, 42, 112)
inventory_open = False
inventory_pos_selected = None
inventory_selected = None
darkness = 0
seed = None
all_ingredients = {}
all_effects = [
        'poison',
        'fire',
        'ice',
        'slow',
        'pulse'
]
effect_to_color = {
    'poison': (120, 0, 120),
    'fire': (255, 80, 0),
    'ice': (0, 150, 255),
    'slow': (100, 100, 100),
    'pulse': (255, 0, 255)
}
pulse = False

layers = []
for i in range(8):
    layers.append(Layer(i))

#Methods
    #Method for testing if Button is pressed
def button_pressed(pos_cursor, pos_button_x, pos_button_y, width_button, height_button):
    return pos_button_x - width_button < pos_cursor[0] < pos_button_x + width_button and pos_button_y - height_button < pos_cursor[1] < pos_button_y + height_button



    #action on mouse
def mouse_global_var(button, pos):     
    global scroll_y
    global absolutey
    global inventory_open
    global inventory_player
    global game_started
    global autoscroll
    global layers

    if button == 4 and absolutey < 1680 and scene == 1:
        scroll_y = 30
    elif button == 5 and absolutey > HEIGHT and scene == 1:
        scroll_y = -30

    if button_pressed(pos, 30, 40, 30, 40) and button == 1:
        if inventory_open:
            inventory_open = False
        else:
            inventory_open = True

    if game_started and not autoscroll:
        inventory_player.mouse(button, pos)
        if scene == 1:
            for layer in layers:
                layer.mouse(button, pos)

        

    #update
def update_global_var():
    global scroll_y
    global absolutey
    global autoscroll
    global game_started
    global game_lost
    global scene
    global time
    global night
    global darkness
    global game_start
    global duration_day
    global all_ingredients
    global inventory_player
    global layers
    
    absolutey += scroll_y

    
    if game_started and game_start:
        game_start = False        

        seed = random.randint(0,255)        
        random.seed(seed)
                
        all_ingredients = {
            'leaf': Item('leaf', 'ingredient', 50, 'items/leaf', 'fire'),
            'cherry': Item('cherry', 'ingredient', 100, 'items/cherry', 'pulse'),
            'dead_worm': Item('dead_worm', 'ingredient', 0, 'monster/worm_dead', 'slow')
            }

        inventory_player.add_item(0, 0, all_ingredients['dead_worm'])
        inventory_player.add_item(1, 0, all_ingredients['leaf'])        
        inventory_player.add_item(2, 0, all_ingredients['cherry'])        
        inventory_player.add_item(0, 1, all_ingredients['dead_worm'])
        inventory_player.add_item(1, 1, all_ingredients['leaf'])        
        inventory_player.add_item(2, 1, all_ingredients['cherry'])

    if game_started:
        if time < duration_day and not night:
            time += 1
            if 255 - time >= 0:
                darkness = 255 - time
        elif time > 0 and night:
            time -= 1
            if  duration_day - time <= 255:
                darkness = duration_day - time
        elif not night:
                wave.next_wave()
                night = True
        elif wave.ended() and night:
                night = False
        wave.update()

        inventory_player.update()
    
    for layer in layers:
        layer.update()
    
    if not autoscroll or not (HEIGHT < absolutey < 1680):
       scroll_y = 0
       autoscroll = False

    if game_lost:
        print("Verloren")
        game_setback()
                   

def draw_global_var(screen):        
    global game_started
    global wave
    global layers
    
    if game_started:
        inventory_player.draw(screen)
        if scene == 1:
            for layer in layers:
                layer.draw(screen)
        wave.draw()

def game_setback():
    global scroll_y
    global autoscroll
    global game_started
    global game_lost
    global scene
    global time
    global night
    global inventory_open
    global inventory_pos_selected
    global inventory_selected
    global wave
    global darkness
    global game_start
    global seed

    darkness = 0
    scene = 1
    autoscroll = True
    scroll_y = -10
    game_started = False
    game_lost = False     
    wave.wave = 1
    time = duration_day
    night = False
    inventory_open = False
    inventory_pos_selected = None
    inventory_selected = None
    seed = None
    game_start = False

    

#button ==
#1 -> left_click
#2 -> middle_click
#3 -> right_click
#4 -> wheel_up
#5 -> wheel_down
