class Character:
    def __init__(self, name, health, damage):

        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self, target):
        ...
        
    def is_alive(self):
        ...
    
    # Methods
class Player(Character):
    def __init__(self, name, health, damage, inventory=None, current_room=None):
        super().__init__(name, health, damage) 
        
        self.inventory = inventory
        self.current_room = current_room
        
        def move(self, direction):
            ...
        
        def take_item(self, item):
            ...
        
class Enemy(Character):
        def __init__(self, name, health, damage):
            super().__init__(name, health, damage)