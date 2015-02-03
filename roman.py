#roman.py
from math import *


class Roman:
    """
    Roman Class
    """
    
    def __init__(self, x):
        """
        Roman Class Constructor. Roman(x)
        x is an integer that's absolute value is less than 2,000,000
        """
        
        if(type(x) != int):
            raise ValueError("For Roman(x), x MUST be an integer")          
        if(2000000 < abs(x)):
            raise ValueError("For Roman(x), abs(x) cannot be more than 2 million")      
        self.dataInt = x
        self.dataString = self.intToRoman(x)

    def __repr__(self):
        return "Roman(" + str(self.dataInt) + ")"
    
    def __str__(self):
        return self.dataString

    def intToRoman(self, x):
        temp = x        
        s = ""
        #Case where temp = 0        
        if(temp == 0): 
            return "N"
        #Account for negative
        if(temp < 0):
            s += "-"            
            temp = -1 * temp
        #Start building Roman Numeral here        
        while(temp >= 1000000):
            s += "(M)"
            temp -= 1000000
        while(temp >= 900000):
            s += "(C)(M)"
            temp -= 900000
        
        while(temp >= 500000):
            s += "(D)"
            temp -= 500000
        while(temp >= 400000):
            s += "(C)(D)"
            temp -= 400000

        while(temp >= 100000):
            s += "(C)"
            temp -= 100000
        while(temp >= 90000):
            s += "(X)(C)"
            temp -= 90000

        while(temp >= 50000):
            s += "(L)"
            temp -= 50000
        while(temp >= 40000):
            s += "(X)(L)"
            temp -= 40000

        while(temp >= 10000):
            s += "(X)"
            temp -= 10000
        while(temp >= 9000):
            s += "M(X)"
            temp -= 9000

        while(temp >= 5000):
            s += "(V)"
            temp -= 5000
        while(temp >= 4000):
            s += "M(V)"
            temp -= 4000

        while(temp >= 1000):
            s += "M"
            temp -= 1000
        while(temp >= 900):
            s += "CM"
            temp -= 900

        while(temp >= 500):
            s += "D"
            temp -= 500
        while(temp >= 400):
            s += "CD"
            temp -= 400
        
        while(temp >= 100):
            s += "C"
            temp -= 100
        while(temp >= 90):
            s += "XC"
            temp -= 90
        
        while(temp >= 50):
            s += "L"
            temp -= 50
        while(temp >= 40):
            s += "XL"
            temp -= 40

        while(temp >= 10):
            s += "X"
            temp -= 10
        while(temp >= 9):
            s += "IX"
            temp -= 9

        while(temp >= 5):
            s += "V"
            temp -= 5
        while(temp >= 4):
            s += "IV"
            temp -= 4
        while(temp >= 1 ):
            s += "I"
            temp -= 1
        return s
    
    def __add__(self, other):
        if(type(other) == Roman):        
            return Roman(self.dataInt + other.dataInt)
        elif(type(other) == int):
            return Roman(self.dataInt + other)
        else:
            raise ValueError("+ used incorrectly")
    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if(type(other) == Roman):        
            return Roman(self.dataInt - other.dataInt)
        elif(type(other) == int):
            return Roman(self.dataInt - other)
        else:
            raise ValueError("- used incorrectly")
    def __rsub__(self, other):
        if(type(other) == Roman):        
            return Roman(other.dataInt - self.dataInt)
        elif(type(other) == int):
            return Roman(other - self.dataInt)
        else:
            raise ValueError("- used incorrectly")

    def __mul__(self, other):
        if(type(other) == Roman):        
            return Roman(self.dataInt * other.dataInt)
        elif(type(other) == int):
            return Roman(self.dataInt * other)
        else:
            raise ValueError("* used incorrectly")
    def __rmul__(self, other):
        return self.__mul__(other)   

    def __floordiv__(self, other):
        if(type(other) == Roman):        
            return Roman(self.dataInt // other.dataInt)
        elif(type(other) == int):
            return Roman(self.dataInt // other)
        else:
            raise ValueError("// used incorrectly")
    def __rfloordiv__(self, other):
        if(type(other) == Roman):        
            return Roman(other.dataInt // self.dataInt)
        elif(type(other) == int):
            return Roman(other // self.dataInt)
        else:
            raise ValueError("// used incorrectly")

    def __truediv__(self, other):
        if(type(other) == Roman):        
            return (Roman(self.dataInt // other.dataInt), Roman(self.dataInt % other.dataInt))
        elif(type(other) == int):
            return (Roman(self.dataInt // other), Roman(self.dataInt % other))
        else:
            raise ValueError("/ used incorrectly")
    def __rtruediv__(self, other):
        if(type(other) == Roman):        
            return (Roman(other.dataInt // self.dataInt), Roman(other.dataInt % self.dataInt))
        elif(type(other) == int):
            return (Roman(other // self.dataInt), Roman(other % self.dataInt))
        else:
            raise ValueError("/ used incorrectly")

    def __pow__(self, other):
        if(type(other) == Roman):        
            return Roman(self.dataInt ** other.dataInt)
        elif(type(other) == int):
            return Roman(self.dataInt ** other)
        else:
            raise ValueError("** used incorrectly")
    def __rpow__(self, other):
        if(type(other) == Roman):        
            return Roman(other.dataInt ** self.dataInt)
        elif(type(other) == int):
            return Roman(other ** self.dataInt)
        else:
            raise ValueError("** used incorrectly")

    def __eq__(self, other):
        if(type(other) == Roman):            
            if(self.dataInt == other.dataInt):
                return True
            else:
                return False
        elif(type(other) == int):
            if(self.dataInt == other):
                return True
            else:
                return False
        else:
            raise ValueError("== used incorrectly")
 
    def __ne__(self, other):
        if(type(other) == Roman):            
            if(self.dataInt != other.dataInt): return True
            else: return False
        elif(type(other) == int):
            if(self.dataInt != other): return True
            else: return False
        else:
            raise ValueError("!= used incorrectly")

    def __lt__(self, other):       
        if(type(other) == Roman):            
            if(self.dataInt < other.dataInt):
                return True
            else:
                return False
        elif(type(other) == int):
            if(self.dataInt < other):
                return True
            else:
                return False
        else:
            raise ValueError("< used incorrectly")
    
    def __le__(self, other):
        if(type(other) == Roman):            
            if(self.dataInt <= other.dataInt):
                return True
            else:
                return False
        elif(type(other) == int):
            if(self.dataInt <= other):
                return True
            else:
                return False
        else:
            raise ValueError("<= used incorrectly")
    
    def __ge__(self, other):
        if(type(other) == Roman):            
            if(self.dataInt >= other.dataInt):
                return True
            else:
                return False
        elif(type(other) == int):
            if(self.dataInt >= other):
                return True
            else:
                return False
        else:
            raise ValueError(">= used incorrectly")
    
    def __gt__(self, other):
        if(type(other) == Roman):            
            if(self.dataInt > other.dataInt):
                return True
            else:
                return False
        elif(type(other) == int):
            if(self.dataInt > other):
                return True
            else:
                return False
        else:
            raise ValueError("> used incorrectly")

    def __neg__(self):
        return Roman(-1 * self.dataInt)

for i in range(0, 1001, 1):
    G = globals()
    G[Roman(i).dataString] = Roman(i)


    



