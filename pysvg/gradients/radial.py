from .gradient import Gradient

class RadialGradient(Gradient):
    def __init__(self,canvas,id_:str ,cx:float=0,cy:float=0,r:float=0, fx:float=0,fy:float=0,fr:float=0):
        super().__init__("radialGradient", canvas)
        self.cx = cx
        self.cy = cy
        self.r = r
        self.fx = fx
        self.fy = fy
        self.fr = fr
        self.id = id_

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.cx}'"
        info += f" cy='{self.cy}'"
        info += f" r='{self.r}'"
        if self.fx:
            info+=f" fx='{self.fx}'"
        if self.fy:
            info+=f" fy='{self.fy}'"
        if self.fx:
            info+=f" fr='{self.fr}'"
        
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.gradient_attribute(info)
        info = self.inner_attribute(info)
        return info