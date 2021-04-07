from .inner import InnerShape

class Ellipse(InnerShape):

    def __init__(self,canvas, x=0, y=0, rx=0, ry=0):
        super().__init__("ellipse", canvas)
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.pathLength = None

    def set_path_length(self,length):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.x}'"
        info += f" cy='{self.y}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"
        info += f" pathLength='{self.pathLength}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info