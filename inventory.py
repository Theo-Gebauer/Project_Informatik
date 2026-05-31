from pgzero.actor import Actor
import global_var
from items import Item

class Inventory:
    def __init__(self, columns, rows, x, y):
        self.inventory_background = []
        self.item_slot = []
        global_var.inventory_pos_selected = None
        global_var.inventory_open = False

        item = Item(1,1,1,1,250,'plant_item1')

        for i in range(columns):
            self.inventory_background.append([])
            self.item_slot.append([])
            for j in range(rows):
                self.inventory_background[i].append(Actor('panel_brown', center = (x + i*65, y + j*65), anchor = ('center', 'center')))
                self.item_slot[i].append(0)

        self.add_item(0, 0, item)
    
    def add_item(self, colum, row, item):
        self.item_slot[colum][row] = item
        
    def del_item(self, colum, row):
        self.item_slot[colum][row] = 0

    def empty(self, colum, row):
        return self.item_slot[colum][row] == 0

    def mouse(self, button, pos):
        if global_var.button_pressed(pos, 
                                     len(self.inventory_background) * 33 + self.inventory_background[0][0].x - 32,
                                     len(self.inventory_background[0]) * 33 + self.inventory_background[0][0].y - 32, 
                                     len(self.inventory_background) * 33, 
                                     len(self.inventory_background[0]) * 33) and button == 1 and global_var.inventory_open:
            found = False
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    if global_var.button_pressed(pos, self.inventory_background[i][j].x, self.inventory_background[i][j].y, 32, 32):
                        print(self)
                        print(global_var.inventory_selected)
                        if global_var.inventory_pos_selected is not None:
                            global_var.inventory_selected.inventory_background[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]].image = 'panel_brown'
                            
                            item_temp = self.item_slot[i][j]
                            self.add_item(i, j, global_var.inventory_selected.item_slot[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]])
                            global_var.inventory_selected.add_item(global_var.inventory_pos_selected[0], global_var.inventory_pos_selected[1], item_temp)

                            global_var.inventory_pos_selected = None
                            global_var.inventory_selected = None
                            print('getauscht')
                        else:      
                            self.inventory_background[i][j].image = 'panel_brown_selected'
                            global_var.inventory_pos_selected = [i,j]  
                            global_var.inventory_selected = self
                            print(global_var.inventory_pos_selected)                
                        found = True
                        break
                if found:
                    break
        '''elif global_var.inventory_pos_selected is not None:
            global_var.inventory_selected.inventory_background[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]].image = 'panel_brown'
            global_var.inventory_pos_selected = None
            global_var.inventory_selected = None'''
            
    def draw(self):
        if global_var.inventory_open:
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    self.inventory_background[i][j].draw()
                    if self.item_slot[i][j] != 0:
                        self.item_slot[i][j].actor.center = (self.inventory_background[i][j].x, self.inventory_background[i][j].y)
                        self.item_slot[i][j].actor.draw()