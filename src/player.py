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
        print("Your invetory currently has: ")
        if len(self.inventory) == 0:
            print("nothing")
        else:
            for i in self.inventory:
                print(i)

    def announce(self):
        print(self.state_current_room())
        self.current_room.state_items()
        print("Type 'get <item>' to pick up an item.")
        self.state_inventory()

    def move_to(self, newRoom):
        try:
            self.set_current_room(self.current_room.n_to)
            print("You have entered", self.current_room)
        except:
            print("Can't go in that direction")

    def pickup_item(self, item_name):
        # find item by name
        item = None
        for i in self.current_room.get_items():
            if i.name == item_name:
                item = i
        # take item out of current rooms items list
        self.current_room.remove_item(item)
        # add item to player inventory
        self.add_to_inventory(item)
        # toggle item's picked_up property
        item.pick()
        self.state_inventory()
        self.current_room.state_items()

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def drop_item(self, item_name):
        #find item by name
        item = None
        for i in self.inventory:
            print('itemx', i)
            if i.name == item_name:
                item = i
        print('inventory item', item)
        # remove item from inventory
        self.remove_from_inventory(item)
        # add item to current room
        self.current_room.add_item(item)
        # toggle item's picked_up property
        item.drop()
        self.state_inventory()
        self.current_room.state_items()