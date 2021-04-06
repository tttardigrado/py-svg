from shapes import *
class Canvas:
    def __init__(self, width=400,height=400, x=0,y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.inner = ""
        self.fi = "#000000"
        self.st = "#000000"
        self.stW = 1
        self.fiO = 1
        self.stO = 1

    def stroke(self, st):
        self.st = st

    def strokeOpacity(self, stO):
        self.stO = stO

    def fillOpacity(self, fiO):
        self.fiO = fiO

    def fill(self, fi):
        self.fi = fi

    def noFill(self):
        self.fi = "none"
    
    def noStroke(self):
        self.st = "none"
    
    def draw(self, shape):
        s = shape.draw()
        self.inner += s

    def render(self):
        info = f"""<svg viewBox="{self.x} {self.y} {self.width} {self.height}">"""
        info += self.inner
        info += "</svg>"
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

if __name__ == "__main__":
    ca = Canvas()
    ca.noStroke()
    for i in range(10):
        ca.fill(f"rgb({i*25.5},{i*25.5},{i*25.5})")
        ca.draw(ca.circle(i*5,i*5,5))

    ca.stroke("#ff00ff")
    ca.draw(ca.line(0,0,100,100))

    r = ca.render()

    print(r)