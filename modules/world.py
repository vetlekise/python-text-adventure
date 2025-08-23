from .room import Room
from .puzzle import Puzzle
from .item import Item

def setup_world():
    # Items and Keys
    silver_key = Item("Silver Key", "An ornate silver key.")
    brass_key = Item("Brass Key", "A heavy brass key.")
    gold_key = Item("Gold Key", "A shiny gold key.")
    book_of_whispers = Item("Book of Whispers", "The ancient, forbidden tome.")

    # Puzzles
    riddle_puzzle = Puzzle(
        "I have a spine, but I cannot stand. I have leaves, but I am not a tree. I have a voice, but I cannot speak. What am I?", 
        "book", 
        silver_key
    )
    order_puzzle = Puzzle(
        "A note reads: 'Only their proper order will reveal what is hidden.' The books are Dracula, Moby Dick, and Alice in Wonderland.",
        "alice dracula moby", 
        brass_key
    )
    word_puzzle = Puzzle(
        "A faint whisper seems to echo through the profound SILENCE of this room...", 
        "silence", 
        gold_key
    )

    # Create All Rooms
    main_hall = Room(
        name="Main Hall",
        description="A vast, dusty hall. A grand staircase leads north.",
        puzzle=riddle_puzzle
    )
    
    study = Room(
        name="Study",
        description="A quiet room with a large mahogany desk. A passage continues north.",
        puzzle=order_puzzle
    )
    
    archives = Room(
        name="The Archives",
        description="Dusty shelves line the walls, filled with forgotten tomes.",
        puzzle=word_puzzle
    )
    
    restricted_section = Room(
        name="Restricted Section",
        description="The air crackles with energy. A central lectern is held by three chains with silver, brass, and gold locks.",
        is_locked=True,
        locks={ # True means it is locked
            'silver': True, 
            'brass': True,
            'gold': True
        }
    )
    
    # Link Rooms Together
    main_hall.exits = {'north': study}
    study.exits = {'south': main_hall, 'north': archives}
    archives.exits = {'south': study, 'north': restricted_section}
    restricted_section.exits = {'south': archives}

    # Return the starting point of the game
    return main_hall