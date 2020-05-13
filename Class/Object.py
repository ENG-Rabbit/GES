from Class.Code import Code,Create_code
class Object:
    object_list = []
    def __init__(self,name = "",code = None,location = "",*args,**kwargs):
        Object.object_list.append(self)
        self.name = name
        if not code is None:
            self.code = Code(code)
        else:
            self.code = Create_code()
        self.Location = location
    def __str__(self):
        return self.name