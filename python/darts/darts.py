def score(x, y):
    """
    The outer circle has a radius of 10 units (this is equivalent to the total 
    radius for the entire target), the middle circle a radius of 5 units, and 
    the inner circle a radius of 1. Of course, they are all centered at the 
    same point — that is, the circles are concentric defined by the coordinates 
    (0, 0).

    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.
"""
    distance_to_point = (x ** 2 + y ** 2) ** 0.5
    score = 0
    #  If the dart lands outside the target, player earns no points (0 points).
    if distance_to_point > 10:
        score = 0
    # If the dart lands in the outer circle of the target, player earns 1 point.
    if 5 < distance_to_point <= 10:
        score = 1
    if 1 < distance_to_point <= 5:
        score = 5
    if distance_to_point <= 1:
        score = 10
    return score