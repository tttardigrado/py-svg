from ..transform import InnerTransform

class Gradient(InnerTransform):
    def __init__(self,tag:str,canvas):
        super().__init__(tag, canvas)
        self.href = None
        self.spreadMethod = "pad"
        self.gradientUnits = "objectBoundingBox"

    # set href
    def set_href(self,url:str):
        self.href = url
    
    # no href
    def no_href(self):
        self.href = None

    # set spread
    def set_spread(self, keyword:str):
        self.spreadMethod = keyword
    
    # set gUnits
    def set_gradientUnits(self,keyword:str):
        self.gradientUnits = keyword



    def spread_attribute(self, info:str):
        if self.spreadMethod != "pad":
            info += f""" spreadMethod="{self.spreadMethod}" """

        return info
    
    def gUnits_attribute(self, info:str):
        if self.gradientUnits != "objectBoundingBox":
            info += f""" gradientUnits="{self.gradientUnits}" """

        return info

    def href_attribute(self, info:str):
        if self.href:
            info += f""" href="{self.href}" """

        return info
    
    def gradient_attribute(self, info:str):
        info = self.transform_attribute(info)
        info = self.spread_attribute(info)
        info = self.gUnits_attribute(info)
        info = self.href_attribute(info)
        return info