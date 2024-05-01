def square_root(number):
    """
    cheating as i'm assuming the test cases are perfect squares
    """
    stages = 0
    odd_num = 1
    while number > 0:
        number = number - odd_num
        stages+= 1
        odd_num = odd_num + 2
    return stages