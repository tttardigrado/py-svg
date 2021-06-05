from .animation import Animation


class TranAnim(Animation):
    def __init__(self, canvas, _type: str = ""):
        super().__init__("animateTransform", canvas)
        self.attribute = "transform"
        self.type = _type

    def set_type(self, keyword: str):
        self.type = keyword

    def draw(self):
        info = f"<{self.tag}"
        info = self.values_attribute(info)
        info = self.timing_attribute(info)
        info = self.other_attributes(info)
        if self.type:
            info += f' type="{self.type}"'
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info += " />"
        return info
