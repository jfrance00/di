
class MenuManager():

    def __init__(self, menu):
        self.menu = {
            'Name' : '',
            'Price' : '',
            'Spice level' : '',
            'Gluten index' : '',
        }

    def add_item(self, name, price, spice_level, gluten_index):
        self.menu['Name'] = name
        self.menu['Price'] = price

    def update_item(self, name, price, spice_level, gluten_index):
        pass

    def remove_item(self, name, price, spice_level, gluten_index):
        pass