import math



def rad(angle:float):
    return math.radians(angle)

def deg(angle):
    return math.degrees(angle)
    

# sin
def sin(angle:float,unit:str="deg"):
    if unit == "deg":
        angle = rad(angle)
    return math.sin(angle)
# cos
def cos(angle:float,unit:str="deg"):
    if unit == "deg":
        angle = rad(angle)
    return math.cos(angle)
# tg
def tan(angle:float,unit:str="deg"):
    if unit == "deg":
        angle = rad(angle)
    return math.tan(angle)

# asin
def asin(x:float,unit:str="deg"):
    angle= math.asin(x)
    if unit == "deg":
        angle = deg(angle)
    return angle
# acos
def acos(x:float,unit:str="deg"):
    angle= math.acos(x)
    if unit == "deg":
        angle = deg(angle)
    return angle
# atg 
def atan(x:float,unit:str="deg"):
    angle= math.atan(x)
    if unit == "deg":
        angle = deg(angle)
    return angle

# root
def root(x:float, r:int):
    return x**(1/r)
# sqrt
def sqrt(x:float):
    return x**(1/2)
# cbrt
def cbrt(x:float):
    return x**(1/3)
# exp
def exp(x:float):
    return math.exp(x)

# log
def log(x:float, base=math.e):
    return math.log(x,base)
# abs
def abs(x:float):
    return math.fabs(x)
# sign
def sign(x:float):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0