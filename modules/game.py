import time
import textwrap
from .character import Player
from .slowprinter import SlowPrinter

class Game:
    def __init__(self, starting_room):
        self.player = Player("Investigator", 100, 25) # Create the player
        self.player.current_room = starting_room 
        self.is_running = True 

    def _display_intro(self):
        """Prints the game's introduction story."""
        try:
            printer = SlowPrinter(delay=0.03)

            story = textwrap.dedent("""
                You are a paranormal investigator locked inside a massive,
                ancient library at midnight. The ghost of the head librarian
                is said to haunt the halls, protecting a forbidden book.

                Find the three hidden keys to unlock the Restricted Section,
                retrieve the Book of Whispers, and escape the library
                before dawn. If you fail, the head librarian might catch you.
            """)
            
            printer.print(story)
            printer = SlowPrinter(delay=0.2)
            printer.print("." * 6)
            time.sleep(0.25)
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            self.is_running = False

    def run(self):
        """The main game loop."""
        
        # Display the intro
        self._display_intro()

        while self.is_running:
            try:
                
                user_input = input("\n> ").lower().strip()
                
                parts = user_input.split()
                verb = parts[0]
                
                if verb == "help":
                    print("Available commands: help, quit, go [direction]")
                elif verb == "quit":
                    print("Thanks for playing!")
                    self.is_running = False
                    return
                elif verb == "go":
                    if len(parts) < 2:
                        print("Go where? Specify a direction (e.g., 'go north').")
                        continue
                    
                    direction = parts[1]
                    
                    # Find current room
                    current_room = self.player.current_room
                    exits = current_room.exits

                    if direction in exits:
                    # Update the player's location to the new room object
                        next_room = exits[direction]
                        self.player.current_room = next_room
                        print(f"You walk {direction} and arrive at the {self.player.current_room.name.lower()}.")
                        print(f"{self.player.current_room.description}")
                    else:
                        print("You can't go that way.")
            except KeyboardInterrupt:
                print("\nGame interrupted. Exiting...")
                break
            except IndexError:
                print("Please enter a command.")
                continue
            except Exception as error:
                print(f"An error occurred: {error}")
                continue