import json

def readdata(filename):
    with open(filename) as file:
        inventory = json.load(file)
    
        return inventory