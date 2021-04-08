from .svg import SVG

class InnerShape(SVG):
    def __init__(self, tag: str, canvas):
        super().__init__(tag,canvas)
        self.inner = []
        
    # inner
    def set_inner(self, new_inner:list):
        self.inner = new_inner

    def add_inner(self, new_inner:str):
        self.inner.append(new_inner)

    def rem_inner(self, index:int):
        del self.inner[index]

    def inner_attribute(self, info:str):
        if self.inner:
            info += f""">{" ".join(self.inner)}</{self.tag}>'"""
        else:
            info += "/>"
        return info