def steps(number, count=0):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return count
    count += 1
    if number % 2 is 0:
        number = number // 2
        return steps(number, count)
    else:
        number = 3 * number + 1
        return steps(number, count)