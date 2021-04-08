from typing import Any

class SVG:
    """Base SVG class"""

    def __init__(self, tag:str, canvas):
        self.canvas = canvas
        self.tag = tag
        self.id = None
        self.classes = []
        self.style = {}

    def super_attribute(self,info:str):
        info += f""" fill="{self.canvas.fi}" stroke="{self.canvas.st}" """
        if self.canvas.fiO != 1:
            info += f""" fill-opacity="{self.canvas.fiO}" """
        if self.canvas.stO != 1:
            info += f""" stroke-opacity="{self.canvas.stO}" """
        if self.canvas.stW != 1:
            info += f""" stroke-weight="{self.canvas.stW}" """
        return info

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
    def set_class(self, new_classes:list):
        self.classes = new_classes

    def add_class(self, new_class:str):
        self.classes.append(new_class)

    def rem_class(self, index:int):
        del self.classes[index]

    def class_attribute(self, info:str):
        if self.classes:
            info += f""" class='{" ".join(self.classes)}'"""
        return info
