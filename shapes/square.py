from .rect import Rect

class Square(Rect):

    def __init__(self,canvas, x=0, y=0, s=0, rx=0, ry=0):
        super().__init__(canvas ,x, y, s, s, rx, ry)
    

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" width='{self.w}'"
        info += f" height='{self.h}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"
        info += f" pathLength='{self.pathLength}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info