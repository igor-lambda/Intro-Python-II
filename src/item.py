class Item:
    def __init__(self, name, description, picked_up = False):
        self.name = name
        self.description = description
        self.picked_up = picked_up

    def pick(self):
        self.picked_up = True
        print("You have picked up {name}".format(name=self.name))
    
    def drop(self):
        self.picked_up = False
        print("You have dropped {name}".format(name=self.name))
    
    def __str__(self):
        return "{self.name}".format(self=self)