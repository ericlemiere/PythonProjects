

class Instructor:

    def __init__(self):
        self.__schoolName = "Tech Academy" # schoolName variable is private
        self._name = "Mr. Clark" #name is protected
    

    def printInfo(self):
        print("Instructor: \t", self._name)
        print("School:     \t", self.__schoolName)


    # Calling this method allows for _name to be changed
    def changeName(self, newName): 
        self._name = newName

    def __changeSchoolName(self, newSchoolName):
        self.__schoolName = newSchoolName
        


if __name__ == "__main__":
    var = Instructor()
    var.printInfo()
    var.changeName("Mrs. Clark")
    var.printInfo()
    var._Instructor__changeSchoolName("The Tech Academy")
    var.printInfo()
        
