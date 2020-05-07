from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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

# Define items
grass = Item("Grass", "Shitty green plant")
dirt = Item("Dirt", "Brown stuff everywhere")
potted_plant = Item("Potted_Plant", "Plant in a clay pot")


# Set room items
room["outside"].set_items([grass, dirt])
room["foyer"].set_items([potted_plant])
#
# Main


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("Igor", room["outside"])
player.announce()
user = input("[n] North  [e] East  [s] South  [w] West  [q] Quit: \n")
userList = user.split(" ")
while not user == "q":
    #user chooses north
    if len(userList) == 1:
        if user == "n":
            player.announce()
            player.move_to(player.current_room.n_to)
        elif user == "e":
            player.announce()
            player.move_to(player.current_room.e_to)
        elif user == "s":
            player.announce()
            player.move_to(player.current_room.s_to)
        elif user == "w":
            player.announce()
            player.move_to(player.current_room.w_to)
        user = input("[n] North  [e] East  [s] South  [w] West  [q] Quit: \n")
        userList = user.split(" ")

    elif len(userList) == 2:
        if userList[0] == "get":
            player.pickup_item(userList[1])
        elif userList[0] == "drop":
            player.drop_item(userList[1])
    
        
        user = input("[n] North  [e] East  [s] South  [w] West  [q] Quit: \n")
        userList = user.split(" ")


        
