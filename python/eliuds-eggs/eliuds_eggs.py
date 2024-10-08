def egg_count(display_value):
    count = 0
    #display the value in binary format
    string = f'{display_value:b}'
    for i in string:
        if i == '1':
            count+=1
    return count