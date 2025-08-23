from .puzzle import Puzzle
from .item import Item

class Room:
    def __init__(self, name, description, exits=None, item=None, puzzle=None, locks=None, is_locked=False):
        self.name = name
        self.description = description
        
        # If no exits are provided, default to an empty dictionary
        self.exits = exits if exits is not None else {}
        
        self.item = item
        self.puzzle = puzzle
        self.locks = locks
        self.is_locked = is_locked