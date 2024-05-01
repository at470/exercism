
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    score_span = highest - 40
    bucket_size = int(score_span / 4)

    grade_index = 0
    grade_boundary = []
    while grade_index in range(0, 4):
        lower_bound = 41 + grade_index*bucket_size
        print(grade_index, lower_bound)
        grade_boundary.append(lower_bound)
        grade_index+=1
    # grade_boundary = [41, 41+bucket_size, 41+2*bucket_size, 41 +3*bucket_size]
    return grade_boundary


highest = 88
print(letter_grades(highest))