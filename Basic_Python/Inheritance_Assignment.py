

class User:
    #define the attributes of the class
    name = "not provided"
    email = ""
    password = ""
    account = 0

    #define the methods of the class
    def login(self):
        entryEmail = input("Enter your email: ")
        entryPassword = input("Enter your password: ")
        if (entryEmail == self.email and entryPassword == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("Incorrect name or password.")

    #define the initialization
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account


#create instance of the User class outside of class
new_user = User("John Doe", "john@johndoe.com","p@ssw0rd", 1234)

#call the login method
new_user.login()



#child class of User class
class Employee(User):
    #extra attributes unique to Employee
    employeeNum = 0
    basePay = 15
    employeeBenefits = False
    jobTitle = ""


#child class of User class
class Customer(User):
    customerNumber = 0
    orders = 0
    
