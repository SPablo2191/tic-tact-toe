import random
class Player:
    def __init__(self,name : str,token : str):
        self.__name = name
        self.__token = token
    def doAMove(self):
        return self.__token
    def randomChoice(self):
        return random.randint(1,9)
    def getName(self):
        return self.__name
