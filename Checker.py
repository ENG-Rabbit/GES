from Smart_Home.Class.Object import Object
#from Smart_Home.Class.Code import is_hex,hexe,inttohex
from Smart_Home.Class.Code import Code,Create_code
#from Furniture import Furniture

default_location = {"Table":[],"Home":[],"Mobile":[]}
names = []

def Check():
    for obj in Object.object_list:
        if not obj.Location in default_location.keys():
            print('wrong location!')
        else:
            if not obj.name in default_location[obj.Location]:
                default_location[obj.Location].append(obj)
            else:
                print("Wrong name in {}.".format(obj.Location))
        if obj.code in Code.code_list:
            print("Wrong code!")
            print("You can choose:",end=" ")
            print(Create_code(),end=" ")
            print("instead {} in {}".format(obj.code,obj.Location))


