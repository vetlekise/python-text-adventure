from modules.world import setup_world
from modules.game import Game

# 1. Create all the game objects and get the starting location
start_location = setup_world()

# 2. Create a Game instance with that starting location
my_game = Game(start_location)

# 3. Run the game
my_game.run()