from typing import Any

class SVG:
    """Base SVG class"""

    def __init__(self, tag:str, canvas):
        self.canvas = canvas
        self.tag = tag
        self.id = None
        self.classes = []
        self.style = {}

    def mask_attribute(self, info:str):
        if self.canvas.ma:
            info += f""" mask="{self.canvas.ma}" """
        return info

    def cp_attribute(self, info:str):
        if self.canvas.clipRule:
            info += f""" clip-rule="{self.canvas.clipRule}" """
        if self.canvas.cp:
            info += f""" clip-path="{self.canvas.cp}" """
        return info

    def fill_attribute(self,info:str):
        if self.canvas.fillRule != "nonzero":
            info += f""" fill-rule="{self.canvas.fillRule}" """
        if self.canvas.fi != "#000000":
            info += f""" fill="{self.canvas.fi}" """
        if self.canvas.fiO != 1:
            info += f""" fill-opacity="{self.canvas.fiO}" """
        return info

    def opacity_attribute(self,info:str):
        if self.canvas.o != 1:
            info += f""" opacity="{self.canvas.o}" """
        return info
    
    def stroke_attribute(self,info:str):
        if self.canvas.st != "#000000":
            info += f""" stroke="{self.canvas.st}" """
        if self.canvas.stO != 1:
            info += f""" stroke-opacity="{self.canvas.stO}" """
        if self.canvas.stW != 1:
            info += f""" stroke-weight="{self.canvas.stW}" """
        return info
    
    def linejoin_attribute(self,info:str):
        if self.canvas.stLineJoin!="miter":
            info += f""" stroke-linejoin="{self.canvas.stLineJoin}" """
        return info
    def linecap_attribute(self,info:str):
        if self.canvas.stLineCap!="butt":
            info += f""" stroke-linecap="{self.canvas.stLineCap}" """
        return info
    def dash_attribute(self,info:str):
        if self.canvas.stA:
            info += f""" stroke-dasharray="{''.join(self.canvas.stA)}" """
        if self.canvas.stOffset:
            info += f""" stroke-dashoffset="{self.canvas.stOffset}" """        
        return info
    

    def marker_attribute(self,info:str):
        if self.canvas.mk:
            info += f""" marker-start="{self.canvas.mk}" marker-mid="{self.canvas.mk}" marker-end="{self.canvas.mk}" """    
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

    
