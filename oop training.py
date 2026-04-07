import requests

class Species:
    def __init__(self,population, growth_rate):
        self.population = population
        self.growth_rate = growth_rate

    def grow(self):
        self.population += self.population*self.growth_rate

sp = Species(100, 5)
print(sp.population)
sp.grow()
print(sp.population)

class Predator(Species):
    def __init__(self, population, growth_rate, hunting_success_rate):
        Species.__init__(self, population, growth_rate)
        self.hunting_success_rate = hunting_success_rate

    def survive(self):
        self.population -= self.population*(1 - self.hunting_success_rate)

pred = Predator(1000, 0.02, 1.05)
print(pred.population)
pred.survive()
print(pred.population)

class Herbivore(Species):
    def __init__(self, population, growth_rate, food_availability):
        Species.__init__(self, population, growth_rate)
        self.food_availability = food_availability

    def migrate(self):
        self.population -= self.population*0.2
        self.food_availability = 0.3

    def grow(self):
        if self.food_availability > 0.2:
            self.population += self.population*self.growth_rate
            self.food_availability -= 0.15
        else:
            self.migrate()

herb = Herbivore(2000, 0.04, 0.3)
herb.grow()
herb.grow()
print(herb.population)
print(herb.food_availability)

class Omnivore(Predator, Herbivore):
    def __init__(self, population, growth_rate, food_availability, hunting_success_rate, diet_balance):
        Predator.__init__(self, population, growth_rate, hunting_success_rate)
        Herbivore.__init__(self, population, growth_rate, food_availability)
        self.diet_balance = diet_balance

    def grow(self):
        if self.diet_balance >= 0.5:
            Predator.survive(self)
        else:
            Herbivore.grow(self)

omni = Omnivore(1000, 0.05, 1, 0.6, 0.4)
print(omni.population)
omni.grow()
print(omni.population)

omni_2 = Omnivore(500, 0.02, 1.2, 0.5, 0.6)
print(omni_2.population)
omni_2.grow()




