import global_var
from pgzero.actor import Actor
from inventory import Inventory


class Trader:
    def __init__(self):
        self.actor = Actor('trader', bottomleft = (920, 950))
        self.trade_button = Actor('startknopf', center = (1120, 350))

        self.selling_items = Inventory(3, 3, 900, 502)
        self.buying_items = Inventory(4, 4, 1170, 470)

        for name, item in global_var.all_ingredients.items():
            self.buying_items.add_item_on_empty(item)

    def mouse(self, button, pos):
        self.selling_items.mouse(button, pos)

        if global_var.trade_allowed and global_var.button_pressed(pos, 1120, 350, 130, 60) and global_var.inventory_open:
            self.selling_items.del_all()            
            global_var.trade_allowed = False
            self.selling_items.add_item(1, 1, self.selected_item)
        else:
            self.selected_item = self.buying_items.trade(button, pos, self.selling_items.get_value())
    
    def update(self):
        self.trade_button.y += global_var.scroll_y
        self.actor.y += global_var.scroll_y
        self.selling_items.move(0, global_var.scroll_y)
        self.buying_items.move(0, global_var.scroll_y)

        self.selling_items.update()
        self.buying_items.update()

    def draw(self, screen):
        self.selling_items.draw(screen)

        if not global_var.night:
            self.actor.draw()
            self.buying_items.draw(screen)

            if global_var.inventory_open:
                if global_var.trade_allowed:
                    self.trade_button.draw()