

class Encap:                        ##Declare the class
    def __init__(self):             ##initiate the class
        self.__priVar = 500         ##set private variable
        self._proVar = 1000         ##set protected variable

obj = Encap()                       ##enstatiate the object

obj.__priVar = 250                  ##set private variable to 250, allowing
                                    ##access outside of the class
obj._proVar = 500                   ##set protected variable to 500

##print each variable
print("Private variable = {}, \nProtected Variable = {}".format(obj.__priVar, obj._proVar))















