import re

def is_isogram(string):
    """
    An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
    """
    # non-letters matched and replaced with '', all in lowercase
    pattern = r'[^A-Za-z]+'
    cleaned_string = re.sub(pattern, '', string.lower())

    letter_dict = {}
    is_isogram = True
    
    for character in cleaned_string:
        if character in letter_dict.keys():
            is_isogram = False
            break
        else:
            letter_dict[character] = True

    return is_isogram
