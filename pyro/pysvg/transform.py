from .inner import InnerShape


class InnerTransform(InnerShape):
    def __init__(self, tag, canvas):
        super().__init__(tag, canvas)
        self.transform = []

    def no_transform(self):
        self.transform = []

    def rem_transform(self, index: int):
        del self.transform[index]

    def add_matrix(self, a: float = 0, b: float = 0, c: float = 0, d: float = 0, e: float = 0, f: float = 0):
        self.transform.append(["matrix", [a, b, c, d, e, f]])

    def add_translate(self, x: float = 0, y: float = 0):
        self.transform.append(["translate", [x, y]])

    def add_scale(self, x: float = 0, y: float = 0):
        self.transform.append(["scale", [x, y]])

    def add_rotate(self, a: float = 0, x: float = 0, y: float = 0):
        self.transform.append(["rotate", [a, x, y]])

    def add_skew_x(self, a: float = 0):
        self.transform.append(["skewX", [a]])

    def add_skew_y(self, a: float = 0):
        self.transform.append(["skewY", [a]])

    def transform_attribute(self, info: str):
        if self.transform:
            info += """ gradientTransform=" """
            for element in self.transform:
                info += f"""{element[0]}({",".join(element[1])})"""
            info += """ " """

        return info
