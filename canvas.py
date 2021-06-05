from pysvg import *
import renderer

class Canvas:
    def __init__(self, width=400, height=400, x=0, y=0):
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
        self.stOffset = 0
        self.stLineCap = "butt"
        self.stLineJoin = "miter"
        self.style = ""
        self.ma = ""
        self.cp = ""
        self.fillRule = "nonzero"
        self.clipRule = "nonzero"
        self.mk = ""

    def set_clipPath(self, path: str, url: bool = True):
        if url:
            self.cp = f"url(#{path})"
        else:
            self.cp = path

    def set_clipRule(self, keyword: str):
        self.clipRule = keyword

    def set_mask(self, mask: str, url: bool = True):
        if url:
            self.ma = f"url(#{mask})"
        else:
            self.ma = mask

    def set_marker(self, marker: str, url: bool = True):
        if url:
            self.mk = f"url(#{marker})"
        else:
            self.mk = marker

    def noClipPath(self):
        self.cp = ""

    def noMask(self):
        self.ma = ""

    def noMarker(self):
        self.mk = ""

    def strokeWeight(self, stW: float):
        self.stW = stW

    def linecap(self, keyword: str):
        self.stLineCap = keyword

    def lineJoin(self, keyword: str):
        self.stLineJoin = keyword

    def stroke(self, st: str):
        self.st = st

    def strokeArray(self, arr: list):
        self.stA = arr

    def strokeOffset(self, offset: float):
        self.stOffset = offset

    def strokeOpacity(self, stO: float):
        self.stO = stO

    def fillOpacity(self, fiO: float):
        self.fiO = fiO

    def fill(self, fi: str):
        self.fi = fi

    def set_fillRule(self, keyword: str):
        self.fillRule = keyword

    def noFill(self):
        self.fi = "none"

    def noStroke(self):
        self.st = "none"

    def d(self, shape):
        s = shape.draw()
        self.inner.append(s)

    def set_style(self, style: str):
        self.style = style

    def set_opacity(self, opacity: float):
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

    # Shapes
    def circle(self, x:float=0, y:float=0, r:float=0):
        c = Circle(self, x, y, r)
        return c

    def ellipse(self,x:float=0,y:float=0,rx:float=0,ry:float=0):
        e = Ellipse(self,x,y,rx,ry)
        return e

    def line(self, x1:float=0,y1:float=0,x2:float=100,y2:float=100):
        l = Line(self, x1, y1,x2,y2)
        return l
    
    def polygon(self, points:list = []):
        p = Polygon(self, points)
        return p
    
    def polyline(self, points:list = []):
        p = PolyLine(self, points)
        return p
    
    def rect(self, x:float=0,y:float=0,w:float=0,h:float=0,rx:float=0,ry:float=0):
        r = Rect(self, x,y,w,h,rx,ry)
        return r
    def square(self, x:float=0,y:float=0,s:float=0,rx:float=0,ry:float=0):
        s = Square(self, x,y,s,rx,ry)
        return s
    def text(self, t:str="", x:float=0,y:float=0,dx:float=0,dy:float=0):
        te = Text(self, t, x,y,dx,dy)
        return te
    def tspan(self,t:str="",x:float=0,y:float=0,dx:float=0,dy:float=0):
        ts = TSpan(self, t,x,y,dx,dy)
        return ts
    def tpath(self, t:str="", href:str=""):
        tp = TextPath(self, t,href)
        return tp

    # Others
    def clippath(self, _id:str=""):
        c = ClipPath(self,_id)
        return c
    
    def defs(self,_id:str=""):
        d = Defs(self, _id)
        return d
    def g(self, _id:str=""):
        a = G(self,_id)
        return a
    def image(self, href:str="", x:float=0,y:float=0,w:float=0,h:float=0):
        i = Image(self, href,x,y,w,h)
        return i
    def marker(self, _id:str="",w:float=0, h:float=0):
        m = Marker(self, _id,h,w)
        return m
    def mask(self, _id:str="", x:float=0,y:float=0,w:float=0,h:float=0):
        m = Mask(self, _id, x,y,w,h)
        return m
    def path(self, d:str=""):
        p = Path(self, d)
        return p
    def symbol(self, _id:str="", x:float=0,y:float=0,w:float=0,h:float=0,refx:float=0,refy:float=0):
        s = Symbol(self, _id,x,y,w,h,refx,refy)
        return s
    def use(self, href:str="", x:float=0,y:float=0,w:float=0,h:float=0):
        u = Use(self, href,x,y,w,h)

    # Gradients
    def linearGrad(self, _id:str="", x1:float=0,y1:float=0,x2:float=0,y2:float=0):
        l = LinearGradient(self, _id,x1,y1,x2,y2)
        return l
    def radialGrad(self,_id:str="", cx:float=0,cy:float=0,r:float=0,fx:float=0,fy:float=0,fr:float=0):
        r = RadialGradient(self,_id,cx,cy,r,fx,fy,fr)
        return r
    def pattern(self, href:str="", x:float=0,y:float=0,w:float=0,h:float=0):
        p = Pattern(self, href, x,y,w,h)
        return p
    def stop(self, offset:float=0, color:str="#000000", opacity:float=1):
        s = Stop(offset,color,opacity)
        return s
    

    #anim
    def motionAnim(self, d:str=""):
        a = MotionAnim(self, d)
        return a
    def tranAnim(self, _type:str=""):
        a = TranAnim(self,_type)
        return a
    def anim(self, attribute:str=""):
        a = Animation("animation", self)
        a.set_attribute(attribute)
        return a

if __name__ == "__main__":
    ca = Canvas()
    ca.noStroke()
    m = ca.mask()
    m.d(ca.circle(5, 5, 5))
    ca.d(m)
    for i in range(10):
        ca.fill(f"rgb({i*25.5},{i*25.5},{i*25.5})")
        ca.d(ca.circle(i*5,i*5,5))

    ca.stroke("#ff00ff")
    ca.d(ca.line(0,0,100,100))

    r = ca.render()
    renderer.render([ca])
