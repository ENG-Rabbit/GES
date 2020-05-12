#import sys
#sys.path.append("./") 
#print(sys.path)
from Smart_Home.Hex import is_hex,inttohex
from Smart_Home.Attributes import light,Sound,Picture
from Smart_Home.Methods import States,Rotate
from Smart_Home.Object import Object
from Smart_Home.Sensors import temp_hum_S
from Smart_Home.Checker import codes
#import gc
#import weakref


def code_finder():
    for i in range(1,4096):
                if not i in codes:
                   i = inttohex(i,3)
                   break
    return i


class Furniture(States,Object):
    furniture_list=[]
    def __init__(self,name = "",code = "",location = "",state = False,*args,**kwargs):
        super().__init__(name=name,code=code,location=location,state = state,*args,**kwargs)
        for key, value in kwargs.items():
            setattr(self,key,value)
        self.name = name
        Furniture.furniture_list.append(self)


class Lamp(light, Furniture):
    """
    ##  می تواند نور داشته باشد و رنگ نور را تغییر دهد
    --------------
    ### متد ها:
    
    RGB_Changer(): برای تغییر رنگ\n

    ----------
    ### Attributes:

    state =  روشن یا خاموش بودن\n
        True --> روشن | False --> خاموش\n
    RGB : .باید به صورت `هگز` و به شکل زیر وارد شود\n
         Format --> "#ffffff"
    brightness = .باید به صورت عدد صحیح و بین 0 و100 وارد شود \n
    R : قرمز\n
    G : سبز\n
    B : آبی\n\n

    ** .با افزودن لامپ ها به همدیگر یا یک دسته لامپ می توان یک دسته لامپ ساخت و تمام لامپ های آن دسته را باهم ویرایش کرد 
    """
    def __init__(self,name = "",code = "",state = False,location='',RGB = "#000000",brightness = 00,*args, **kwargs):
        super().__init__(name=name,code = code,location=location,state=state,RGB=RGB,brightness=brightness,*args, **kwargs)
        
        if not is_hex(RGB):
            raise ValueError("write a hex for RGB!(hex start with \"#\")")
        self.RGB = RGB
        if type(RGB) is int:
            raise ValueError("مقدار RGB را به صورت هگز و متنی وارد کنید.")
        if RGB[0] == "#":
            RGB = RGB[1:]
        self.RGB = RGB
        self.Red =  "#" + RGB[0:2]
        self.Green =  "#" + RGB[2:4]
        self.Blue = "#" + RGB[4:6]
        self.brightness = brightness
        self.location=location
    def __add__(self,other):#TODO location dorost shavad.
        i= code_finder()
        if type(other) == Lamp:
            return Lamps(name="رشته لامپ",code='#006',state = (self.state and other.state),location=self.location,RGB = "#"+self.RGB,brightness = self.brightness,number_lamp=2)

        elif type(other) == Lamps:
            return Lamps(name="رشته لامپ",code=i,state = other.state,location=other.location,RGB = "#"+ other.RGB,brightness = other.brightness,number_lamp=other.number_lamp + 1)


class Lamps(Lamp):
    def __init__(self,name = "",code = "",state = False,location='',RGB = "#000000",brightness = 00,number_lamp=2,*args, **kwargs):
        super().__init__(name=name,code = code,location=location,state=state,RGB=RGB,brightness=brightness,*args, **kwargs)
        self.number_lamp = number_lamp


    def __add__(self,other):
        i = code_finder()
        if type(other) == Lamps:
            return Lamps(name="رشته لامپ",code=i,state = (self.state and other.state),location=self.location,RGB = "#"+ self.RGB,brightness = self.brightness,number_lamp=other.number_lamp + self.number_lamp)
        
        elif type(other) == Lamp:
            return Lamps(name="رشته لامپ",code=i,state = self.state,location=self.location,RGB = "#"+ self.RGB,brightness = self.brightness,number_lamp=1 + self.number_lamp) 

class Screen(Sound,Picture, Furniture):
    """
    ## هم صدا دارد هم تصویر
    --------------
    ### متد ها:

    sound_control(): برای استاپ/پلی کردن صدا یا کمو زیادکردن صدا یا میوت کردن صدا \n
    sound_looper(): برای مد حلقه صدا\n
    sound_speed_changer(): برای تغییر سرعت صدا\n
        (True-->افزایش سرعت|False-->کاهش سرعت)\n
    pic_control(): برای استاپ/پلی کردن تصویر یا کمو زیادکردن نور صفحه \n
    pic_looper(): برای مد حلقه تصویر \n
    pic_speed_changer(): برای تغییر سرعت تصویر\n
        (True-->افزایش سرعت|False-->کاهش سرعت)\n
    video_control(): برای استاپ/پلی کردن ویدئو  \n
    video_looper(): برای مد حلقه ویدئو \n
    video_speed_changer(): برای تغییر سرعت ویدئو\n
        (True-->افزایش سرعت|False-->کاهش سرعت)\n
    ----------
    ### ویژگی ها:

    state =  روشن یا خاموش بودن\n
        True --> روشن / False --> خاموش\n
    sound_value : حجم صدا که باید به بین 0 تا 100 انتخاب شود\n
    brightness : نور صفحه که باید بین 0 تا 100 انتخاب شود \n


    """
    def __init__(self,name="",code = "",state=False,location="",sound_value = 00,pic_brightness = 00,*args,**kwargs):
        super().__init__(name=name,code = code,location=location,
                            state=state,sound_value = sound_value,pic_brightness = pic_brightness,*args,**kwargs)
    def video_control(self,key = "p"):
        options_s = {"p":"play","s":"stop"}
        if key.lower() in options_s.keys():
            self.State_pic = options_s[key.lower()]
            self.State_sound = options_s[key.lower()]
    def video_looper(self,key_loop="nor"):
        """
        "nor": "no_repeat"\n
        "ol": "one_repeat"\n
        "al":"All_repeat"\n
        """
        options = {"nor": "no_repeat","ol": "one_repeat","al":"All_repeat"}
        if key_loop.lower() in options.keys():
            self.sound_Loop = options[key_loop.lower()]  
            self.pic_Loop = options[key_loop.lower()]
        else:
            raise ValueError("key_loop is Incorrect(\"nor\": \"no_repeat\",\"ol\": \"one_repeat\",\"al\":\"All_repeat\")")

    def video_speed_changer(self,speed = None):
        if speed is None:
            self.sound_speed = self.pic_speed
            return self.pic_speed
        elif speed:
            self.pic_speed += 0.1
        elif not speed:
            self.pic_speed -= 0.1
        self.sound_speed = self.pic_speed
        return self.pic_speed
    
class Door(Rotate,Furniture):#TODO add ADD
    """
    ## می تواند بچرخد
    --------------
    ### متد ها:

    Rotation(): برای چرخش \n
    Angle_converter(): برای تبدیل مقیاس زاویه \n

    ----------
    ### ویژگی ها:

    state =  روشن یا خاموش بودن\n
        True --> روشن / False --> خاموش\n
    initial_value : مقدار اولیه زاویه که باید بین 0 تا 360 درجه وارد شود.\n
    """
    def __init__(self,name="",code = "",state=False,location="",initial_value = 00,*args,**kwargs):
        super().__init__(name=name,code = code,state=state,location=location,initial_value = initial_value,*args,**kwargs)


class Speaker(Sound,Furniture):#TODO add ADD
    """
    ## فقط صدا دارد
    --------------
    ### متد ها:

    sound_control(): برای استاپ/پلی کردن صدا یا کمو زیادکردن صدا یا میوت کردن صدا \n
    sound_looper(): برای مد حلقه صدا\n
    sound_speed_changer(): برای تغییر سرعت صدا (True-->افزایش سرعت|False-->کاهش سرعت)\n
    
    ----------
    ### ویژگی ها:

    state =  روشن یا خاموش بودن\n
        True --> روشن / False --> خاموش (defult:False)\n
    sound_value : حجم صدا باید بین 0 تا 100 انتخاب شود (defult:0)\n
    """
    def __init__(self,name="",code = "",state=False,location="",sound_value = 00,*args,**kwargs):
        super().__init__(name=name,code = code,state=state,location=location,sound_value = sound_value,*args,**kwargs)


class Clock:
    pass


class Bluetooth:
    pass



    
