from ..transform import InnerTransform
class ClipPath(InnerTransform):
    def __init__(self,canvas, _id:str):
        super().__init__("clipPath", canvas)
        self.units = "userSpaceOnUse"
        self.id = _id

    def d(self, shape):
        s = shape.draw()
        self.inner.append(s)

    def set_units(self,keyword:str):
        self.units = keyword
    
    def draw(self):
        info = f"<{self.tag} "

        if self.units != "userSpaceOnUse":
            info += f' clipPathUnits="{self.units}"'

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
        info = self.inner_attribute(info)
        return info