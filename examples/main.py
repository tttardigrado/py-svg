from ..canvas import Canvas
from ..renderer import render

w, h = 1200, 1200
code_start = h/20
code_end = h - h/20
lines = 30
line_sep = (code_end - code_start)/lines


ca = Canvas(width=w, height=h)
ca.strokeWeight(12)
ca.linecap("round")
ca.stroke("#00ffff")
ca.d(ca.line(200, 600, 1000, 600))

line_y = code_start
for i in range(lines):
    ca.d(ca.line(50, line_y, 1150, line_y))
    line_y += line_sep


render([ca])
