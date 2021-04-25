from pysvg import *
class Canvas:
    def __init__(self, width=400,height=400, x=0,y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.inner = []
        self.o = 1
        self.fi = "#000000"
        self.st = "#000000"
        self.stW = 1
        self.fiO = 1
        self.stO = 1
        self.stA = []
        self.stOffset=0
        self.stLineCap="butt"
        self.stLineJoin="miter"
        self.style = ""
        self.ma = ""
        self.cp = ""

    def set_clipPath(self, path:str, url:bool=True):
        if url:
            self.cp = f"url(#{path})"
        else:
            self.cp = path

    def set_mask(self, mask:str, url:bool=True):
        if url:
            self.ma = f"url(#{mask})"
        else:
            self.ma = mask

    def noClipPath(self):
        self.cp = ""

    def noMask(self):
        self.ma = ""
    
    def strokeWeight(self, stW:float):
        self.stW = stW

    def linecap(self, keyword:str):
        self.stLineCap = keyword

    def lineJoin(self,keyword:str):
        self.stLineJoin = keyword

    def stroke(self, st:str):
        self.st = st
    
    def strokeArray(self, arr:list):
        self.stA = arr
    
    def strokeOffset(self, offset:float):
        self.stOffset = offset

    def strokeOpacity(self, stO:float):
        self.stO = stO

    def strokeOpacity(self, stO:float):
        self.stO = stO

    def fillOpacity(self, fiO:float):
        self.fiO = fiO

    def fill(self, fi:str):
        self.fi = fi

    def noFill(self):
        self.fi = "none"
    
    def noStroke(self):
        self.st = "none"
    
    def d(self, shape):
        s = shape.draw()
        self.inner.append(s)
    
    
    def set_style(self, style:str):
        self.style = style
    
    def set_opacity(self,opacity:float):
        self.o = opacity    

    def render(self):
        info = f"""<svg viewBox="{self.x} {self.y} {self.width} {self.height}">\n"""
        if self.style:
            info += "<style>"
            info += self.set_style
            info += "</style>\n"        
        if self.inner:
            info += " ".join(self.inner)
        info += "\n</svg>"
        return info

    def circle(self, x=0, y=0, r=0):
        c = Circle(self,x,y,r)
        return c
    def rect(self, x=0, y=0, w=0,h=0,rx=0,ry=0):
        r = Rect(self,x,y,w,h,rx,ry)
        return r
    def square(self, x=0, y=0, s=0,rx=0,ry=0):
        r = Square(self,x,y,s,rx,ry)
        return r

    def ellipse(self, x=0, y=0,rx=0,ry=0):
        e = Ellipse(self,x,y,rx,ry)
        return e
    def line(self,x1=0,y1=0,x2=0,y2=0):
        l = Line(self, x1,y1,x2,y2)
        return l
    def mask(self,x1=0,y1=0,x2=0,y2=0):
        l = Mask(self, "d")
        return l

if __name__ == "__main__":
    ca = Canvas()
    ca.noStroke()
    m = ca.mask()
    m.d(ca.circle(5,5,5))
    ca.d(m)
    #for i in range(10):
        #ca.fill(f"rgb({i*25.5},{i*25.5},{i*25.5})")
        #ca.d(ca.circle(i*5,i*5,5))
    
    #ca.stroke("#ff00ff")
    #ca.d(ca.line(0,0,100,100))

    r = ca.render()

    print(r)