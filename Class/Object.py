#from .Hex import is_hex
class Object:
    object_list = []
    def __init__(self,name = "",code = "",location = "",*args,**kwargs):
        Object.object_list.append(self)
        self.name = name
        self.code = code
        self.Location = location
    def __str__(self):
        return self.name


#print(Object.object_list)
