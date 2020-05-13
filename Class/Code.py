class Code:
    """
    str --> hex(with or without \"#\") to int

    int --> int to hex
    """

    code_list = []

    def __init__(self,value = "#"):
        try:
            self.code = int(value[1:],16)
        except:
            raise ValueError("Code Has Wrong Format!")
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

    def Create_code(self):
        pass
"""
def inttohex(num = None,dig=None):
    let = {15:"f",14:"e",13:"d",12:"c",11:"b",10:"a",9:"9",8:"8",7:"7",6:"6",5:"5",4:"4",3:"3",2:"2",1:"1",0:"0"}
    ith = ""
    while 1:
        h = num % 16
        num = num//16
        if h in let.keys():
            ith = let[h] + ith
        if num == 0:
            break
    hash_dig =  "#"
    if dig is None:
        dig = len(ith)
    elif type(dig) == int:
        for i in range(dig-len(ith)):
            hash_dig +=  "0"
    ith = hash_dig + ith
    del let
    return ith
def is_hex(num = None):
    if num:
        if type(num) is str and num[0]=="#":
            return True
        else:
            return False
    else:
        return None
"""
