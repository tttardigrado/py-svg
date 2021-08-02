from ..transform import InnerTransform


class G(InnerTransform):
    def __init__(self, canvas, _id: str):
        super().__init__("g", canvas)
        self.id = _id

    def draw(self):
        info = f"<{self.tag} "

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

