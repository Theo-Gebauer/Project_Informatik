import global_var
from pgzero.actor import Actor
from inventory import Inventory


class Trader:
    def __init__(self):
        self.actor = Actor('trader', bottomleft = (920, 900))