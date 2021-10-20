from .intervals import IntervalTemplate

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
