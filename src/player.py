# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room
        self.inventory = []

    def set_current_room(self, room):
        self.current_room = room

    def state_current_room(self):
        return "Current room: {self.current_room.name}, description: {self.current_room.description}".format(self=self)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def state_inventory(self):
        if len(self.inventory) == 0:
            return "nothing"
        else:
            return ", ".join((self.inventory))
            
    def announce(self):
        print(self.state_current_room())
        self.current_room.state_items()
        print("Type 'get <item>' to pick up an item.")
        print("You currently have {stuff} in your inventory".format(stuff=self.state_inventory()))
    
    def move_to(self, newRoom):
        try: 
            self.set_current_room(self.current_room.n_to)
            print("You have entered", self.current_room)
        except:
            print("Can't go north from here")
    