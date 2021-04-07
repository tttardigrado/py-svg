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
