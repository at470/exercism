def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    exponent = number - 1
    return 2 ** exponent


def total():
    count = 1
    total_num_grains = 0
    while count in range(1, 65):
        total_num_grains = total_num_grains + square(count)
        count += 1
    return total_num_grains