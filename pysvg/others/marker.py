from ..transform import InnerTransform
class Marker(InnerTransform):
    def __init__(self,canvas, _id:str, height:float=3, width:float=3):
        super().__init__("marker", canvas)
        self.units = "strokeWidth"
        self.id = _id
        self.height = height
        self.width = width
        self.orient = 0
        self.ratio = ["xMidYMid","meet"]
        self.x = ""
        self.y = ""
        self.viewbox = []

    
    def set_refX(self, keyword:str):
        self.x = keyword

    def set_refY(self, keyword:str):
        self.y = keyword

    def set_viewBox(self,numbers:list):
        self.viewbox = numbers

    def viewBox_attribute(self,info:str):
        if self.viewbox:
            info += f""" viewBox="{" ".join(self.viewbox)}" """

        return info

    def d(self, shape):
        s = shape.draw()
        self.inner.append(s)

    def set_units(self,keyword:str):
        self.units = keyword

    def set_orient(self,angle:float):
        self.orient = angle

    def set_ratio(self,key1:str,key2:str):
        self.ratio = [key1,key2]

    def ratio_attribute(self, info:str):
        if self.ratio != ["xMidYMid","meet"]:
            info += f""" preserveAspectRatio="{self.ratio[0]} {self.ratio[1]}" """

        return info
    
    def draw(self):
        info = f"<{self.tag} "

        if self.units != "strokeWidth":
            info += f' markerUnits="{self.units}"'
        
        if self.height - 3:
            info += f'markerHeight="{self.height}"'
        if self.width - 3:
            info += f'markerWidth="{self.width}"'
        if self.orient:
            info += f'orient="{self.orient}"'
        if self.x:
            info += f'refX="{self.x}"'
        if self.y:
            info += f'refY="{self.y}"'

        info = self.viewBox_attribute(info)
        info = self.ratio_attribute(info)
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

#TODO: marker draw