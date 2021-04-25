from ..transform import InnerTransform

class Symbol(InnerTransform):
    def __init__(self,canvas, _id:str,x:float=0,y:float=0,width:float=0,height:float=0, refx:float=0,refy:float=0):
        super().__init__("symbol", canvas)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.refx = refx
        self.refy = refy
        self.viewbox = []
        self.ratio = ["xMidYMid","meet"]
        self.id = _id

    def set_viewBox(self,numbers:list):
        self.viewbox = numbers

    def viewBox_attribute(self,info:str):
        if self.viewbox:
            info += f""" viewBox="{" ".join(self.viewbox)}" """

        return info

    def set_ratio(self,key1:str,key2:str):
        self.ratio = [key1,key2]

    def ratio_attribute(self, info:str):
        if self.ratio != ["xMidYMid","meet"]:
            info += f""" preserveAspectRatio="{self.ratio[0]} {self.ratio[1]}" """

        return info

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
        if self.refx:
            info += f' refX="{self.refx}"'
        if self.refy:
            info += f' refY="{self.refy}"'

        info = self.viewBox_attribute(info)
        info = self.ratio_attribute(info)
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
        info = self.mask_attribute(info)
        info = self.cp_attribute(info)
        info = self.inner_attribute(info)
        return info