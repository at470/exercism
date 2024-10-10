def check_input(input_grid):
    if len(input_grid)%4 == 0:
        for row in input_grid:
            if len(row)%3 == 0:
                #checks have passed
                return True
            else:
                raise ValueError("Number of input columns is not a multiple of three")
    raise ValueError("Number of input lines is not a multiple of four")

def check_one_digit(input_grid):
    result = '?'
    # check for 3 x 4
    if check_input(input_grid):
        if input_grid == [" _ ", "| |", "|_|", "   "]:
            result = '0'
        elif input_grid == ["   ", "  |", "  |", "   "]:
            result = '1'
        elif input_grid == [" _ ", " _|", "|_ ", "   "]:
            result = '2'
        elif input_grid == [" _ ", " _|", " _|", "   "]:
            result = '3'
        elif input_grid == ["   ", "|_|", "  |", "   "]:
            result = '4'
        elif input_grid == [" _ ", "|_ ", " _|", "   "]:
            result = '5'
        elif input_grid == [" _ ", "|_ ", "|_|", "   "]:
            result = '6'
        elif input_grid == [" _ ", "  |", "  |", "   "]:
            result = '7'
        elif input_grid == [" _ ", "|_|", "|_|", "   "]:
            result = '8'
        elif input_grid == [" _ ", "|_|", " _|", "   "]:
            result = '9'
    return result

def split_string(s, chunk_size):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
    
def convert(input_grid):
    split_row = []
    for row in input_grid:
        split_row.append(split_string(row,3))
    print(split_row)
    return check_one_digit(input_grid)