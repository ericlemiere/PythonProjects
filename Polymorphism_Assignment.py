# ==========================  
# Parent class
# ==========================  
class Superhero:
    name = ""
    alias = ""
    origin = ""
    abilities = ""

    # Greeting prints name and alias of superhero
    def greeting(self):
        sh_name = self.name
        sh_alias = self.alias
        sh_abilities = self.abilities
        print("\nYou are {}, also known as {}.".format(sh_name,sh_alias))
        print("Your abilities are: {}\n".format(sh_abilities))

    # This method prints a generic weakness message    
    def weakness(self):
        print("\nEvery superhero has a weakness.\n")


# ==========================       
# Child classes of Superhero
# ==========================  

class Ironman(Superhero):
    name = "Ironman"
    alias = "Tony Stark"
    origin = "Earth"
    abilities = "Genius, Billionaire, Playboy, Philanthropist with a fancy metal flying suit."

    # This weakness method is specific to the Ironman class
    def weakness(self):
        print("Your weakness is your ego.\n")



class Superman(Superhero):
    name = "Superman"
    alias = "Clark Kent"
    origin = "Krypton"
    abilities = "X-ray vision, power of flight, extreme strength, and cold breath."

    # This weakness method is specific to the Superman class
    def weakness(self):
        print("Your weakness is Kryptonite.\n")
    











    

if __name__ == "__main__":

    # create instance of Superhero and print generic weakness message
    superhero = Superhero()
    superhero.weakness()

    # create instance of Ironman
    ironman = Ironman()
    ironman.greeting()
    ironman.weakness()

    # create instance of Superman
    superman = Superman()
    superman.greeting()
    superman.weakness()
    
