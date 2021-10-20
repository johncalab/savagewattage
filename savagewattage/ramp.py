"""
Protocol:
    Warm up.
    Start at 100W.
    Every 150seconds increase by 25W.
    Go until failure.

    Record two things:
        completed: wattage of last SUCCESSFUL ramp
        extra: seconds of last failed ramp

    For example:
    150 seconds @100W
    150 seconds @125W
    150 seconds @150W
    150 seconds @175W
    150 seconds @200W
    150 seconds @225W
    150 seconds @250W
    150 seconds @275W
    150 seconds @300W
    13 seconds @325

    completed  = 300
    extra = 13

    leading to an estimated ftp of: 249
"""

def estimate_ftp(completed: int, extra: int = 0):
    wattage = ((extra/150) * 25) + completed
    ftp = wattage * .825
    return int(ftp)

