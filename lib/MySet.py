class MySet:# Define new class named MySet
    # Defines the constructor method of the class which takes an optional argument initial_data that defaults to None.
    def __init__(self, initial_data=None):
        self.dictionary = {}
        if initial_data:
            for item in initial_data:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)


    def __init__(self, initial_data=None):
        self.dictionary = {}
        if initial_data:
            for item in initial_data:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)


    def __init__(self, initial_data=None):
        self.dictionary = {}
        if initial_data:
            for item in initial_data:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)

