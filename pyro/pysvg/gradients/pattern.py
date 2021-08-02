from ..transform import InnerTransform

class Pattern(InnerTransform):
    def __init__(self,canvas, href:str="", x:float=0,y:float=0, width:float=0,height:float=0):
        super().__init__("pattern", canvas)
        self.href = href
        self.patternUnits = "objectBoundingBox"
        self.pcUnits = "objectBoundingBox"
        self.ratio = ["xMidYMid","meet"]
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    # set ratio
    def set_ratio(self,key1:str,key2:str):
        self.ratio = [key1,key2]


    # set href
    def set_href(self,url:str):
        self.href = url
    
    # no href
    def no_href(self):
        self.href = None

    # set spread
    def set_patternUnits(self, keyword:str):
        self.patternUnits = keyword
    
    # set gUnits
    def set_pcUnits(self,keyword:str):
        self.pcUnits = keyword


    
    def patternUnits_attribute(self, info:str):
        if self.patternUnits != "objectBoundingBox":
            info += f""" spreadMethod="{self.patternUnits}" """

        return info
    
    def gUnits_attribute(self, info:str):
        if self.gradientUnits != "objectBoundingBox":
            info += f""" gradientUnits="{self.gradientUnits}" """

        return info

    def href_attribute(self, info:str):
        if self.href:
            info += f""" href="{self.href}" """

        return info
    
    def ratio_attribute(self, info:str):
        if self.ratio != ["xMidYMid","meet"]:
            info += f""" href="{self.ratio[0]} {self.ratio[1]}" """

        return info
    
    def various_attribute(self, info:str):
        info = self.transform_attribute(info)
        info = self.spread_attribute(info)
        info = self.gUnits_attribute(info)
        info = self.ratio_attribute(info)
        info = self.href_attribute(info)
        return info

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" width='{self.width}'"
        info += f" height='{self.height}'"
        
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.fill_attribute(info)
        info = self.stroke_attribute(info)
        info = self.linecap_attribute(info)
        info = self.linejoin_attribute(info)
        info = self.dash_attribute(info)
        info = self.various_attribute(info)
        info = self.opacity_attribute(info)
        info = self.mask_attribute(info)
        info = self.cp_attribute(info)
        info = self.inner_attribute(info)
        return info