from Smart_Home.Class.Furniture import Furniture
from .Checker import default_location


class_names = []
com = Furniture.furniture_list

def Subject(*args):
    """
    # برای مشخص کردن فاعل افعال 
    ###   باید بین وسایل انتخاب شوند
    ---
    در صورتی که نیاز بود تمام وسایل یک کار مشخص را انجام دهند می توان ورودی وارد نکرد و یا از\n
    .استفاده کرد `all`  \n
    می توان اطلاعات را به صورت لیستی یا به صورت تکی وارد کرد.
    اطلاعاتی که از  یک وسیله می توان داد برای انتخاب شامل:
        نام/مکان/خود وسیله/نوع\n
        Subject() or Subject("all") --> انتخاب تمام وسایل \n
        Subject('['Lamp,"Home","لامپ 2","lamp_3"']') or Subject(Lamp,"Home","لامپ 2","lamp_3") --> lamp'_'3 تمام چراغ ها و تمام وسایلی که در خانه قرار دارند، لامپ 2 و وسیله  
    """
    args = list(args)
    for ffl in com:
        if not ffl in class_names:
            class_names.append(type(ffl))
    obj_list = []
    for i in range(len(args)-1):
        if args[i] == None:
            args.remove(None)
    for i in range(len(args)): 
        if args[i] == "all" or len(args)==0:
            for obj in com:
                obj_list.append(obj)  
        if type(args[i]) == list:
                for obj in com:
                    if obj.Location in args[i] or type(obj) in args[i] or obj in args[i] or obj.name in args[i]:
                        obj_list.append(obj)
        elif args[i] in class_names:
            for obj in com:
                if type(obj) == args[i]:
                    obj_list.append(obj)
        elif args[i] in default_location.keys():
            for obj in com:
                if obj.Location == args[i]:
                    obj_list.append(obj)
        else:
            for obj in com:
                if obj in args or args[i] == obj.name:
                    obj_list.append(obj)
    return obj_list
