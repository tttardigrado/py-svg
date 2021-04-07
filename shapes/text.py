from .inner import InnerShape

class Text(InnerShape):
    def __init__(self,canvas,text="", x=0, y=0, dx=0, dy=0):
        super().__init__("text", canvas)
        self.inner += text
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotate = []
        self.adjust = "spacing"
        self.length = 0

    def set_text(self,text):
        self.inner = text

    def set_adjust(self, adjust):
        self.adjust = adjust
    
    def set_length(self,length):
        self.length = length

    def set_rotate(self,rotate):
        self.rotate = rotate

    def add_rotate(self, number):
        self.rotate.append(number)
    
    def rem_rotate(self, index):
        del self.rotate[index]

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" dx='{self.dx}'"
        info += f" dy='{self.dy}'"

        if self.rotate:
            info += f""" rotate='{" ".join(self.rotate)}' """

        if self.length:
            info += f""" textLength='{self.length}'' """
        
        info += f""" lengthAdjust='{self.adjust}' """

        self.inner = [self.text]

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info

class TSpan(Text):
    def __init__(self, canvas, text='', x=0, y=0, dx=0, dy=0):
        super().__init__(canvas, text=text, x=x, y=y, dx=dx, dy=dy)
        self.tag = "tspan"