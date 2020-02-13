# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    def __str__(self):
        return f"Player: {self.name}"
    def __repr__(self):
        return f"Player({repr(self.name, self.room)})"
    def add_items(self, item):
        self.inventory.append(item)