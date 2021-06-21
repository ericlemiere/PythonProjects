
import os


fileName = "testA.rtf"

filePath = "/Users/ericlemiere/Documents/GitHub/PythonProjects/A"


abPath = os.path.join(filePath, fileName)

directoryList = os.listdir(filePath)


def printAllFiles():
    print("\nThe directory:\n")
    print(filePath)
    print("\nContains the following files:\n")
    for file in directoryList:
        newPath = os.path.join(filePath, file) #file path for individual files
        lastModified = os.path.getmtime(newPath) #gets time of last modification for this file
        lmString = str(lastModified) #turns float into string
        print(file + "\t-\t last modified:\t" + lmString)


def printtxtFiles(): #function traverses through directory and prints .txt files
    print("\nThese are the .txt files in the directory:")
    for file in directoryList:
        fileName = file
        if fileName.endswith('.txt'):
            print(fileName)


def getTimeFromPath():
    lastModified = os.path.getmtime(filePath)
    print("\nLast modification in directory: " + str(lastModified) + "\n")


if __name__ == "__main__":

    printAllFiles()
    printtxtFiles()
    getTimeFromPath()
