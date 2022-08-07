
class Item(object):
    def __init__(self):
        self.name = ""
        self.tag = ""
        self.attr = ""
        self.val = ""

    def __repr__(self):
        return f"name: {self.name} :: tag: {self.tag} :: attr: {self.attr} :: val: {self.val}"
