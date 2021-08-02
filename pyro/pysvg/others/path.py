from ..transform import InnerTransform


class Path(InnerTransform):
    def __init__(self, canvas, d: str = ""):
        super().__init__("path", canvas)
        self.d = d
        self.pathLength = None

    def set_d(self, d: str):
        self.d = d

    def d_move(self, x: float, y: float, relative: bool = False):
        if relative:
            self.d += f" m {x},{y}"
        else:
            self.d += f" M {x},{y}"

    def d_line(self, x: float, y: float, relative: bool = False):
        if relative:
            self.d += f" l {x},{y}"
        else:
            self.d += f" L {x},{y}"

    def d_horizontal(self, x: float, relative: bool = False):
        if relative:
            self.d += f" h {x}"
        else:
            self.d += f" H {x}"

    def d_vertical(self, y: float, relative: bool = False):
        if relative:
            self.d += f" v {y}"
        else:
            self.d += f" V {y}"

    def d_curve(self, handle1X: float, handle1Y: float, handle2X: float, handle2Y: float, finalX: float, finalY: float, relative: bool = False):
        if relative:
            self.d += f" c {handle1X},{handle1Y} {handle2X},{handle2Y} {finalX},{finalY}"
        else:
            self.d += f" C {handle1X},{handle1Y} {handle2X},{handle2Y} {finalX},{finalY}"

    def d_curve2(self, handleX: float, handleY: float, finalX: float, finalY: float, relative: bool = False):
        if relative:
            self.d += f" s {handleX},{handleY} {finalX},{finalY}"
        else:
            self.d += f" S {handleX},{handleY} {finalX},{finalY}"

    def d_quadratic(self, ctrlX: float, ctrlY: float, finalX: float, finalY: float, relative: bool = False):
        if relative:
            self.d += f" q {ctrlX},{ctrlY} {finalX},{finalY}"
        else:
            self.d += f" Q {ctrlX},{ctrlY} {finalX},{finalY}"

    def d_quadratic2(self, finalX: float, finalY: float, relative: bool = False):
        if relative:
            self.d += f" t {finalX},{finalY}"
        else:
            self.d += f" T {finalX},{finalY}"

    def d_arc(self, rotationX: float, rotationY: float, arc: bool, sweep: bool, finalX: float, finalY: float, relative: bool = False):
        if relative:
            self.d += f" a {rotationX},{rotationY} {int(arc)},{int(sweep)} {finalX},{finalY}"
        else:
            self.d += f" A {rotationX},{rotationY} {int(arc)},{int(sweep)} {finalX},{finalY}"

    def d_end(self):
        self.d += " Z"

    def set_path_length(self, length: float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag} "
        info = f""" d="{self.d}" """
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
        info = self.marker_attribute(info)
        info = self.inner_attribute(info)
        return info

