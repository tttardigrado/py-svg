from pyro import Canvas, render
from random import random, randrange

w, h = 1200, 1200
# Where the code starts and ends
code_start = h/60
code_end = h - h/100

# Code Line Thickness
code_size = 10

# Code Segments (Number and length)
min_segments = 5
max_segments = 16
min_segment_length = 5
max_segment_length = 60
segment_sep = 20

# Lines of code
code_lines = 60
code_sep = (code_end - code_start)/code_lines
line_break_chance = .4

# Indent values
indent_size = 50
max_indents = 6
indent_inc_chance = .4
indent_dec_chance = .3

# Random Colors
random_colors = False

# Higher value means the color will change more often
change_chance = .4

# If you want to use your own color palette, just set random colors to false
# colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]
colors = ["#c2616a", "#a2be8f", "#80a1c0", "#eacb8f", "#85c0cf"]

# Background Color
bc = ("#2e343f")


def set_palette_color(canvas):
    c = colors[int(random()*len(colors))]
    ca.stroke(c)


ca = Canvas(width=w, height=h)
ca.strokeWeight(code_size)
ca.linecap("round")
ca.background(bc)

set_palette_color(ca)

line_y = code_start
indent = 0
for i in range(code_lines):
    # if (i < 4):
    #     stroke(*colors[i])
    if (not (random() < line_break_chance and indent == 0)):
        line_x = indent_size + (indent * indent_size)
        line_segments = int(randrange(min_segments, max_segments))
        for j in range(line_segments):
            if (random() < change_chance):
                set_palette_color(ca)
            segment_length = randrange(min_segment_length, max_segment_length)

            ca.d(ca.line(line_x, line_y, line_x + segment_length, line_y))
            line_x = line_x + segment_length + segment_sep
        if (random() < indent_inc_chance and indent < max_indents):
            indent += 1
        elif(random() < indent_dec_chance and indent > 0):
            indent -= int(randrange(1, max_indents))
            if (indent < 0):
                indent = 0
    line_y += code_sep

render([ca], name="code")
