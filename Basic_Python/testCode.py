

mySent = "loves this color:"

colorList = ['red','blue','orange','black']


def color_func(name):
    lst = []
    for i in colorList:
        msg = "{} {} {}".format(name,mySent,i)
        lst.append(msg)
    return lst



def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('Please provide name: ')
        else:
            go = False
    lst = color_func(name)
    for i in lst:
        print(i)

get_name()


