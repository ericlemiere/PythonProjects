


import ourModule
import datetime




if __name__ == "__main__":
    results = ourModule.getNumbers(12, 5)
    print(results)

    x = datetime.datetime.now()
    print(x)

    print(x.strftime("%B") + " " + x.strftime("%d") + " " + x.strftime("%Y"))
