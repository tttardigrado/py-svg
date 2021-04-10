from ..transform import InnerTransform

class Circle(InnerTransform):

    def __init__(self,canvas, x:float=0, y:float=0, r:float=0):
        super().__init__("circle", canvas)
        self.x = x
        self.y = y
        self.r = r
        self.pathLength = None

    def set_path_length(self,length:float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.x}'"
        info += f" cy='{self.y}'"
        info += f" r='{self.r}'"
        if self.pathLength:
            info += f" pathLength='{self.pathLength}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info

