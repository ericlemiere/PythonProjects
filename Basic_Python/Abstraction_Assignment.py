
# Import
from abc import ABC, abstractmethod


# Parent class
class GreatDane(ABC):

    # Regular method
    def gdGreeting(self):
        print("\nThe Great Dane is a majestic animal.\n")

    # Abstract method that child classes can call
    @abstractmethod
    def gdColor(self):
        pass

# ==================================================================
# Child classes
class BlueDane(GreatDane):
    # This method defines the abstract method in parent class
    def gdColor(self): 
        print("""The Blue Dane has blue-ish gray fur
and is the most beautiful of them all.\n""")


class FawnDane(GreatDane):
    # This method defines the abstract method in parent class
    def gdColor(self): 
        print("""A Fawn-colored Dane has tan fur with a black muzzle
and is the traditional color for the Great Dane.\n""")

# End Child classes
# ==================================================================





if __name__ == "__main__":
    dog1 = BlueDane()
    dog1.gdGreeting()
    dog1.gdColor()

    dog2 = FawnDane()
    dog2.gdColor()
    
