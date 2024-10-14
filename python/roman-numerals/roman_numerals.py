def roman(number):
    arabic_to_roman_lookup = {1000 : 'M',
                              500 : 'D',
                              100 : 'C',
                              50 : 'L',
                              10 : 'X',
                              5 : 'V',
                              1 : 'I'}

    special_case_fours = {4 : 'IV',
                              40 : 'XL',
                              400 : 'CD'}

    
    # set up
    roman_numerals = list(arabic_to_roman_lookup.keys())  
    remaining_number = number
    returned_string = ''

    for numeral_value in roman_numerals:
        # ignore numerals greater than the remaining number
        if numeral_value <= remaining_number:
            count = remaining_number // numeral_value
            # handle 9
            if remaining_number == 9:
                returned_string = returned_string + 'IX'
                # remaining_number = remaining_number-9
                remaining_number = 0
            # handle numbers in 900s
            elif remaining_number >= 900 and remaining_number < 1000:
                print('hello')
                returned_string = returned_string + 'CM'
                remaining_number = remaining_number - 900
            # handle numbers in 90s
            elif remaining_number >= 90 and remaining_number < 100:
                returned_string = returned_string + 'XC'
                remaining_number = remaining_number - 90 
            # handle special case of fours
            elif count == 4:
                returned_string = returned_string + special_case_fours[count*numeral_value]
                remaining_number = remaining_number - count*numeral_value
            else:
                while count > 0:
                    returned_string = returned_string + arabic_to_roman_lookup[numeral_value]
                    count-=1
                remaining_number = remaining_number % numeral_value
    return returned_string