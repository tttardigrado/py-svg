from typing import Any
class Stop:
    def __init__(self, offset:float=0, color:str="#000000", opacity:float=1):
        self.id = None
        self.classes = []
        self.style = {}
        self.offset = offset
        self.color = color
        self.opacity = opacity

    # id
    def set_id(self, new_id:str):
        self.id = new_id

    def id_attribute(self, info:str):
        if self.id:
            info += f""" id='{self.id}'"""
        return info

    # style

    def set_style(self, new_style:dict):
        self.style = new_style

    def add_style(self, style:str, value: Any):
        self.style[style] = value

    def rem_style(self, style:str):
        del self.style[style]

    def style_attribute(self, info:str):
        if self.style:
            s = """ style=" """
            for k, v in self.style:
                s += f"""{k}:{v};"""
            s += """ " """
            info += s
        return info


    # class
    def set_class(self, new_classes:str):
        self.classes = new_classes

    def add_class(self, new_class:str):
        self.classes.append(new_class)

    def rem_class(self, index:int):
        del self.classes[index]

    def class_attribute(self, info:str):
        if self.classes:
            info += f""" class='{" ".join(self.classes)}'"""
        return info

    def draw(self):
        info = "<stop"
        if self.offset:
            info += f" offset='{self.offset}'"
        if self.opacity != "1":
            info += f" stop-opacity='{self.opacity}'"
        info += f" stop-color='{self.color}'"
        

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info += " />"
        return info