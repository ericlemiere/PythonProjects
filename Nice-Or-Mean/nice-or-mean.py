#
# Python:   3.9.5
#
# Author:   Eric Lemiere
#
#
#
#


from playsound import playsound
from PIL import Image

#Load the image
img = Image.open('smile.png')



def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice,mean,name)
    


def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get user's name.
        If not, thank player for playing again
    """

    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nPlease enter your name: ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("In this game, you will be greeted by ")
                    print("several different people. You can choose ")      
                    print("to be nice or mean, but at the end of the ")
                    print("game, your fate will be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaces you for a conversation. \nWill you be nice or mean? (N/M) ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling... ")
            nice += 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you and storms off... ")
            mean += 1
            stop = False
        else:
            print("\nPlease enter n for nice or m for mean: ")
    score(nice,mean,name) #pass the three variables to score() to update score

    
        
def show_score(nice, mean, name):
    print("\n{} - Your current score is... ".format(name))
    print("Nice: {}".format(nice))
    print("Mean: {}".format(mean))



def score(nice, mean, name):
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    img.show()
    print("\nWell, {}... it turns out you're a nice person!".format(name))
    again(nice,mean,name)


def lose(nice,mean,name):
    print("\nWell, {}... it turns out you're not a very nice person!".format(name))
    playsound('snap.wav')
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (y/n) ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nThank you for playing.")
            stop = False
            quit()
        else:
            print("\nPlease enter y for yes or n for no (y/n) ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # We don't reset name because player may play again
    start(nice,mean,name)





































if __name__ == "__main__":
    start()














    
