from ..transform import InnerTransform

class Ellipse(InnerTransform):

    def __init__(self,canvas, x:float=0, y:float=0, rx:float=0, ry:float=0):
        super().__init__("ellipse", canvas)
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.pathLength = None

    def set_path_length(self,length:float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.x}'"
        info += f" cy='{self.y}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"
        if self.pathLength:
            info += f" pathLength='{self.pathLength}'"

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