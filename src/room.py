# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, desc, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return "You are at {self.name} \ndesc: {self.desc}\n".format(self=self)

    def add_item(self, new_item):
        self.items.append(new_item)
        # return f"You added {new_item}"
