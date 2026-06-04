from pgzero.actor import Actor
import global_var
from items import Item
import pygame
from pgzero.builtins import Rect

class Inventory:
    def __init__(self, columns, rows, x, y):
        self.inventory_background = []
        self.item_slot = []
        self.hovered_item = None

        for i in range(columns):
            self.inventory_background.append([])
            self.item_slot.append([])
            for j in range(rows):
                self.inventory_background[i].append(Actor('panel_brown', center = (x + i*65, y + j*65), anchor = ('center', 'center')))
                self.item_slot[i].append(None)

    def add_item(self, colum, row, item):
        self.item_slot[colum][row] = item

    def add_item_on_empty(self, item):
        added = False
        for i in range(len(self.item_slot)):
            for j in range(len(self.item_slot[i])):
                if self.item_slot[i][j] is None:
                    self.item_slot[i][j] = item
                    added = True
                    break
            if added:
                break

        if not added:
            pass

        
    def del_item(self, colum, row):
        self.item_slot[colum][row] = None

    def del_all(self):
        for i in range(len(self.item_slot)):
            for j in range(len(self.item_slot[i])):
                self.item_slot[i][j] = None

    def empty(self, colum, row):
        return self.item_slot[colum][row] is None
    
    def add_inv(self, x, y):
        self.item_slot[0].append(None)
        self.inventory_background[0].append(Actor('panel_brown', center = (x, y), anchor = ('center', 'center')))

    def move(self, dx, dy):
        for i in range(len(self.inventory_background)):
            for j in range(len(self.inventory_background[i])):
                self.inventory_background[i][j].x += dx
                self.inventory_background[i][j].y += dy

    def get_value(self):
        value = 0
        for i in range(len(self.item_slot)):
            for j in range(len(self.item_slot[i])):
                if self.item_slot[i][j] is not None:
                    value += self.item_slot[i][j].value
        return value

    def trade(self, button, pos, value1):
        global_var.trade_allowed = False
        selected_item = None
        if button == 1 and global_var.inventory_open:
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    self.inventory_background[i][j].image = 'panel_brown'
                    if global_var.button_pressed(pos, self.inventory_background[i][j].x, self.inventory_background[i][j].y, 32, 32):
                        if global_var.inventory_selected is not None:
                            global_var.inventory_selected.inventory_background[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]].image = 'panel_brown'
                        if self.item_slot[i][j] is not None:
                            self.inventory_background[i][j].image = 'panel_brown_selected'
                            selected_item = self.item_slot[i][j]
                            if self.item_slot[i][j].value * 2 <= value1:
                                global_var.trade_allowed = True
        return selected_item



    def mouse(self, button, pos):
        if button == 1 and global_var.inventory_open:
            found = False
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    if global_var.button_pressed(pos, self.inventory_background[i][j].x, self.inventory_background[i][j].y, 32, 32):
                        if global_var.inventory_selected is not None:
                            global_var.inventory_selected.inventory_background[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]].image = 'panel_brown'
                            
                            item_temp = self.item_slot[i][j]
                            self.add_item(i, j, global_var.inventory_selected.item_slot[global_var.inventory_pos_selected[0]][global_var.inventory_pos_selected[1]])
                            global_var.inventory_selected.add_item(global_var.inventory_pos_selected[0], global_var.inventory_pos_selected[1], item_temp)

                            global_var.inventory_pos_selected = None
                            global_var.inventory_selected = None
                        else:      
                            self.inventory_background[i][j].image = 'panel_brown_selected'
                            global_var.inventory_pos_selected = [i,j]  
                            global_var.inventory_selected = self           
                        found = True
                        break
                if found:
                    break

    def update(self):
        for i in range(len(self.item_slot)):
            for j in range(len(self.item_slot[i])):
                if self.item_slot[i][j]is not None:                    
                    mouse_pos = pygame.mouse.get_pos()

                    if self.inventory_background[i][j].collidepoint(mouse_pos):
                        self.hovered_item = self.item_slot[i][j]

            
    def draw(self, screen):
        if global_var.inventory_open:
            for i in range(len(self.item_slot)):
                for j in range(len(self.item_slot[i])):
                    self.inventory_background[i][j].draw()
                    if self.item_slot[i][j] is not None:
                        self.item_slot[i][j].draw(self.inventory_background[i][j].x, self.inventory_background[i][j].y, screen)
            
            if self.hovered_item is not None:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                i = 0            
                for prop, value in self.hovered_item.effects.items():
                    i += 1 

                screen.draw.filled_rect(
                    Rect(mouse_x - 135, mouse_y  - i * 20 - 5, 135, i * 20 + 25),
                    (30, 30, 30)
                )

                screen.draw.text(
                    self.hovered_item.name,
                    (mouse_x - 130, mouse_y - i * 20),
                    color="white"
                )
                
                y_offset = 20
                for effect_name, value in self.hovered_item.effects.items():
                    if effect_name in self.hovered_item.discovered_effects:
                        screen.draw.text(
                            f"{effect_name}: {value}",
                            (mouse_x - 130, mouse_y - i * 20 + y_offset),
                            color="white"
                        )
                    else:
                        screen.draw.text(
                            "- Unbekannt -",
                            (mouse_x - 130, mouse_y - i * 20 + y_offset),
                            color="white"
                        )

                    y_offset += 20
                
                self.hovered_item = None