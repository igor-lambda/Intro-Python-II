# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room

    def set_current_room(self, room):
        self.current_room = room

    def state_current_room(self):
        return "Current room: {self.current_room.name}, description: {self.current_room.description}".format(self=self)
