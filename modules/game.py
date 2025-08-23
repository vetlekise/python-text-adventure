from .character import Player

class Game:
    def __init__(self, starting_room):
        self.player = Player("Investigator", 100, 25) # Create the player
        self.player.current_room = starting_room
        self.is_running = True

    def run(self):
        """The main game loop."""
        print(f"You are in the {self.player.current_room.name}.")
        print(self.player.current_room.description)

        while self.is_running:
            user_input = input("> ").lower().strip()
            ...