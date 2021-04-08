from ..inner import InnerShape

class Text(InnerShape):
    def __init__(self,canvas,text:str="", x:float=0, y:float=0, dx:float=0, dy:float=0):
        super().__init__("text", canvas)
        self.inner += text
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rotate = []
        self.adjust = "spacing"
        self.length = 0

    def set_text(self,text:str):
        self.inner = text

    def set_adjust(self, adjust:str):
        self.adjust = adjust
    
    def set_length(self,length:float):
        self.length = length

    def set_rotate(self,rotate:list):
        self.rotate = rotate

    def add_rotate(self, number:float):
        self.rotate.append(number)
    
    def rem_rotate(self, index:int):
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
    def __init__(self, canvas, text:str='', x:float=0, y:float=0, dx:float=0, dy:float=0):
        super().__init__(canvas, text=text, x=x, y=y, dx=dx, dy=dy)
        self.tag = "tspan"

class TextPath:
    """https://developer.mozilla.org/en-US/docs/Web/SVG/Element/textPath"""
    pass