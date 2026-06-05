import random
from pgzero.actor import Actor
import pygame

from waves import WaveManager
from items import Item
from inventory import Inventory
from layers import Layer
from trader import Trader
from patches import Patch
from brewing import Brew_potions


#variables
WIDTH = 1420
HEIGHT = 930 
scroll_y = 0
max_height = HEIGHT - 1680
autoscroll = False
absolutex = 0
absolutey = 930

clock = Actor('clock', center = (WIDTH // 2 + 300, 100), anchor = ('center', 'center'))
clock_arrow = pygame.image.load('images/clock_arrow.png').convert_alpha()

scene = 1

trader = None
trade_allowed = False

wave = None
all_monsters = None

game_started = False
game_start = False
game_lost = False

time = 0
duration_day = 4000
night = False
darkness = 255

inventory_open = False
inventory_pos_selected = None
inventory_selected = None


patches = []
layers = []
pulse = []
for i in range(4):
    patches.append(Patch(300 + i*250, 785))
potions = Brew_potions(700, 450)
inventory_player = Inventory(5, 5, 42, 112)
for i in range(8):
    layers.append(Layer(i))
    pulse.append(False)

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
    'poison': (60, 255, 20),
    'fire': (255, 80, 0),
    'ice': (0, 150, 255),
    'slow': (100, 100, 100),
    'pulse': (120, 0, 120)
}

translation = {
    'poison': 'Gift',
    'fire': 'Feuer',
    'ice': 'Eis',
    'slow': 'Langsam',
    'pulse': 'Pulsieren'
}

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
            trader.mouse(button, pos)
            for layer in layers:
                layer.mouse(button, pos)

        

    #update
def update_global_var():
    global scroll_y, absolutey, autoscroll
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
    global trader
    global all_monsters
    global wave
    global patches
    global potions
    
    absolutey += scroll_y

    
    if game_started and game_start: #creating all important variables during start of the game

        game_start = False        

        seed = random.randint(0, 1000)        
        random.seed(seed)
                
        all_ingredients = {
            'leaf': Item('Blatt', 'ingredient', 200, 'items/leaf', 'fire'),
            'cherry': Item('Kirsche', 'ingredient', 300, 'items/cherry', None),
            'banana': Item('Banane', 'ingredient', 300, 'items/banana', None),
            'dragonfruit': Item('Drachenfrucht', 'ingredient', 400, 'items/dragonfruit', 'pulse'),
            'herbs': Item('Kräuter', 'ingredient', 400, 'items/herbs', 'poison'),
            'lanterfruit': Item('Laternenfrucht', 'ingredient', 300, 'items/lanternfruit', None),
            'plum': Item('Pflaume', 'ingredient', 400, 'items/plum', 'ice'),
            'spikefruit': Item('Stachelfrucht', 'ingredient', 400, 'items/spikefruit', 'slow'),
            'strawberry': Item('Erdbeere', 'ingredient', 300, 'items/strawberry', None),
            'dead_worm': Item('Toter Wurm', 'ingredient', 0, 'monster/worm_dead', 'slow'),
            'dead_ghost': Item('Toter Geist', 'ingredient', 0, 'monster/ghost_dead', 'ice'),
            'dead_slime': Item('Toter Schleim', 'ingredient', 0, 'monster/slime_dead', 'fire'),
            'dead_spider': Item('Tote Spinne', 'ingredient', 0, 'monster/spider_dead', 'poison'),
            'dead_spinner': Item('Toter Schneider', 'ingredient', 0, 'monster/spinner_dead', 'pulse')
            }
        
        all_monsters = [
            {
                'image': 'monster/worm',
                'hp': 50,
                'speed': 0.6,
                'loot': all_ingredients['dead_worm']
                     },
            {
                'image': 'monster/slime',
                'hp': 80,
                'speed': 1,
                'loot': all_ingredients['dead_slime']
                     },
            {
                'image': 'monster/ghost',
                'hp': 50,
                'speed': 1.2,
                'loot': all_ingredients['dead_ghost']
                     },
            {
                'image': 'monster/spider',
                'hp': 70,
                'speed': 1.1,
                'loot': all_ingredients['dead_spider']
                     },
            {
                'image': 'monster/spinner',
                'hp': 100,
                'speed': 1.3,
                'loot': all_ingredients['dead_spinner']
                     }
        ]

        wave = WaveManager()
        trader = Trader()

        inventory_player.add_item(2, 2, all_ingredients['leaf'])        
        inventory_player.add_item_on_empty(Item('Debug Feuer', 'potion', 0, None, {'fire':10}))
        #inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'pulse':20}))
        #inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'pulse':20}))
        inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'pulse':20}))
        inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'slow':10}))
        inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'poison':10}))
        inventory_player.add_item_on_empty(Item('Debug Pulse', 'potion', 0, None, {'ice':10}))

    if game_started: #updating during the running game
        if scene == 1:
            trader.update()
            for layer in layers:
                layer.update()

        if time < duration_day and not night:
            time += 1
            if 255 - time >= 0:
                darkness = 255 - time
        elif time > 0 and night:
            time -= 1
            if  duration_day - time <= 255:
                darkness = duration_day - time
        elif wave.ended() and not night:
                wave.next_wave()
                night = True
        elif wave.ended() and night:
                night = False

        wave.update()
        inventory_player.update()
        potions.update()
    
    if not autoscroll or not (HEIGHT < absolutey < 1680): #resetting scroll variable
       scroll_y = 0
       autoscroll = False

    if game_lost:
        game_setback()
                   
    #draw
def draw_global_var(screen):        
    global game_started
    global wave
    global layers
    global trader
    global clock
    global clock_arrow
    global time
    global duration_day
    
    if game_started:
        inventory_player.draw(screen)
        if scene == 1:
            trader.draw(screen)
            for layer in layers:
                layer.draw(screen)
        wave.draw(screen)

        clock.draw()

        #rotating the arrow of the clock
        if night:
            rotated = pygame.transform.rotate(clock_arrow, 180 * abs(time)/duration_day)
        else:
            rotated = pygame.transform.rotate(clock_arrow, -180 * abs(time)/duration_day)
        rect = rotated.get_rect(center = (clock.x, clock.y))
        screen.surface.blit(rotated, rect.topleft)

    #resetting all important variables so a new game can start
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
    global trade_allowed
    global inventory_player
    global patches
    global potions
    global trader
    global layers

    potions.potion_slot.del_all()
    potions.ingredients_slot.del_all()

    for patch in patches:
        patch.seed_slot.del_all()
        patch.harvest_slot.del_all()
    
    for layer in layers:        
        layer.animation_effect = None
        layer.potion_used = False
        layer.effect_timer = 0
        layer.effect_duration = 0
        layer.potion_slot.del_item(0, 0)
        layer.animation.image = 'animations/nothing'

        
    inventory_player.del_all()


    trader = None
    trade_allowed = False
    darkness = 255
    scene = 1
    autoscroll = True
    scroll_y = -10
    game_started = False
    game_lost = False     
    wave = None
    time = 0
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
