



def getInfo():
    var1 = input("Please provide an integer: ")
    var2 = input("Please provide another integer: ")
    return var1, var2



def compute():
    go = True
    while go:
        var 1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}: \nYou did not provide valid integers.".format(e))
        except:
            print("Invalid Input.")

    print("{} + {} = {}".format(var1,var2,var3))














if __name__ == "__main__":
    compute()
