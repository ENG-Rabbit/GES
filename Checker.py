import sys
sys.path.append("./") 
from Smart_Home.Object import Object
from Smart_Home.Hex import is_hex,hexe,inttohex
#from Furniture import Furniture

default_location = {"Table":[],"Home":[],"Mobile":[]}
codes = []
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
        if not int(hexe(obj.code)) in codes:
            codes.append(int(hexe(str(obj.code))))
            codes.sort()
        else:
            print("Wrong code!")
            print("You can choose:",end=" ")
            for i in range(1,4096):
                if not i in codes:
                   i = inttohex(i,3)
                   break
            print(str(i),end=" ")
            print("instead {} in {}".format(obj.code,obj.Location))


