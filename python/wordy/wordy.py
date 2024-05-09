def answer(question):


    import re

    # Iteration 0 — Numbers
    if re.match(r'^[Ww]hat is \d+\?$', question):
        answer = re.findall(r'[\d]+', question)
        value = int(answer[0]) #use findall(), convert to integer (string by default)

    # Iteration 1 — Addition
    # Handle large numbers and negative numbers.
    elif re.match(r'^[Ww]hat is -{0,1}\d+ plus -{0,1}\d+\?$', question):
        answer = re.findall(r'-{0,1}\d+', question)
        value = int(answer[0]) + int(answer[1])

    # Iteration 2 — Subtraction, Multiplication and Division
    # A - Subtraction
    elif re.match(r'^[Ww]hat is -{0,1}\d+ minus -{0,1}\d+\?$', question):
        answer = re.findall(r'-{0,1}\d+', question)
        value = int(answer[0]) - int(answer[1])
    
    # B - Multiplication
    elif re.match(r'^[Ww]hat is -{0,1}\d+ multiplied by -{0,1}\d+\?$', question):
        answer = re.findall(r'-{0,1}\d+', question)
        value = int(answer[0]) * int(answer[1])

    # C - Division
    elif re.match(r'^[Ww]hat is -{0,1}\d+ divided by -{0,1}\d+\?$', question):
        answer = re.findall(r'-{0,1}\d+', question)
        value = int(answer[0]) // int(answer[1])
    else:
        raise ValueError("unknown operation")
        raise ValueError("syntax error")
    
    return value

    



"""
Notes
re.match() checks for a match only at the beginning of the string
re.search() checks for a match anywhere in the string
"""