from Smart_Home.Class.Code import hexe,is_hex,inttohex,hextoint


class light:
    """
    #  .یک ویژگی است که به اجسام نوردار داده می شود light
    ---
    ## متد 

    RGB_Changer: برای تغییر رنگ (defaults:(Choose = "rgb",IDF = "Fix",ValIDF = 00)) \n
    ---
    ## ویژگی ها

    brightness: میزان شدت نور\n
    RGB: رنگ نور\n
    R: قرمزی نور\n
    G: سبزی نور\n
    B: آبی نور\n
    """
    def __init__(self,RGB="#000000",brightness = 00,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if not type(RGB) is str:
            raise ValueError("RGB value must be string.")
        if not is_hex(RGB):
            raise ValueError("write a hex for RGB!(hex start with \"#\")")
        self.brightness = brightness
        self.RGB = RGB
        self.Red =  hexe(self.RGB[1:3])
        self.Green =  hexe(self.RGB[3:5])
        self.Blue = hexe(self.RGB[5:7])

    def RGB_Changer(self,Choose = "rgb",IDF = "Fix",ValIDF = 00):
        valueidf = 0
        r = 1
        #rogob = [] 
        if IDF == "Fix":
            valueidf = 0
        elif IDF == "Inc":
            valueidf = ValIDF
        elif IDF == "Dec":
            valueidf = -ValIDF
        elif IDF == "Rev":
            r = -1
        else:
            raise ValueError("IDF is Incorrect.")
        if "r" in Choose.lower():
            self.Red = inttohex(r*hextoint(self.Red) + valueidf)
        if "g" in Choose.lower():
            self.Green = inttohex(r*hextoint(self.Green) + valueidf)
        if "b" in Choose.lower():
            self.Blue = inttohex(r*hextoint(self.Blue) + valueidf)


class Sound:
    """
    # .یک ویژگی است که به اجسام صدادار داده می شود Sound
    ---
    ## متد ها

    sound_control(): برای استاپ/پلی کردن صدا یا کمو زیادکردن صدا یا میوت کردن صدا \n
    sound_looper(): برای مد حلقه صدا\n
    sound_speed_changer(): برای تغییر سرعت صدا \n
        \t(True-->افزایش سرعت|False-->کاهش سرعت)\n
    ---
    ## ویژگی ها

    sound_value: حجم صدا\n
    State_sound: حالت پخش صدا\n
        \t("play","stop")(default: "play")\n
    sound_Loop: مد حلقه صدا می باشد\n
        \t("nor": بدون تکرار|"ol": تکرار تکی|"al":تکرار همه)
    sound_speed: سرعت صدا به صورت عددی با یک رقم اعشار
    """
    def __init__(self,sound_value = 00,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.sound_value = sound_value
        self.State_sound = "play"
        self.sound_Loop = "no_repeat"        
        self.sound_speed = 1.0

    def sound_control(self,value=0,key = "+"):
        options_c = {"+":self.sound_value + value,"-":self.sound_value - value,"m":0}
        options_s = {"p":"play","s":"stop"}
        if key.lower() in options_s.keys():
            self.State_sound = options_s[key.lower()]
        elif key.lower() in options_c.keys():
            self.sound_value = options_c[key.lower()]
            if self.sound_value >100:
                self.sound_value = 100
            elif self.sound_value <0:
                self.sound_value = 0
        else:
            raise ValueError("Key is wrong!")

    def sound_looper(self,key_loop="nor"):
        """
        "nor": "no_repeat"\n
        "ol": "one_repeat"\n
        "al":"All_repeat"
        """
        options = {"nor": "no_repeat","ol": "one_repeat","al":"All_repeat"}
        if key_loop.lower() in options.keys():
            self.sound_Loop = options[key_loop.lower()]  
        else:
            raise ValueError("key_loop is Incorrect(\"nor\": \"no_repeat\",\"ol\": \"one_repeat\",\"al\":\"All_repeat\")") 

    def sound_speed_changer(self,speed = None):
        if speed is None:
            return self.sound_speed
        elif speed:
            self.sound_speed += 0.1
        elif not speed:
            self.sound_speed -= 0.1
        return (self.sound_speed)

    def __int__(self):
        return int(self.sound_value)

    def __str__(self):
        return str(self.sound_value) 

    #Logical
    def __lt__(self, other):
        return (other) > self.sound_value

    def __gt__(self, other):
        return (other) < self.sound_value

    def __le__(self, other):
        return (other) >= self.sound_value

    def __ge__(self, other):
        return (other) <= self.sound_value

    def __eq__(self, other):
        return (other) == self.sound_value

    def __ne__(self, other):
        return (other) != self.sound_value  
   # def __setattr__(self,name,value):
      #  self.__dict__[name] = value
    #    if name == "sound_speed":
   #         if not type(value) is str or not value[0] == "X":
    #            raise ValueError("sound_speed start with \"X\" and it's a string.")


class Picture:
    """
    # .یک ویژگی است که به اجسام تصویردار داده می شود Picture
    ---
    ## متد ها

    pic_control(): برای استاپ/پلی کردن تصویر یا کم و زیاد کردن نور صفحه \n
    pic_looper(): برای مد حلقه تصویر\n
    pic_speed_changer(): برای تغییر سرعت تصویر \n
        \t(True-->افزایش سرعت|False-->کاهش سرعت)\n
    ---
    ## ویژگی ها

    pic_brightness: شدت نور تصویر\n
    State_pic: حالت پخش تصویر\n
        \t("play","stop")(default: "play")\n
    pic_Loop: مد حلقه تصویر می باشد\n
        \t("nor": بدون تکرار|"ol": تکرار تکی|"al":تکرار همه)
    pic_speed: سرعت تصویر به صورت عددی با یک رقم اعشار
    """
    def __init__(self,pic_brightness = 00,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.pic_brightness = pic_brightness
        self.State_pic = "play"
        self.pic_Loop = "no_repeat"        
        self.pic_speed = 1.0
        
    def pic_control(self,value=0,key = "+"):
        options_c = {"+":self.pic_brightness + value,"-":self.pic_brightness - value,"m":0}
        options_s = {"p":"play","s":"stop"}
        if key.lower() in options_s.keys():
            self.State_pic = options_s[key.lower()]
        elif key.lower() in options_c.keys():
            self.pic_brightness = options_c[key.lower()]
            if self.pic_brightness >100:
                self.pic_brightness = 100
            elif self.pic_brightness <0:
                self.pic_brightness = 0

    def pic_looper(self,key_loop="nor"):
        """
        "nor": "no_repeat"\n
        "ol": "one_repeat"\n
        "al":"All_repeat"
        """
        options = {"nor": "no_repeat","ol": "one_repeat","al":"All_repeat"}
        if key_loop.lower() in options.keys():
            self.pic_Loop = options[key_loop.lower()]  
        else:
            raise ValueError("key_loop is Incorrect(\"nor\": \"no_repeat\",\"ol\": \"one_repeat\",\"al\":\"All_repeat\")")    

    def pic_speed_changer(self,speed = None):
        if speed is None:
            return self.pic_speed
        elif speed:
           self.pic_speed += 0.1
        elif not speed:
            self.pic_speed -= 0.1
        return self.pic_speed
   
        
class Vibre:
    pass

