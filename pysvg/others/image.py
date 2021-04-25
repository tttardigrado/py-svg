from ..transform import InnerTransform

class Image(InnerTransform):
    def __init__(self, canvas, href:str, x:float=0,y:float=0,width:float=0,height:float=0):
        super().__init__("image", canvas)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.href = href
        self.ratio = ["xMidYMid","meet"]

    def set_ratio(self,key1:str,key2:str):
        self.ratio = [key1,key2]

    def ratio_attribute(self, info:str):
        if self.ratio != ["xMidYMid","meet"]:
            info += f""" preserveAspectRatio="{self.ratio[0]} {self.ratio[1]}" """

        return info

    def draw(self):
        info = f"<{self.tag} "
        info += f' x="{self.x}"'
        info += f' y="{self.y}"'
        info += f' width="{self.width}"'
        info += f' height="{self.height}"'
        info += f' href="{self.href}"'

        info = self.ratio_attribute(info)
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.opacity_attribute(info)
        info = self.mask_attribute(info)
        info = self.cp_attribute(info)
        info = self.inner_attribute(info)
        return info

    