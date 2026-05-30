from pgzero.actor import Actor
import global_var


class Item():
    def __init__(self, value, name, attribute, type, delay, image):
        self.value = value
        self.name = name
        self.attribute = attribute
        self.type = type
        self.delay = delay

        self.actor = Actor(image)
    
    def move(self, new_location):
        pass
