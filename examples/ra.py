from pyro import Canvas, render
from random import random, randrange, choice, randint
from math import pi, sin, cos
# Background Color
w = 1000
h = 1000
sw = 1

maxRadius = 80
minRadius = 20
border = 15
numberOfCircles = 55
tau = 2 * pi
color0 = [0, 50, 50]


def background_color() -> str:
    values = ["c", "d", "e", "f"]
    bc = ""
    for _ in range(2):
        bc += choice(values)
    bc = "#" + bc + bc + bc
    return bc


def background_color_hsl() -> str:
    bc = "hsl("
    h = randint(0, 360)
    s = randint(10, 50)
    l = randint(1, 20)
    bc += f"{h}, {s}%, {l}%)"
    return bc


def circleValues() -> list:
    centerX = random() * w
    centerY = random() * h
    radius = (random() * (maxRadius - minRadius)) + minRadius
    return [centerX, centerY, radius]


def distance(c1: list, c2: list) -> float:
    squareX = (c1[0] - c2[0]) ** 2
    squareY = (c1[1] - c2[1]) ** 2
    dist = (squareX+squareY) ** (1/2)
    return dist


def radiusSum(c1: list, c2: list) -> float:
    return c1[2] + c2[2] + border


def isDrawable(c: list, circles: list) -> bool:
    isToDraw = True
    for circle in circles:
        dist = distance(c, circle)
        radSum = radiusSum(c, circle)
        if dist < radSum:
            isToDraw = False
            break
    return isToDraw


bc = background_color_hsl()

# init
ca = Canvas(width=w, height=h)
ca.strokeWeight(sw)
ca.linecap("round")
ca.background(bc)
ca.stroke("#000000")


circles = []
while len(circles) < numberOfCircles:
    newCircle = circleValues()
    isToDraw = isDrawable(newCircle, circles)
    if isToDraw:
        circles.append(newCircle)


def liners(ca: Canvas, c: list):
    number = randint(10, 70)
    number = tau / number
    angle = 0
    while angle < tau:
        #shift = random() * c[2]/10
        radius = c[2]  # + shift
        x = cos(angle) * radius + c[0]
        y = sin(angle) * radius + c[1]
        ca.d(ca.line(c[0], c[1], x, y))
        angle += number


def borderDots(ca: Canvas, c: list, radius: float):
    number = randint(50, 70)
    number = tau / number
    angle = 0
    while angle < tau:
        x = cos(angle) * radius + c[0]
        y = sin(angle) * radius + c[1]
        ca.d(ca.line(x, y, x, y))
        angle += number


def dots(ca: Canvas, c: list):
    maxR = c[2]
    radius = 0
    div = randint(5, 10)
    while radius < maxR:
        radius += random() * maxR/div + 4 * sw
        borderDots(ca, c, radius)


def increaseHue(color: list, shift: float) -> list:
    color[0] += randint(0, shift)
    if color[0] > 360:
        color[0] -= 360
    elif color[0] < 0:
        color[0] += 360
    return color


for c in circles:
    #circ = ca.circle(c[0], c[1], c[2])
    # ca.d(circ)
    color0 = increaseHue(color0, int(360/numberOfCircles))
    ca.st = f"hsl({color0[0]}, {color0[1]}%, {color0[2]}%)"
    case = choice([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3])
    if case == 1:
        liners(ca, c)
    elif case == 2:
        dots(ca, c)
    else:
        borderDots(ca, c, c[2])
    # render
render([ca], name="test")
