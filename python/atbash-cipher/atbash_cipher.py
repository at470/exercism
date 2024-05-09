def encode(plain_text):
    import re
    encoder = {
        'a' : 'z',
        'b' : 'y',
        'c' : 'x',
        'd' : 'w',
        'e' : 'v',
        'f' : 'u',
        'g' : 't',
        'h' : 's',
        'i' : 'r',
        'j' : 'q',
        'k' : 'p',
        'l' : 'o',
        'm' : 'n',
        'n' : 'm',
        'o' : 'l',
        'p' : 'k',
        'q' : 'j',
        'r' : 'i',
        's' : 'h',
        't' : 'g',
        'u' : 'f',
        'v' : 'e',
        'w' : 'd',
        'x' : 'c',
        'y' : 'b',
        'z' : 'a'
    }
    
    encoded_plain_text = ''
    for letter in plain_text:
        if re.match(r'[A-Za-z]', letter):
            encoded_plain_text = encoded_plain_text + encoder[letter.lower()]
        if re.match(r'[0-9]', letter):
            encoded_plain_text = encoded_plain_text + letter
    
    returned_string = ''
    # insert space at every sixth position
    for index, value in enumerate(encoded_plain_text):
        if index == 0:
            returned_string = returned_string + value
        elif index % 5 == 0:
            returned_string = returned_string + ' ' + value
        else:
            returned_string = returned_string + value

    return returned_string


def decode(ciphered_text):
    import re
    encoder = {
        'a' : 'z',
        'b' : 'y',
        'c' : 'x',
        'd' : 'w',
        'e' : 'v',
        'f' : 'u',
        'g' : 't',
        'h' : 's',
        'i' : 'r',
        'j' : 'q',
        'k' : 'p',
        'l' : 'o',
        'm' : 'n',
        'n' : 'm',
        'o' : 'l',
        'p' : 'k',
        'q' : 'j',
        'r' : 'i',
        's' : 'h',
        't' : 'g',
        'u' : 'f',
        'v' : 'e',
        'w' : 'd',
        'x' : 'c',
        'y' : 'b',
        'z' : 'a'
    }

    unciphered_text = ''

    for letter in ciphered_text:
        if re.match(r'[A-Za-z]', letter):
            unciphered_text = unciphered_text + encoder[letter.lower()]
        if re.match(r'[0-9]', letter):
            unciphered_text = unciphered_text + letter

    return unciphered_text
