class States:
    """    
    ## .این متد برای تغییر حالت اشیا مختلف(وسایل و سنسور ها) استفاده می شود
    ---
   ## متد ها:
   toggle(): برای تغییر دادن حالت\n
   ON(): برای روشن کردن\n
   OFF(): برای خاموش کردن\n
   ---
   ## ویژگی
   state: .حالت را نشان میدهد (default = False)
        (True --> روشن|False --> خاموش)
    """
    def __init__(self,state,*args,**kwargs):
        super().__init__(state=state,**kwargs)
        self.state = state
        if state is True:
            self.state = True
        elif state is False:
            self.state = False
        elif state.lower() == "on":
            self.state = True
        elif state.lower() == "off" :
            self.state = False
        else:
            raise ValueError("state can't be {}".format(state))
    def toggle(self):
        if self.state is False:
            self.state = True
        elif self.state is True:
            self.state = False
    
    def ON(self):
        self.state = True
        
    def OFF(self):
        self.state = False
class Rotate:
    """    
    ## .این متد برای تغییر زاویه اشیا موتور دار(وسایل و سنسور ها) استفاده می شود
    ---
   ## متد ها:
   Rotation(int): .برای تغییر زاویه می باشد که میتوانید به دو صورت وارد کنید\n
   Angle_converter(): .برای تغییر مقیاس زاویه به کار می رود\n
   ---
   ## ویژگی ها
   angle_scale: مقیاس زاویه (default = "D")
        ("D" --> درجه|"R" --> رادیان)
   initial_value: مقدار اولیه (default = 0) 
    """    
    def __init__(self,initial_value = 0,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.angle_scale = "D"
        self.initial_value = initial_value
        self.second_position = initial_value
    def Rotation(self,R_value = None,Second_Position=None):
        if Second_Position is None:
            if type(R_value) is int:
                self.second_position = self.second_position + R_value
            elif type(R_value) is str:
                s = R_value[:(len(R_value)-1)]    
                s = round(s,2)
                if R_value[(len(R_value)-1)].lower() == "d":
                    self.second_position = self.second_position + s
                elif R_value[(len(R_value)-1)].lower() == "r":
                    s = s*180/3.14
                    self.second_position = self.second_position + s
                    self.angle_scale == "D"
        else:
            if type(Second_Position) is int:
                self.second_position = Second_Position

            elif type(Second_Position) is str:
                if Second_Position[:(len(Second_Position)-1)].lower() == "3.14":
                        s = 3.14
                else:
                    s = round(float(Second_Position[:(len(Second_Position)-1)]),2)
                if Second_Position[(len(Second_Position)-1)].lower() == "d":
                    self.second_position =  s
                elif Second_Position[(len(Second_Position)-1)].lower() == "r":
                    s = s*180/3.14
                    self.second_position =  s
                    self.angle_scale == "D"
    def Angle_converter(self):
        if self.angle_scale == "D":
            self.second_position = self.second_position*3.14/180
            self.angle_scale = "R"
        elif self.angle_scale == "R":
            self.second_position = self.second_position*180/3.14
            self.angle_scale = "D"
