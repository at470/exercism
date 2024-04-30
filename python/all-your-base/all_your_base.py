def rebase(input_base, digits, output_base):
    """
    The number 42, in base 10, means:

    (4 × 10¹) + (2 × 10⁰)

    The number 101010, in base 2, means:

    (1 × 2⁵) + (0 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)

    The number 1120, in base 3, means:

    (1 × 3³) + (1 × 3²) + (2 × 3¹) + (0 × 3⁰)
    """
    
    # input_base = 3, digits = [1, 1, 2, 0], output_base = 16

    # for input.
    if input_base < 2:
        raise ValueError("input base must be >= 2")

      # or, for output.
    if output_base < 2 :
        raise ValueError("output base must be >= 2")

    max_power = len(digits) - 1
    result_in_base_ten = []

    for d in digits:
    # another example for input.
        if 0 <= d < input_base:
            result_in_base_ten.append(d * input_base ** max_power)
            max_power -= 1
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # add conditional to handle returning empty list
    if sum(result_in_base_ten) == []:
        number_in_base_ten = [0]
    else:
        number_in_base_ten = sum(result_in_base_ten)

    number_being_divided_in_base_ten = number_in_base_ten
    result_in_output_base = []

    while number_being_divided_in_base_ten > 0:
        div, mod = divmod(number_being_divided_in_base_ten, output_base)
        result_in_output_base.append(mod)
        number_being_divided_in_base_ten = div

    result_in_output_base.reverse()
    
    # add conditional to handle returning empty list
    if result_in_output_base == []:
        return [0]
    else:
        return result_in_output_base