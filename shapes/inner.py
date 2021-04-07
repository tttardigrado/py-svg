from .shapes import Shape

class InnerShape(Shape):
    def __init__(self, tag, canvas):
        super().__init__(tag,canvas)
        self.inner = []
        
    # inner
    def set_inner(self, new_inner):
        self.inner = new_inner

    def add_inner(self, new_inner):
        self.inner.append(new_inner)

    def rem_inner(self, rem_inner):
        self.inner.remove(rem_inner)

    def inner_attribute(self, info):
        if self.inner:
            info += f""">{" ".join(self.inner)}</{self.tag}>'"""
        else:
            info += "/>"
        return info