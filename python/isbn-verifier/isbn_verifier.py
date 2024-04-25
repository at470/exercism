import re
def is_valid(isbn):
    # remove hyphen
    no_hyphen_isbn_input = re.sub(r'-', '', isbn)
    is_isbn = False

    if len(no_hyphen_isbn_input) != 10:
        # raise ValueError("Not valid")
        return is_isbn
    
    elif re.match(r'([0-9]{10})|([0-9]{9}[Xx]{1}$)', no_hyphen_isbn_input):
        cleaned_string = re.match(r'([0-9]{10})|([0-9]{9}[Xx]{1}$)', no_hyphen_isbn_input)[0]
        counter = 10
        result = 0
        for index, num in enumerate(cleaned_string):
            if index == 9 and num == 'X':
                # something with 10
                print(10)
                result = int(result) + 10
            else:
                result = int(result) + counter * int(num)
                counter -= 1
        
        if result % 11 == 0:
            is_isbn = True
    
    return is_isbn