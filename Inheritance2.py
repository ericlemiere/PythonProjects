

# parent class ========================================
class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.origin, self.carbon_based)
        return msg


# child classes ========================================
class Human(Organism):
    name = "Bruce Wayne"
    species = "Homosapien"
    legs = 2
    arms = 2
    orign = "Earth"

    def qualities(self):
        msg = "\nBillionaire vigilante with special equipment.\n"
        return msg


class Dog(Organism):
    name = "Hudson"
    species = "Canine"
    legs = 4
    arms = 0
    origin = "Earth"

    def qualities(self):
        msg = "\nLoyal creatures with maximum cuddlabliity.\n"
        return msg
    

class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    arms = 0
    legs = 0
    origin = "Mars"

    def replication(self):
        msg = "\nEliminate immediately. Dire threat to humanity.\n"
        return msg















if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.qualities())

    dog = Dog()
    print(dog.information())
    print(dog.qualities())

    bact = Bacterium()
    print(bact.information())
    print(bact.replication())






    
