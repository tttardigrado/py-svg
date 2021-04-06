class Shape:
    def __init__(self, tag, canvas):
        self.canvas = canvas
        self.tag = tag
        self.inner = []
        self.id = None
        self.classes = []
        self.style = {}

    def super_attribute(self,info):
        info += f""" fill="{self.canvas.fi}" stroke="{self.canvas.st}" """
        if self.canvas.fiO != 1:
            info += f""" fill-opacity="{self.canvas.fiO}" """
        if self.canvas.stO != 1:
            info += f""" stroke-opacity="{self.canvas.stO}" """
        if self.canvas.stW != 1:
            info += f""" stroke-weight="{self.canvas.stW}" """
        return info

    # id
    def set_id(self, new_id):
        self.id = new_id

    def id_attribute(self, info):
        if self.id:
            info += f""" id='{self.id}'"""
        return info

    # style

    def set_style(self, new_style):
        self.style = new_style

    def add_style(self, style, value):
        self.style[style] = value

    def rem_style(self, style):
        del self.style[style]

    def style_attribute(self, info):
        if self.style:
            s = """ style=" """
            for k, v in self.style:
                s += f"""{k}:{v};"""
            s += """ " """
            info += s
        return info


    # class
    def set_class(self, new_classes):
        self.classes = new_classes

    def add_class(self, new_class):
        self.classes.append(new_class)

    def rem_class(self, rem_class):
        self.classes.remove(rem_class)

    def class_attribute(self, info):
        if self.classes:
            info += f""" class='{" ".join(self.classes)}'"""
        return info

    # inner
    def set_inner(self, new_inner):
        self.inner = new_inner

    def add_inner(self, new_inner):
        self.inner.append(new_inner)

    def rem_inner(self, rem_inner):
        self.inner.remove(rem_inner)

    def inner_attribute(self, info):
        if self.inner:
            info += f""">{" ".join(self.inner)}</{self.tag}>'"""
        else:
            info += "/>"
        return info


class Circle(Shape):

    def __init__(self,canvas, x=0, y=0, r=0):
        super().__init__("circle", canvas)
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.x}'"
        info += f" cy='{self.y}'"
        info += f" r='{self.r}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info


class Ellipse(Shape):

    def __init__(self,canvas, x=0, y=0, rx=0, ry=0):
        super().__init__("ellipse", canvas)
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry

    def draw(self):
        info = f"<{self.tag}"
        info += f" cx='{self.x}'"
        info += f" cy='{self.y}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info


class Rect(Shape):

    def __init__(self,canvas, x=0, y=0, w=0, h=0, rx=0, ry=0):
        super().__init__("rect", canvas)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rx = rx
        self.ry = ry

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" w='{self.w}'"
        info += f" h='{self.h}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info


class Square(Rect):

    def __init__(self,canvas, x=0, y=0, s=0, rx=0, ry=0):
        super().__init__(canvas ,x, y, s, s, rx, ry)

    def draw(self):
        info = f"<{self.tag}"
        info += f" x='{self.x}'"
        info += f" y='{self.y}'"
        info += f" w='{self.w}'"
        info += f" h='{self.h}'"
        info += f" rx='{self.rx}'"
        info += f" ry='{self.ry}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info


class Line(Shape):

    def __init__(self,canvas, x1=0, y1=0, x2=0, y2=0):
        super().__init__("line", canvas)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        info = f"<{self.tag}"
        info += f" x1='{self.x1}'"
        info += f" y1='{self.y1}'"
        info += f" x2='{self.x2}'"
        info += f" y2='{self.y2}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info


