from Smart_Home.Subject import Subject
from Smart_Home.Class.Furniture import Lamp,Lamps
#from Smart_Home.main import *
from Smart_Home.Class.Attributes import Sound,Picture,light
from Smart_Home.Class.Methods import States
from Smart_Home.Checker import default_location
from Smart_Home.Question import Quest




class Verb:
    def __init__(self,verb=None ,object = None ,place = None,Start_Time = None,End_Time = None,To = None):
        try:
            self.object=object
        except:
            self.object = Quest("sub",verb)
        try:
            self.place=place
        except:
            self.place = Quest("place",verb)
        self.verb=verb
        #print(self.verb)
        if self.verb =="روشن کردن":
            Turn("ON",self.object,self.place)
        elif self.verb == "خاموش کردن":
            Turn("OFF",self.object,self.place)
        elif self.verb =="نوشتن":   
            Write(self.object)
        elif self.verb in ["پخش کردن","پلی کردن"]:   
            Play(object = self.object)
        elif self.verb in ["استاپ کردن",'ایست کردن'] :   
            Stop(object = self.object)
        elif self.verb == "اضافه کردن":
            Add("add to lamps",object,place)

class Save:
    pass                


class Calculate:
    pass


class Translate:
    pass


class Write:
    def __init__(self,object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                print(sub)
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue


class Read:
    pass


class Turn:
    def __init__(self,state="ON",object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                if state == "ON":
                    States.ON(sub)
                elif state == "OFF":
                    States.OFF(sub)
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue
    

class Send:
    def __init__(self,object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                States.OFF(sub)
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue


class Play:
      def __init__(self,subject="music",object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                if subject == "music":
                    Sound.sound_control(sub,key="p")
                elif subject == "film":
                    Sound.sound_control(sub,key="p")
                    Picture.pic_control(sub,key="p")
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue


class Stop:
    def __init__(self,subject="music",object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                if subject == "music":
                    Sound.sound_control(sub,key="s")
                elif subject == "film":
                    Sound.sound_control(sub,key="s")
                    Picture.pic_control(sub,key="s")
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue


class Call:
    pass


class Set:
    pass


class Add:
    def __init__(self,subject=None,object = None ,place = None,Start_Time = None):
        list_sub=Subject(object)
        for sub in list_sub: 
            try:
                if type(sub) == Lamp:
                    #code = code_finder()
                    for i in default_location[place]:
                        if type(i) == Lamps:
                            strlamp = i
                            del i
                            break
                    strlamp =  strlamp + object
                pass
            except:
                print(str(type(sub)) + " can't do that.")
                continue
    


#Verb("اضافه کردن",object = lamp3, place="Room")



