if __name__ == "__main__":
    print(__name__)
else:
    print(1212)
class Code:
    """
    str --> hex(with or without \"#\") to int

    int --> int to hex
    """

    code_list = []

    def __init__(self,value = "#"):
        self.val = value
        if self.is_code():
            self.code = int(value[1:],16)
        else:
            raise ValueError("Code Has Wrong Format!")
        del value
        del self.val
        if not self.code in Code.code_list:
            Code.code_list.append(self.code)

    #Dtypes
    def __str__(self):
        return "#" + hex(self.code).lstrip("0x")

    def __int__(self):
        return self.code

    def __float__(self):
        raise ValueError("Code can't be float!")

    def __hex__(self):
        return "#" + hex(self.code).lstrip("0x")
    #Oprators
    ##adds
    def __add__(self,other):
        return self.code + int(other,16)
    
    def __radd__(self,other):
        return int(other,16) + self.code 

    def __iadd__(self,other):
        return int(other,16) + self.code 
    ##subs
    def __sub__(self,other):
        return self.code - int(other,16)
    
    def __rsub__(self,other):
        return int(other,16) - self.code 

    def __isub__(self,other):
        return int(other,16) - self.code 
    ##multiple
    def __mul__(self,other):
        return self.code * int(other,16)
    
    def __rmul__(self,other):
        return int(other,16) * self.code 

    def __imul__(self,other):
        return int(other,16) * self.code 
    ##division
    def __div__(self,other):
        return self.code / int(other,16)
    
    def __rdiv__(self,other):
        return int(other,16) / self.code 

    def __idiv__(self,other):
        return int(other,16) / self.code 
    ##floordiv
    def __floordiv__(self,other):
        return self.code // int(other,16)
    
    def __rfloordiv__(self,other):
        return int(other,16) // self.code 

    def __ifloordiv__(self,other):
        return int(other,16) // self.code 
    ##power
    def __pow__(self,other):
        return self.code ** int(other,16)
    
    def __rpow__(self,other):
        return int(other,16) ** self.code 

    def __ipow__(self,other):
        return int(other,16) ** self.code 
    ##power
    def __mod__(self,other):
        return self.code % int(other,16)
    
    def __rmod__(self,other):
        return int(other,16) % self.code 

    def __imod__(self,other):
        return int(other,16) % self.code 
    #Logical
    def __lt__(self, other):
        return int(other,16) > self.code
    def __gt__(self, other):
        return int(other,16) < self.code
    def __le__(self, other):
        return int(other,16) >= self.code
    def __ge__(self, other):
        return int(other,16) <= self.code
    def __eq__(self, other):
        return int(other,16) == self.code
    def __ne__(self, other):
        return int(other,16) != self.code
    #other
    """
    def __neg__(self):
        return -(self.code)
    def __pos__(self):
        return +(self.code)
    """
    def __abs__(self):
        if self.code < 0:
            return -(self.code)
        else:
            return self.code
    def is_code(self):
        if type(self.val) is str and self.val[0] == "#" and len(self.val) == 4:
            return True
        else:
            return False
def Create_code():
    for i in range(1,4096):
            if not i in Code.code_list:
               i = inttohex(i,3)
               break
    return i
def inttohex(num=0,dig=None):
    ith = hex(num).lstrip("0x")
    hash_dig =  "#"
    if dig is None:
        dig = len(ith)
    elif type(dig) == int:
            hash_dig +=  ("0" * (dig-len(ith)))
    else:
        return "Can't do that!"
    return hash_dig + ith

