from item import Item

class LightSource(Item):
    def __init__(self, name, desciption):
        super().__init__(name, desciption)
    
    def drop(self):
        print("It's not wise to drop your source of light!")
        super.drop()
