from pgzero.actor import Actor
import global_var
import random


class Inventory:
    def __init__(self, columns, rows, x, y):
        self.inventory_background = []
        self.item_slot = []
        self.pos_selected = [-1,0]
        self.open = False

        item = Item(1,1,1,1,1,1,1,'worm')



        for i in range(columns):
            self.inventory_background.append([])
            self.item_slot.append([])
            for j in range(rows):
                self.inventory_background[i].append(Actor('panel_brown', center = (x + i*65, y + j*65), anchor = ('center', 'center')))
                self.item_slot[i].append(0)

        self.add_item(1, 2, item)
    
    def add_item(self, colum, row, item):
        self.item_slot[colum][row] = item
        
    def del_item(self, colum, row):
        self.item_slot[colum][row] = 0

    def toggle_open(self):
        if self.open:
            self.open = False
        else:
            self.open = True

    def mouse(self, button, pos):
        if global_var.button_pressed(pos, 175, 245, 165, 165) and button == 1 and self.open:
            found = False
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    if global_var.button_pressed(pos, self.inventory_background[i][j].x, self.inventory_background[i][j].y, 32, 32):
                        if self.pos_selected[0] >= 0:
                            self.inventory_background[self.pos_selected[0]][self.pos_selected[1]].image = 'panel_brown'
                            self.add_item(i, j, self.item_slot[self.pos_selected[0]][self.pos_selected[1]])
                            self.del_item(self.pos_selected[0], self.pos_selected[1])
                            self.pos_selected = [-1,0]
                        else:
                            self.pos_selected = [i,j]                        
                            self.inventory_background[i][j].image = 'panel_brown_selected'
                        found = True
                        break
                if found:
                    break
        elif self.pos_selected[0] >= 0:
            self.inventory_background[self.pos_selected[0]][self.pos_selected[1]].image = 'panel_brown'
            self.pos_selected = [-1,0]
            
    def draw(self):
        if self.open:
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    self.inventory_background[i][j].draw()
                    if self.item_slot[i][j] != 0:
                        self.item_slot[i][j].actor.center = (self.inventory_background[i][j].x, self.inventory_background[i][j].y)
                        self.item_slot[i][j].actor.draw()
    
        

class Item():
    def __init__(self, max_count, count, value, name, attribute, location, type, image):
        self.max_count = max_count
        self.count = count
        self.value = value
        self.name = name
        self.attribute = attribute
        self.location = location
        self.type = type

        self.actor = Actor(image)
    
    def move(self, new_location):
        pass
