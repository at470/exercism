def square_root(number):
    if number == 1:
        return 1
    
    step = 1
    count = 0
    while number > 0:
        print(number)
        number = number - count
        count+= 1
        step = step + 2
    return count

number = 25