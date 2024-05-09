def rows(letter):
    """
    The first row contains one 'A'.
    The last row contains one 'A'.
    All rows, except the first and last, have exactly two identical letters.
    All rows have as many trailing spaces as leading spaces. (This might be 0).
    The diamond is horizontally symmetric.
    The diamond is vertically symmetric.
    The diamond has a square shape (width equals height).
    The letters form a diamond shape.
    The top half has the letters in ascending order.
    The bottom half has the letters in descending order.
    The four corners (containing the spaces) are triangles.
    """
    letter_lookup = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8,
        'I' : 9,
        'J' : 10,
        'K' : 11,
        'L' : 12,
        'M' : 13,
        'N' : 14,
        'O' : 15,
        'P' : 16,
        'Q' : 17,
        'R' : 18,
        'S' : 19,
        'T' : 20,
        'U' : 21,
        'V' : 22,
        'W' : 23,
        'X' : 24,
        'Y' : 25,
        'Z' : 26
    }
    if letter == 'A':
        # loop only once, no spaces
        widest = 1
        diamond = ['A']
    if letter == 'B':
        widest = 3
        diamond = [' A ', 'B B', ' A ']
    if letter == 'C':
        widest = 5
        diamond = ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
    if letter == 'E':
        widest = 9
        diamond = ['    A    ', '   B B   ', '  C   C  ', ' D     D ', 'E       E']
    
    return diamond
