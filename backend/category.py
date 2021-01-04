class Category:

    def __init__(self, name, sub_categories):
        self._name = name
        self.sub_categories = sub_categories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __getitem__(self, item):
        return self.sub_categories[item]