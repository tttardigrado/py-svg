from ..transform import InnerTransform
class Mask(InnerTransform):
    def __init__(self,canvas,_id:str,x:float=0,y:float=0,width:float=0,height:float=0):
        super().__init__("mask", canvas)
        self.id = _id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.contentUnits = "userSpaceOnUse"
        self.maskUnits = "objectBoundingBox"


    def set_contentUnits(self,keyword:str):
        self.contentUnits = keyword
    
    def set_maskUnits(self,keyword:str):
        self.maskUnits = keyword



    def d(self, shape):
        s = shape.draw()
        self.inner.append(s)

    
    
    def draw(self):
        info = f"<{self.tag} "
        if self.x:
            info += f' x="{self.x}"'
        if self.y:
            info += f' y="{self.y}"'
        if self.width:
            info += f' width="{self.width}"'
        if self.height:
            info += f' height="{self.height}"'
        if self.maskUnits != "objectBoundingBox":
            info += f' maskUnits="{self.maskUnits}"'
        if self.contentUnits != "userSpaceOnUse":
            info += f' maskContentUnits="{self.contentUnits}"'

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.fill_attribute(info)
        info = self.stroke_attribute(info)
        info = self.linecap_attribute(info)
        info = self.linejoin_attribute(info)
        info = self.dash_attribute(info)
        info = self.opacity_attribute(info)
        info = self.inner_attribute(info)
        return info