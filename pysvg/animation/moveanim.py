from .animation import Animation


class MotionAnim(Animation):
    def __init__(self, canvas, d: str = ""):
        super().__init__("animateMotion", canvas)
        self.rotate = 0
        self.d = d

    def set_rotate(self, value: str or float):
        self.rotate = value

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

    def draw(self):
        info = f"<{self.tag}"
        if self.rotate:
            info += f' rotate="{self.rotate}"'
        if self.d:
            info += f' path="{self.d}"'
        info = self.values_attribute(info)
        info = self.timing_attribute(info)
        info = self.other_attributes(info)
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info += " />"
        return info
