from .shapes import Shape

class Line(Shape):

    def __init__(self,canvas, x1=0, y1=0, x2=0, y2=0):
        super().__init__("line", canvas)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.pathLength = None

    def set_path_length(self,length):
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
        info = self.super_attribute(info)
        info += "/>"
        return info

