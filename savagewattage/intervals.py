from dataclasses import dataclass

@dataclass
class IntervalTemplate:
    name: str
    low: float
    high: float
    desc: str

@dataclass
class Interval:
    name: str
    low: int
    high: int
    desc: str

    @classmethod
    def from_template(cls,template: IntervalTemplate, ftp: int):
        return cls(
            name = template.name,
            low = int(template.low * ftp),
            high = int(template.high * ftp),
            desc = template.desc,
        )

    def __str__(self):
        out = []
        out.append(self.name)
        out.append(self.desc)
        out.append(f"[{self.low},{self.high}]")
        return " - ".join(out)
