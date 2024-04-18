def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")
    
    check_num = 2
    loop_count = 1
    factors_dict = {1:True}
    check_num_pair = number // check_num

    # check between 1 and number-1
    while check_num in range(2, number):
        # if already_checked[check_num] is True:
        if check_num in factors_dict.keys():
            # print('already checked')
            pass
        else:
            if number % check_num == 0:
                # print('checking')
                factors_dict[check_num] = True
                factors_dict[check_num_pair] = True
                loop_count += 1
        check_num += 1

    aliquot_sum = sum(factors_dict.keys())
    print(aliquot_sum)
    # print(factors_dict, loop_count)

    number_classification = ''
    if aliquot_sum == 1:
        number_classification = 'deficient'
    elif number == aliquot_sum:
        number_classification = 'perfect'
    elif number < aliquot_sum:
        number_classification = 'abundant'
    else:
        number_classification = 'deficient'
    return number_classification





"""
IGNORE
ITERATION 1: Most inefficient, loop everything except first one
number = 12

number_factor_list = [1]
check_num = 2
loop_count = 1

# check between 1 and number-1
while check_num in range(2, number):
    if number % check_num == 0:
        number_factor_list.append(check_num)
    check_num += 1
    loop_count += 1
aliquot_sum = sum(number_factor_list)
print(number_factor_list, aliquot_sum, loop_count)
"""