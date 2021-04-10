from ..transform import InnerTransform

class Use(InnerTransform):
    def __init__(self,canvas,href:str, x:float=0,y:float=0,width:float=0,height:float=0):
        super().__init__("use", canvas)
        self.href = href
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
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
        
        info += f' href="{self.href}"'

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info
