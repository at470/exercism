def convert(number):
    """
    If a given number:
        is divisible by 3, add "Pling" to the result.
        is divisible by 5, add "Plang" to the result.
        is divisible by 7, add "Plong" to the result.
        is not divisible by 3, 5, or 7, the result 
        should be the number as a string.
    """
    string = ''
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        string = string + str(number)
    if number % 3 is 0:
        string = string + 'Pling'
    if number % 5 is 0:
        string = string + 'Plang'
    if number % 7 is 0:
        string = string + 'Plong'
    return string
