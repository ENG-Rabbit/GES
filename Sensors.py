import sys
sys.path.append("./") 
from Smart_Home.Methods import States
#from .Attributes import *
#from random import randint
from Smart_Home.Object import Object

class Sensor(Object):
    Sensor_List = []
    def __init__(self,name = "",code = "",location = "" ,*args,**kwargs):
        super().__init__(name=name,code=code,location=location,*args, **kwargs)
        for key, value in kwargs.items():
                setattr(self,key,value)
        Sensor.Sensor_List.append(self)                       
class temp_hum_S(Sensor):
    """
    # سنسور دما و رطوبت
    --------------
    ## متد ها
    -------
    get_temp(): برای گرفتن دما\n
    get_hum(): برای گرفتن رطوبت\n
    scale_converter(): برای تبدیل مقیاس\n
        (C,F and K)(default: "C")\n
    sey_value(): مقدار سنسور ها را بر میگرداند\n
        (دما,رطوبت)
    Attributes:
    ----------
    temp = دما به صورت اعشاری\n
    hum = رطوبت به صورت عدد صحیح\n
    temp_scale = مقیاس دما\n
    """
    def __init__(self,name="" ,code = "" ,temp = None ,hum=None ,location = "" ,*args ,**kwargs):
        super().__init__(name=name,code = code,location=location,*args,**kwargs)
        if temp is None:
            self.__temp = None
        else:
            self.__temp = float(temp)
        if hum is None:
            self.__hum = None
        else:
            self.__hum = int(hum)
        self.temp_scale = "C"
    def get_temp(self,data):
        """
        data = اطلاعات
        """
        self.__temp = data

    def get_hum(self,data):
        """
        data = اطلاعات
        """
        self.__hum = data

    def scale_converter(self,scale = "c"):
        """
        c = سلسیوس\n
        f = فارنهایت\n
        k = کلوین\n
        """
        if scale.lower() == "c":
            if self.temp_scale.lower() == "f":
                x = (self.__temp-32)/1.8
            elif self.temp_scale.lower() == "k":
                x = self.__temp - 273.15
            else:
                x = self.__temp
            self.temp_scale = "C"
        elif scale.lower() == "f":
            if self.temp_scale.lower() == "c":
                x = (self.__temp*1.8)+32
            elif self.temp_scale.lower() == "k":
                x = (self.__temp*(5/9))-459.67
            else:
                x = self.__temp
            self.temp_scale = "F"
        elif scale.lower() == "k":
            if self.temp_scale.lower() == "f":
                x = (self.__temp+459.67)*(5/9)
            elif self.temp_scale.lower() == "c":
                x = self.__temp + 273.15
            else:
                x = self.__temp
            self.temp_scale = "K"
        else:
            raise ValueError("choose a scale between c, f and k")
        self.__temp = round(x,2)

    def sey_value(self,type_say = "NT",Range_temp = 1,Range_hum = 1):
        """
        type_say: نوع نمایش\n
            ("N" --> به صورت معمولی | "P" --> به صورت درصدی ) | ("S" --> به صورت عددی | "T" --> به صورت متنی)
        ** اگر نمایش به صورت درصدی است می توان رنج دماو رطوبت را تغییر دهید\n
        Range_temp: رنج دما\n
        Range_hum: رنج رطوبت
        """
        if not ("p" in type_say.lower() or "n" in type_say.lower()):
            raise ValueError("Choose type_say between (P)ercent and (N)ormal")
        if not self.__temp is None and not self.__hum is None:
            if "p" in type_say.lower():
                self.__temp = (self.__temp/Range_temp)*100
                self.__hum = (self.__hum/Range_hum)*100
            if "s" in type_say.lower():
                return (self.__temp,self.__hum)
            else:
                return "temp_hum_S" "::" + str(self.__temp) + "::" + str(self.__hum)   
        elif not self.__temp is None:
            if type_say.lower() == "p":
                self.__temp = (self.__temp/Range_temp)*100
            if "s" in type_say.lower():
                return (self.__temp)
            else:
                return "temp_hum_S" "::" + str(self.__temp)
        elif not self.__hum is None:
            if type_say.lower() == "p":
                self.__hum = (self.__hum/Range_hum)*100
            if "s" in type_say.lower():
                return (self.__hum)
            else:
                return "temp_hum_S" "::" + str(self.__hum)
        else:
            return False
    def __str__(self):
        return self.sey_value("nt")
    def __int__(self):
        if not self.__hum is None:
            return self.__hum
        else:
            return 0
    def __float__(self):
        if not self.__temp is None:
            return self.__temp
        else:
            return 0.0
    def __eq__(self, other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp == other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum == other.sey_value("ns"):
                return True    
        elif (self.__temp,self.__hum) == other.sey_value("ns"):
            return True    
        else:
            return False
    def __ne__(self,other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp != other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum != other.sey_value("ns"):
                return True
        elif (self.__temp,self.__hum) != other.sey_value("ns"):
            return True        
        else:
            return False
    def __lt__(self, other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp < other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum < other.sey_value("ns"):
                return True      
        elif (self.__temp,self.__hum) < other.sey_value("ns"):
            return True  
        else:
            return False 
    def __gt__(self,other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp > other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum > other.sey_value("ns"):
                return True 
        elif (self.__temp,self.__hum) > other.sey_value("ns"):
            return True       
        else:
            return False
    def __le__(self,other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp <= other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum <= other.sey_value("ns"):
                return True 
        elif (self.__temp,self.__hum) <= other.sey_value("ns"):
            return True       
        else:
            return False 
    def __ge__(self,other):
        if type(other) != temp_hum_S:
            return None
        if self.__hum is None:
            if self.__temp >= other.sey_value("ns"):
                return True
        elif self.__temp is None:
            if self.__hum >= other.sey_value("ns"):
                return True   
        elif (self.__temp,self.__hum) >= other.sey_value("ns"):
            return True     
        else:
            return False   
class light_S(Sensor):
    """
    # سنسور نور
    --------------
    ## متد ها

    get_value(): برای گرفتن شدت نور\n
    sey_value(): برای نمایش مقدار شدت نور \n
    ---
    ## ویژگی ها
    lux: شدت نور\n
        (default: 00)
    """
    def __init__(self,name = "", code = "",lux = 00,location = "" ,*args ,**kwargs):
        super().__init__(name=name,code = code,location=location,*args,**kwargs)
        self.__lux = lux
    def get_value(self,data):
        """
        data = اطلاعات
        """
        self.__lux = data
    def sey_value(self,type_say = "NT",Range_lux = 1):
        """
        type_say: نوع نمایش\n
            ("N" --> به صورت معمولی | "P" --> به صورت درصدی ) | ("S" --> به صورت عددی | "T" --> به صورت متنی)
        ** اگر نمایش به صورت درصدی است می توان رنج شدت نور را تغییر دهید\n
        Range_lux: رنج شدت نور\n
        
        """
        if not ("p" in type_say.lower() or "n" in type_say.lower()):
            raise ValueError("Choose type_say between (P)ercent and (N)ormal")
        if not self.__lux is None:
            if "p" in type_say.lower():
                self.__lux = (self.__lux/Range_lux)*100
            if "s" in type_say.lower():
                return self.__lux
            else:
                return "light_S" "::" + str(self.__lux)   
        else:
            return False
    def __str__(self):
        return self.sey_value()
    def __int__(self):
        return self.__lux
    def __float__(self):
        return float(self.__lux)
    def __eq__(self, other):
        if type(other) != light_S:
            return None
        if self.__lux == other.sey_value("ns"):
            return True
        else:
            return False
    def __ne__(self,other):
        if type(other) != light_S:
            return None
        if self.__lux != other.sey_value("ns"):
            return True
        else:
            return False
    def __lt__(self, other):
        if type(other) != light_S:
            return None
        if self.__lux < other.sey_value("ns"):
            return True
        else:
            return False 
    def __gt__(self,other):
        if type(other) != light_S:
            return None
        if self.__lux > other.sey_value("ns"):
            return True
        else:
            return False
    def __le__(self,other):
        if type(other) != light_S:
            return None
        if self.__lux <= other.sey_value("ns"):
            return True
        else:
            return False 
    def __ge__(self,other):
        if type(other) != light_S:
            return None
        if self.__lux >= other.sey_value("ns"):
            return True
        else:
            return False 

class Sound_S(Sensor):
    """
    # سنسور صدا
    --------------
    ## متد ها
    
    get_value(): برای گرفتن حجم صدا\n
    sey_value(): برای نمایش مقدار حجم صدا \n
    ---
    ## ویژگی
    DB: حجم صدا\n
        (default: 0)
    """
    def __init__(self,name = "", code = "",DB = 00,location = "" ,*args ,**kwargs):
        super().__init__(name=name,code = code,location=location,*args,**kwargs)
        self.__DB = DB
        #self.cont = "Sound_S" "::" + str(self.__DB)
    def get_value(self,data):
        """
        data = اطلاعات
        """
        self.__DB = data
    def sey_value(self,type_say = "NT",Range_DB = 1):
        """
        type_say: نوع نمایش\n
            ("N" --> به صورت معمولی | "P" --> به صورت درصدی ) | ("S" --> به صورت عددی | "T" --> به صورت متنی)
        ** اگر نمایش به صورت درصدی است می توان رنج حجم صدا را تغییر دهید\n
        Range_DB: رنج حجم صدا\n
        
        """
        if not ("p" in type_say.lower() or "n" in type_say.lower()):
            raise ValueError("Choose type_say between (P)ercent and (N)ormal")
        if not self.__DB is None:
            if "p" in type_say.lower():
                self.__DB = (self.__DB/Range_DB)*100
            if "s" in type_say.lower():
                return self.__DB
            else:
                return "Sound_S" "::" + str(self.__DB)   
        else:
            return False
    def __str__(self):
        return self.sey_value()
    def __int__(self):
        return self.__DB
    def __float__(self):
        return float(self.__DB)
    def __eq__(self, other):
        if type(other) != Sound_S:
            return None
        if self.__DB == other.sey_value("ns"):
            return True
        else:
            return False
    def __ne__(self,other):
        if type(other) != Sound_S:
            return None
        if self.__DB != other.sey_value("ns"):
            return True
        else:
            return False
    def __lt__(self, other):
        if type(other) != Sound_S:
            return None
        if self.__DB < other.sey_value("ns"):
            return True
        else:
            return False 
    def __gt__(self,other):
        if type(other) != Sound_S:
            return None
        if self.__DB > other.sey_value("ns"):
            return True
        else:
            return False
    def __le__(self,other):
        if type(other) != Sound_S:
            return None
        if self.__DB <= other.sey_value("ns"):
            return True
        else:
            return False 
    def __ge__(self,other):
        if type(other) != Sound_S:
            return None
        if self.__DB >= other.sey_value("ns"):
            return True
        else:
            return False 
class Motion_S(Sensor):
    """
    # سنسور حرکت
    --------------
    ## متد ها

    get_value(): برای گرفتن مقدار \n
    sey_value(): برای نمایش مقدار \n
    ---
    ## ویژگی
    motion: جهت نمایش وجود یا عدم وجود حرکت
        \t(True--> حرکت|False-->عدم حرکت)
    """
    def __init__(self,name = "", code = "",motion = None,location = "" ,*args ,**kwargs):
        super().__init__(name=name,code = code,location=location,*args,**kwargs)
        self.__motion = bool(motion)

    def get_value(self,data):
        """
        data = اطلاعات
        """
        self.__motion = bool(data)
    def sey_value(self,type_say = "NT",Range_motion = 1):
        """
        type_say: نوع نمایش\n
            ("N" --> به صورت معمولی | "P" --> به صورت درصدی ) | ("S" --> به صورت عددی | "T" --> به صورت متنی)
        ** اگر نمایش به صورت درصدی است می توان رنج حجم صدا را تغییر دهید\n
        Range_motion: رنج حجم صدا\n
        
        """
        if not ("p" in type_say.lower() or "n" in type_say.lower()):
            raise ValueError("Choose type_say between (P)ercent and (N)ormal")
        if not self.__motion is None:
            if "p" in type_say.lower():
                self.__motion = (self.__motion/Range_motion)*100
            if "s" in type_say.lower():
                return self.__motion
            else:
                return "Motion_S" "::" + str(self.__motion)
        else:
            return False