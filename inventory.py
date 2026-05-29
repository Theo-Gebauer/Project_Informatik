from pgzero.actor import Actor
import global_var
import random

#vars
pos_selected = [0,0]
inventory = []
inventory_open = False

#Actors
inventory_button = Actor('inventory_button', topleft = (10, 10))
for i in range(5):
    inventory.append([])
    for j in range(5):
        inventory[i].append(Actor('panel_brown', center=(42 + i*65, 112 + j*65)))

class item():
    def __init__(self, max_count, count, value, name, attribute, location, type):
        self.max_count = max_count
        self.count = count
        self.value = value
        self.name = name
        self.attribute = attribute
        self.location = location
        self.type = type
    
    def move(self, new_location):
        pass

        


#Methods
    #action on mouse
def mouse_inventory(button,pos):
    global inventory
    global pos_selected
    global inventory_open

    if global_var.button_pressed(pos, 30, 30, 30, 30) and button == 1:
        if not inventory_open:
            inventory_open = True
        else:
            inventory_open = False
    elif global_var.button_pressed(pos, 175, 245, 165, 165) and button == 1:
        found = False
        for i in range(len(inventory)):
            for j in range(len(inventory[i])):
                if global_var.button_pressed(pos, 42 + i*65, 112 + j*65, 32, 32):
                    inventory[pos_selected[0]][pos_selected[1]].image = 'panel_brown'
                    inventory[i][j].image = 'panel_brown_selected'

                    pos_selected = [i,j]
                    found = True
                    break
            if found:
                break
    #update
def update_inventory():
    pass

    #draw
def draw_inventory():
    inventory_button.draw()
    if inventory_open:
        for row in inventory:
            for table in row:
                table.draw()
    
