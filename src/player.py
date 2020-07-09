# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return "name: {self.name} \nCurrent room: {self.current_room}".format(self=self)

    def grab_item(self, new_item):
        self.items.append(new_item)

    def drop_item(self, new_item):
        self.items.remove(new_item)
