def resistor_label(colors):
    """
    Assume colors list has len 1, 4, or 5
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
        'black' : '',
        'brown' : '0',
        'red' : '00',
        'orange' : '000',
        'yellow' : '0000',
        'green' : '00000',
        'blue' : ' 000000',
        'violet' : '0000000',
        'grey' : '00000000',
        'white' : '000000000'
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
        return '0 ohms'

    if len(colors) == 4:
        tolerance = colour_tolerance_lookup[colors[3]]
        label = colors[2]
        resistance_long = int(colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]] + colour_label_lookup[colors[2]])
    
    if len(colors) == 5:
        tolerance = colour_tolerance_lookup[colors[4]]
        label = colors[3]
        resistance_long = int(colour_number_lookup[colors[0]] + colour_number_lookup[colors[1]] + colour_number_lookup[colors[2]] + colour_label_lookup[colors[3]])

    if resistance_long < 10**3:
        label = ' ohms '
        resistance = resistance_long
    
    elif resistance_long >= 10**9:
        label = ' gigaohms '
        resistance = resistance_long / 10**9
    
    elif 10**3 <= resistance_long < 10**6:
        label = ' kiloohms '
        resistance = resistance_long / 10**3
    
    elif 10**6 <= resistance_long < 10**9:
        label = ' megaohms '
        resistance = resistance_long / 10**6

    # if integer, remove trailing decimal
    if float(resistance).is_integer():
        resistance = int(resistance)

    # convert to string for concat
    return str(resistance) + label + tolerance
   

colors = ['orange', 'orange', 'yellow', 'black', 'brown']
# colors = ["blue", "grey", "white", "brown", "brown"]
# colors = ["brown", "red", "orange", "green", "blue"]

print(resistor_label(colors))