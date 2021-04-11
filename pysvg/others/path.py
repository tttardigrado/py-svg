from ..transform import InnerTransform

# TODO: PATH

class Path(InnerTransform):
    def __init__(self, canvas, d:str=""):
        super().__init__("path", canvas)
        self.d=d
        self.pathLength = None

    def set_d(self, d:str):
        self.d = d
    
    def d_move(self, x:float, y:float, relative:bool=False):
        if relative:
            self.d = f" m {x},{y}"
        else:
            self.d = f" M {x},{y}"
    
    def d_line(self, x:float,y:float, relative:bool=False):
        if relative:
            self.d = f" l {x},{y}"
        else:
            self.d = f" L {x},{y}"
    
    def d_horizontal(self, x:float, relative:bool=False):
        if relative:
            self.d = f" h {x}"
        else:
            self.d = f" H {x}"

    def d_vertical(self, y:float, relative:bool=False):
        if relative:
            self.d = f" v {y}"
        else:
            self.d = f" V {y}"
    
    
    
    


    def set_path_length(self,length:float):
        self.pathLength = length

    def no_path_length(self):
        self.pathLength = None

    def draw(self):
        info = f"<{self.tag} "

        if self.pathLength:
            info += f" pathLength='{self.pathLength}'"

        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info = self.transform_attribute(info)
        info = self.super_attribute(info)
        info = self.inner_attribute(info)
        return info