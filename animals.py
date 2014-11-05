class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = self.species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expectancy = self.species.life_expectancy

    def grow(self, age, weight):
        self.age += age
        self.weight += weight
        print("%s the %s has grown and is now %s years old and weighs %s kgs" % (
            self.name, self.species, self.years, self.weight))

    def eat(self, food):
        print("%s the %s ate %s today" % (self.name, self.species, food))

    def can_die(self):
        pass

    def chance_to_die(self):
        return self.age / self.life_expectancy


class Species:

    def __init__(self, species, life_expectancy):
        self.species = species
        self.life_expectancy = life_expectancy
