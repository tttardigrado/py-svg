def rgb(r:int,g:int,b:int):
    return f"rgb({r},{g},{b})"

def rgba(r:int,g:int,b:int, a:float=1):
    return f"rgba({r},{g},{b},{a})"

def hex(r:str,g:str,b:str):
    return f"#{r}{g}{b}"

def hexa(r:str,g:str,b:str,a:str):
    return f"#{r}{g}{b}{a}"

def hsl(h:int,s:int,l:int, hunit:str="deg"):
    return f"hsl({h}{hunit},{s}%,{l}%)"

def hsla(h:int,s:int,l:int, a:float=1, hunit:str="deg"):
    return f"hsla({h}{hunit},{s}%,{l}%)"



