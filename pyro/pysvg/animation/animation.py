from typing import Any


class Animation:
    """Base Animation class"""

    def __init__(self, tag, canvas):
        self.canvas = canvas
        self.tag = tag
        self.id = None
        self.classes = []
        self.style = {}
        self.attribute = ""

        # props
        self.begin = []
        self.end = []
        self.dur = ""
        self.min = ""
        self.max = ""
        self.restart = "always"
        self.repeat = 0
        self.rpDur = ""
        self.fill = "remove"
        self.calcMode = "linear"
        self.values = []
        self.times = []
        self.splines = []
        self.range = {"from": "",
                      "to": "",
                      "by": ""}
        self.additive = "replace"
        self.acumulate = "none"

    # props

    # ---begin
    def set_begin(self, values: list):
        self.begin = values

    def add_begin(self, value: Any):
        self.begin.append(value)

    def rem_begin(self, index: int):
        del self.begin[index]

    # ---end
    def set_end(self, values: list):
        self.end = values

    def add_end(self, value: Any):
        self.end.append(value)

    def rem_end(self, index: int):
        del self.end[index]

    # ---dur
    def set_duration(self, value: str):
        self.dur = value

    # ---min
    def set_min(self, value: str):
        self.min = value

    # ---max
    def set_max(self, value: str):
        self.max = value

    # ---restart
    def set_restart(self, keyword: str):
        self.restart = keyword

    # ---repeat
    def set_repeat(self, count: int):
        self.repeat = count

    # ---rpDur
    def set_rpDur(self, value: str):
        self.rpDur = value

    # ---fill
    def set_fill(self, keyword: str):
        self.fill = keyword

    def timing_attribute(self, info: str):
        if self.begin:
            info += f' begin="{";".join(map(str,self.begin))}"'
        if self.end:
            info += f' end="{";".join(map(str,self.end))}"'
        if self.dur:
            info += f' dur="{self.dur}"'
        if self.min:
            info += f' min="{self.min}"'
        if self.max:
            info += f' max="{self.max}"'
        if self.restart != "always":
            info += f' restart="{self.restart}"'
        if self.repeat <= 0:
            info += ' repeatCount="infinite"'
        else:
            info += f' repeatCount="{self.repeat}"'
        if self.rpDur:
            info += f' repeatDur="{self.rpDur}"'
        if self.fill != "remove":
            info += f' fill="{self.fill}"'
        return info

    # ---calcMode
    def set_calcMode(self, keyword: str):
        self.calcMode = keyword

    # ---values
    def set_values(self, values: list):
        self.values = values

    def add_values(self, value: float):
        self.values.append(value)

    def rem_values(self, index: int):
        del self.values[index]

    # ---times
    def set_times(self, times: list):
        self.times = times

    def add_times(self, time: float):
        self.times.append(time)

    def rem_times(self, index: int):
        del self.times[index]

    # ---splines
    def set_splines(self, splines: list):
        self.splines = splines

    def add_splines(self, x1: float, y1: float, x2: float, y2: float):
        self.splines.append([x1, y1, x2, y2])

    def rem_splines(self, index: int):
        del self.splines[index]

    # ---range
    def set_range(self, _from: Any, to: Any, by: Any):
        self.range["from"] = _from
        self.range["to"] = to
        self.range["by"] = by

    def get_from(self):
        return self.range["from"]

    def get_to(self):
        return self.range["to"]

    def get_by(self):
        return self.range["by"]

    def set_from(self, _from: Any):
        self.range["from"] = _from

    def set_to(self, to: Any):
        self.range["to"] = to

    def set_by(self, by: Any):
        self.range["by"] = by

    def values_attribute(self, info: str):
        if self.calcMode != "linear":
            info += f' calcMode="{self.calcMode}"'
        if self.values:
            info += f' values="{";".join(map(str,self.values))}"'
        if self.times:
            info += f' keyTimes="{";".join(map(str,self.times))}"'
        if self.splines:
            r = ""
            for i in self.splines:
                r += " ".join(map(str, i)) + ";"
            info += f' keySplines="{r}"'
        if self.range["from"]:
            info += f' from="{self.range["from"]}"'
        if self.range["to"]:
            info += f' to="{self.range["to"]}"'
        if self.range["by"]:
            info += f' by="{self.range["by"]}"'
        return info

    # Other
    def set_attribute(self, keyword: str):
        self.attribute = keyword

    def set_additive(self, keyword: str):
        self.additive = keyword

    def set_acumulate(self, keyword: str):
        self.acumulate = keyword

    def other_attributes(self, info: str):
        if self.attribute:
            info += f' attributeName="{self.attribute}"'
        if self.additive != "replace":
            info += f' additive="{self.additive}"'
        if self.acumulate != "none":
            info += f' acumulate="{self.acumulate}"'
        return info
    # id

    def set_id(self, new_id: str):
        self.id = new_id

    def id_attribute(self, info: str):
        if self.id:
            info += f""" id='{self.id}'"""
        return info

    # style
    def set_style(self, new_style: dict):
        self.style = new_style

    def add_style(self, style: str, value: Any):
        self.style[style] = value

    def rem_style(self, style: str):
        del self.style[style]

    def style_attribute(self, info: str):
        if self.style:
            s = """ style=" """
            for k, v in self.style:
                s += f"""{k}:{v};"""
            s += """ " """
            info += s
        return info

    # class
    def set_class(self, new_classes: list):
        self.classes = new_classes

    def add_class(self, new_class: str):
        self.classes.append(new_class)

    def rem_class(self, index: int):
        del self.classes[index]

    def class_attribute(self, info: str):
        if self.classes:
            info += f""" class='{" ".join(self.classes)}'"""
        return info

    def draw(self):
        info = f"<{self.tag}"
        info = self.values_attribute(info)
        info = self.timing_attribute(info)
        info = self.other_attributes(info)
        info = self.id_attribute(info)
        info = self.class_attribute(info)
        info = self.style_attribute(info)
        info += " />"
        return info
