def label(colors):
    # from parts 1 and 2
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
    
    # part 3
    colour_label_lookup = {
        'black' : ' ohms',
        'brown' : '0 ohms',
        'red' : '00 ohms',
        'orange' : ' kiloohms',
        'yellow' : '0 kiloohms',
        'green' : '00 kiloohms',
        'blue' : ' megaohms',
        'violet' : '0 megaohms',
        'grey' : '00 megaohms',
        'white' : ' gigaohms'
        }

    if colors[0] == 'black':
        value = colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]]
    elif colors[1] == 'black' and colors[2] == 'red':
        value = colour_number_lookup[colors[0]] + colour_label_lookup['orange']
    elif colors[1] == 'black' and colors[2] == 'green':
        value = colour_number_lookup[colors[0]] + colour_label_lookup['blue']
    elif colors[1] == 'black' and colors[2] == 'grey':
        value = colour_number_lookup[colors[0]] + colour_label_lookup['white']
    else:
        value = colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]]
    
    return value