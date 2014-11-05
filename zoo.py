class Zoo:

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

    def accomodate(self, animal):
        if animal not in self.animals:
            self.animals[animal] = []
        else:
            

