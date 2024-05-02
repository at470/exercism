
# search_list = [1,2,3]
search_list = [1]
value = 3

# sort the list
search_list.sort()
print(search_list)

if len(search_list) == 0:
    raise ValueError("value not in array")

else:
    # find the middle index - use quotient
    middle_element_index = len(search_list) // 2
    print(middle_element_index)
    middle_element = search_list[middle_element_index]

    if value == middle_element:
        print('found it at index: ', middle_element_index)

    elif value > middle_element:
        print('value is greater than middle')
        # search new list with elements right of middle element
        new_list = search_list[middle_element_index+1:len(search_list)]
        print(new_list)
        # check again


    elif value < middle_element:
        print('value is less than middle')
        new_list = search_list[0:middle_element_index-1]
        print(new_list)
        # check again

    else:
        raise ValueError("value not in array")