from lightsource import LightSource
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room
        self.inventory = []
        if self.current_room.is_lit:
            self.can_see = True
        else:
            self.can_see = False

    def set_current_room(self, room):
        self.current_room = room

    def state_current_room(self):
        return "Current room: {self.current_room.name}, description: {self.current_room.description}".format(self=self)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def state_inventory(self):
        print("Your inventory currently has: ")
        if len(self.inventory) == 0:
            print("nothing")
        else:
            for i in self.inventory:
                print(i)

    def announce(self):
        if self.can_see:
            print(self.state_current_room())
            self.current_room.state_items()
        else:
            print("It's pitch black!")
        print("Type 'get <item>' to pick up an item.")
        self.state_inventory()

    def has_torch(self):
        has = False
        for i in self.inventory:
            if isinstance(i, LightSource):
                has = True
        return has

    def move_to(self, new_room):
        if new_room.is_lit or self.has_torch() or new_room.has_torch():
            self.can_see = True
            print("I can see")
        else:
            self.can_see = False
            print("I amb lind")
        self.announce()
        try:
            self.set_current_room(self.current_room.n_to)
            print("You have entered", self.current_room)
        except:
            print("Can't go in that direction")
        

    def pickup_item(self, item_name):
        # find item by name
        item = None
        try:
            for i in self.current_room.get_items():
                if i.name == item_name:
                    item = i
        except:
            print('Please make sure item is in room and spelled correctily')
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
        # find item by name
        item = None
        try:
            for i in self.inventory:
                print('itemx', i)
                if i.name == item_name:
                    item = i
        except:
            print('Make sure item is in inventory and spelled correctly')
        print('inventory item', item)
        # remove item from inventory
        self.remove_from_inventory(item)
        # add item to current room
        self.current_room.add_item(item)
        # toggle item's picked_up property
        item.drop()
        self.state_inventory()
        self.current_room.state_items()
