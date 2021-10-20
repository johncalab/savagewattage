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
        return self.name + " - " + f"[{self.low},{self.high}]" + " - " + self.desc

templates = [
    IntervalTemplate(
        name = "Recovery",
        low = .3,
        high = .5,
        desc = "∞",
    ),
    IntervalTemplate(
        name = "Endurance",
        low = .5,
        high = .8,
        desc = "1-4hours",
    ),
    IntervalTemplate(
        name = "SteadyState",
        low = .95,
        high = 1.0,
        desc = "10-30min,20-40min of total work",
    ),
    IntervalTemplate(
        name = "Tabata",
        low = 1.3,
        high = 1.8,
        desc = "30s/30s, 8-15reps, 2-3sets",
    ),
]

for templ in templates:
    print(Interval.from_template(ftp=100,template=templ))
