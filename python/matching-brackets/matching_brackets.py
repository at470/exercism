def is_paired(input_string):
    """
    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. 
    """

    input_string_list = []
    for char in input_string:
        input_string_list.append(char)

    stack = []
    bracket_pairs = {
        '(' : ')',
        ')' : '(',
        '{' : '}',
        '}' : '{',
        '[' : ']',
        ']' : '['
    }

    is_paired_result = False
    mismatch_flag = 0
    for char in input_string_list:
        if char in ('{', '(', '['):
            stack.append(char)
        elif char in ('}', ')', ']'):
            if len(stack) > 0 and bracket_pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
            
    return stack == []