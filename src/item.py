class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return "{self.name} \nItem stats: {self.desc}".format(self=self)
