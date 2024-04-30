def value(colors):
    colour_number_lookup = {
        'black' : '0',
        'brown' : '1',
        'red' : '2',
        'orange' : '3',
        'yellow' : '4',
        'green' : '5',
        'blue' : '6',
        'violet' : '7',
        'grey' : '8',
        'white' : '9'
        }
    
    # only take the first two values of colors
    value = int(colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]])
    
    return value