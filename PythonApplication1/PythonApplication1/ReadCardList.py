
# testing how to use json in python
import json # allows Python to use JSON
import os

class ReadCardList():

    #methor to return whole list

    #method to return specific item

    #list directory contents
    #print(os.listdir())

    #List current working directory
    print("Current Working Directory " , os.getcwd())

    try:
        #Change directory to the one I need to
        os.chdir("D:\\3 My New Game\\PythonGameCode\\PythonApplication1\\PythonApplication1\\JSON Files")

    except:
        print("Can't change the Current Working Directory") 

    #test line of code
    #with open('EquipmentLibrary.json') as EquipL: data = json.load(EquipL)

    #get Equipment Library and print to screen
    with open('CardLibrary.json') as CardL:
        data = json.load(CardL)
    print(json.dumps(data, indent=4))