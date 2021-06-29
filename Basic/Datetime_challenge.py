import datetime as dt
from datetime import timezone, timedelta

import pytz
from pytz import timezone



def Branches():

    # assign times in timezones to variables
    currentTime = dt.datetime.now(timezone('UTC'))
    portlandTime = dt.datetime.now(timezone('US/Pacific'))
    newyorkTime = dt.datetime.now(timezone('US/Eastern'))
    londonTime = dt.datetime.now(timezone('Europe/London'))

    # call printInfo function and pass it variables
    printInfo("Portland",portlandTime)
    printInfo("New York",newyorkTime)
    printInfo("London",londonTime)

    




def printInfo(name,x):

    if int(x.strftime("%H")) >= 9 and \
       int(x.strftime("%H")) <= 17 :
        print("\nThe {} branch is currently open".format(name))
    else:
        print("\nThe {} branch is currently closed".format(name))

    print("Local Time is {}:{} {}\n".format(x.strftime("%I"),
                                            x.strftime("%M"),
                                            x.strftime("%p")))


if __name__ == "__main__":
    Branches()
