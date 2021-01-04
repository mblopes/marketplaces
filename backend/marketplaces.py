class Marketplaces:

    def __init__(self, name, categories):
        self._name = name
        self.categories = categories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __getitem__(self, item):
        return self.categories[item]