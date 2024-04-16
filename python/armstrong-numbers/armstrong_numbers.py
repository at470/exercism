def is_armstrong_number(number):
    is_armstrong_number = True
    input_as_string = str(number)
    exponent = int(len(input_as_string))
    if number is 0 or exponent is 1:
        is_armstrong_number = True 
    if exponent == 2:
        is_armstrong_number = False
    if exponent > 2:
        sum_for_armstrong_number_check = 0
        for value in input_as_string:
            sum_for_armstrong_number_check = sum_for_armstrong_number_check + int(value) ** exponent
        if sum_for_armstrong_number_check != number:
            is_armstrong_number = False
    return is_armstrong_number
