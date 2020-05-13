from Smart_Home.Class.Furniture import Lamp,Door,Screen,Speaker,Lamps
#from .Object import Object
from Smart_Home.Checker import Check#,names,codes
#from .Attributes import States
#from .Methods import light,Sound
#from .Subject import Subject





###Classes
lamp = Lamp("لامپ",code="#001",location = "Room",RGB="#123456",brightness=23,state=False)
lamp2 = Lamp("لامپ2",code="#002",location = "Table",brightness=17)
lamp3 = Lamp("3لامپ",code="#005",location = "Table",brightness=12)
dar = Door(name = "در",code = "#003",location = "Room")
speaker = Speaker(name="بلندگو",code = "#004",state=False,location="Room",sound_value = 50)

###
####چک
#Check()
###
####ترکیبیات
lampha = lamp+lamp2
#lampha += lamp3
lampha.code = "#010"
Check()

###
"""
####انتخاب موارد

list_sub=Subject("All",Lamps,Lamp)

###
for sub in list_sub: 
    try:
        ####
                        # فعل مورد نظر خود را در این قسمت وارد کنید.
        #light.RGB_Changer(sub,Choose = "rgb",IDF = "Inc",ValIDF = 100)#مثال
        #Sound.sound_speed_changer(sub,speed = False)
        States.ON(sub)

        ####
        pass
    except:
        print(str(type(sub)) + " can't do that.")
        continue

#print(speaker.sound_speed)


####انتخاب موارد
list_sub=Subject("All",None)
###
for sub in list_sub: 
    try:
        #### فعل مورد نظر خود را در این قسمت وارد کنید.
        #States.ON(sub)

        ####
        pass
    except:
        print(str(type(sub)) + " can't do that.")
        continue
#print(lamp.state)
"""
