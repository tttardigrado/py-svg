from ..transform import InnerTransform
class PolyLine(InnerTransform):

    def __init__(self,canvas, points:list=[]):
        super().__init__("polyline", canvas)
        self.points = points
        self.pathLength = None
    
    def set_path_length(self,length:float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def add_point(self,x:float,y:float):
        self.points.append([x,y])

    def rem_point(self,index:int):
        del self.points[index]

    def set_points(self,points:list):
        self.points = points

    def draw(self):
        info = f"""<{self.tag} points=" """
        for point in self.points:
            info += f" {point[0]},{point[1]} "
        if self.pathLength:
            info += f""" " pathLength='{self.pathLength}'"""
        
        
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info
