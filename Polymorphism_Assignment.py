

class Superhero:
    name = ""
    alias = ""
    origin = ""
    abilities = ""

    def greeting(self):
        sh_name = self.name
        sh_alias = self.alias
        sh_abilities = self.abilities
        print("\nYou are {}, also known as {}.".format(sh_name,sh_alias))
        print("Your abilities are: {}\n".format(sh_abilities))
        
    def weakness(self):
        print("\nEvery superhero has a weakness.\n")

        

class Ironman(Superhero):
    name = "Ironman"
    alias = "Tony Stark"
    origin = "Earth"
    abilities = "Genius, Billionaire, Playboy, Philanthropist with a fancy metal flying suit."

    def weakness(self):
        print("Your weakness is your ego.\n")


class Superman(Superhero):
    name = "Superman"
    alias = "Clark Kent"
    origin = "Krypton"
    abilities = "X-ray vision, power of flight, extreme strength, and cold breath."

    def weakness(self):
        print("Your weakness is Kryptonite.\n")
    
























    

if __name__ == "__main__":
    
    superhero = Superhero()
    superhero.weakness()
    
    ironman = Ironman()
    ironman.greeting()
    ironman.weakness()

    superman = Superman()
    superman.greeting()
    superman.weakness()
    
