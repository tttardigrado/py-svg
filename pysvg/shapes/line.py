from ..transform import InnerTransform

class Line(InnerTransform):

    def __init__(self,canvas, x1:float=0, y1:float=0, x2:float=0, y2:float=0):
        super().__init__("line", canvas)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.pathLength = None

    def set_path_length(self,length:float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag}"
        info += f" x1='{self.x1}'"
        info += f" y1='{self.y1}'"
        info += f" x2='{self.x2}'"
        info += f" y2='{self.y2}'"
        info += f" pathLength='{self.pathLength}'"
        
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.super_attribute(info)
        info += self.inner_attribute(info)
        return info

