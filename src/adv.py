from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("The Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("The Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("The Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("The Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("The Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

adventurer = Player("Gibbons", room['outside'])
print()
print(adventurer.current_room)
print()
user = str(input("\n [q] Quit Continue(n, s, e, w): ")).lower().strip()

while not user == 'q':
    # user goes north
    if user == 'n' and adventurer.current_room.n_to != None:
        adventurer.current_room = adventurer.current_room.n_to
        print(f"\n{adventurer.current_room}\n")
    elif user == 'n' and adventurer.current_room.n_to == None:
        print("\nYou didn't find much, and return to the center of the room")

    # user goes south
    elif user == 's' and adventurer.current_room.s_to != None:
        adventurer.current_room = adventurer.current_room.s_to
        print(f"\n{adventurer.current_room}\n")
    elif user == 's' and adventurer.current_room.s_to == None:
        print("\nYou didn't find much, and return to the center of the room")

    # user goes east
    elif user == 'e' and adventurer.current_room.e_to != None:
        adventurer.current_room = adventurer.current_room.e_to
        print(f"\n{adventurer.current_room}\n")
    elif user == 'e' and adventurer.current_room.e_to == None:
        print("\nYou didn't find much, and return to the center of the room")

    # user goes west
    elif user == 'w' and adventurer.current_room.w_to != None:
        adventurer.current_room = adventurer.current_room.w_to
        print(f"\n{adventurer.current_room}\n")
    elif user == 'w' and adventurer.current_room.w_to == None:
        print("\nYou didn't find much, and return to the center of the room")

    else:
        print("\nYou must input a valid character, n, s, e, w, or q to quit")

    # print(f"\n{adventurer.current_room}\n")
    user = str(input("\n [q] Quit Continue(n, s, e, w): ")).lower().strip()

print("\n Game Over \n")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
