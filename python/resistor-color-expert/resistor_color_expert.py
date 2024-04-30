def resistor_label(colors):
    """
    The program will take 1, 4, or 5 colors as input
    """

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

    # part 4
    colour_tolerance_lookup = {
        'grey' : '±0.05%',
        'violet' : '±0.1%',
        'blue' : '±0.25%',
        'green' : '±0.5%',
        'brown' : '±1%',
        'red' : '±2%',
        'gold' : '±5%',
        'silver' : '±10%'
    }

    # '7300 ohms' -> '7.3 kiloohms'
    # '12300 kiloohms' -> '12.3 megaohms'

    if len(colors) == 1:
        value = '0 ohms'

    
    # TODO
    # look up and get the big number
    # divide by 10 to get 10^x
    # get

    # four colours
    # orange-orange-brown-green would be 330 ohms with a ±0.5% tolerance
    if len(colors) == 4:
        tolerance = colour_tolerance_lookup[colors[3]]
        if colors[0] == 'black':
            value = colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]] + tolerance
        elif colors[1] == 'black' and colors[2] == 'red':
            value = colour_number_lookup[colors[0]] + colour_label_lookup['orange'] + tolerance
        elif colors[1] == 'black' and colors[2] == 'green':
            value = colour_number_lookup[colors[0]] + colour_label_lookup['blue'] + tolerance
        elif colors[1] == 'black' and colors[2] == 'grey':
            value = colour_number_lookup[colors[0]] + colour_label_lookup['white'] + tolerance
        else:
            value = colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]] + tolerance

    # five colours
    # orange-orange-orange-black-green would be 333 ohms with a ±0.5% tolerance.
    if len(colors) == 5:
        tolerance = colour_tolerance_lookup[colors[4]]
        if colors[0] == 'black' and colors[1] == 'black':
            value = colour_number_lookup[colors[2]] + colour_label_lookup[colors[3]] + tolerance
        if colors[0] == 'black':
            value = colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]] + colour_label_lookup[colors[3]] + tolerance
          
    return value

    # if colors[0] == 'black':
    #     value = colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]]
    # elif colors[1] == 'black' and colors[2] == 'red':
    #     value = colour_number_lookup[colors[0]] + colour_label_lookup['orange']
    # elif colors[1] == 'black' and colors[2] == 'green':
    #     value = colour_number_lookup[colors[0]] + colour_label_lookup['blue']
    # elif colors[1] == 'black' and colors[2] == 'grey':
    #     value = colour_number_lookup[colors[0]] + colour_label_lookup['white']
    # else:
    #     value = colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]]
    
