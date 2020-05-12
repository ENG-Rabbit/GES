class hexe():
    """
    str --> hex(with or without \"#\") to int

    int --> int to hex
    """
    def __init__(self,value = 00):
        self.Hnum = hextoint(value)
    #Dtypes
    def __str__(self):
        return str(self.Hnum)

    def __int__(self):
        return int(self.Hnum)

    def __float__(self):
        raise ValueError("HEX can't be float!")
    #Oprators
    ##adds
    def __add__(self,other):
        return self.Hnum + hextoint(other)
    
    def __radd__(self,other):
        return hextoint(other) + self.Hnum 

    def __iadd__(self,other):
        return hextoint(other) + self.Hnum 
    ##subs
    def __sub__(self,other):
        return self.Hnum - hextoint(other)
    
    def __rsub__(self,other):
        return hextoint(other) - self.Hnum 

    def __isub__(self,other):
        return hextoint(other) - self.Hnum 
    ##multiple
    def __mul__(self,other):
        return self.Hnum * hextoint(other)
    
    def __rmul__(self,other):
        return hextoint(other) * self.Hnum 

    def __imul__(self,other):
        return hextoint(other) * self.Hnum 
    ##division
    def __div__(self,other):
        return self.Hnum / hextoint(other)
    
    def __rdiv__(self,other):
        return hextoint(other) / self.Hnum 

    def __idiv__(self,other):
        return hextoint(other) / self.Hnum 
    ##floordiv
    def __floordiv__(self,other):
        return self.Hnum // hextoint(other)
    
    def __rfloordiv__(self,other):
        return hextoint(other) // self.Hnum 

    def __ifloordiv__(self,other):
        return hextoint(other) // self.Hnum 
    ##power
    def __pow__(self,other):
        return self.Hnum ** hextoint(other)
    
    def __rpow__(self,other):
        return hextoint(other) ** self.Hnum 

    def __ipow__(self,other):
        return hextoint(other) ** self.Hnum 
    ##power
    def __mod__(self,other):
        return self.Hnum % hextoint(other)
    
    def __rmod__(self,other):
        return hextoint(other) % self.Hnum 

    def __imod__(self,other):
        return hextoint(other) % self.Hnum 
    #Logical
    def __lt__(self, other):
        return hextoint(other) > self.Hnum
    def __gt__(self, other):
        return hextoint(other) < self.Hnum
    def __le__(self, other):
        return hextoint(other) >= self.Hnum
    def __ge__(self, other):
        return hextoint(other) <= self.Hnum
    def __eq__(self, other):
        return hextoint(other) == self.Hnum
    def __ne__(self, other):
        return hextoint(other) != self.Hnum
    #other
    def __neg__(self):
        return -(self.Hnum)
    def __pos__(self):
        return +(self.Hnum)
    def __abs__(self):
        if self.Hnum < 0:
            return -(self.Hnum)
        else:
            return self.Hnum
def hextoint(num = None):
    if type(num) is int:
        return num
    #num = num.lower()
    digits = {"f":15,"e":14,"d":13,"c":12,"b":11,"a":10,"F":15,"E":14,"D":13,"C":12,"B":11,"A":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0}
    hti = 0
    i = 0
    if num[0] == "#":
            num = num[1:]
    for j in range(1,len(num)+1):
        if num[-j] in digits.keys():
            hti = hti + digits[num[-j]]*(16**i)
            i +=1
        else:
            raise ValueError("hex don't have {}.".format(num[-j]))
    del digits
    return hti
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
