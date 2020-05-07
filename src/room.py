# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return self.name
    
    def add_item(self, item):
        self.items.append(item)

    def set_items(self, new_items):
        self.items = new_items

    def remove_item(self, item):
        self.items.remove(item)

    def has_items(self):
        has = False
        if len(self.items) > 0:
            has = True
        return has

    def state_items(self):
        print("The room contains these items: ")
        if len(self.items) == 0:
            print("No Items")
        else:
            for i in self.items:
                print(i)
    
    def get_items(self):
        return self.items