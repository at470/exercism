def find(search_list, value):
    """
    The algorithm looks like this:

    Find the middle element of a sorted list and compare it with the item we're looking for.
    If the middle element is our item, then we're done!
    If the middle element is greater than our item, we can eliminate that element and all the elements after it.
    If the middle element is less than our item, we can eliminate that element and all the elements before it.
    If every element of the list has been eliminated then the item is not in the list.
    Otherwise, repeat the process on the part of the list that has not been eliminated.

    """

    # check that value is bigger than the middle element:
    if is_value_equal_to_middle_element(search_list, value):
        return middle_element_index
    
    # first sort the list
    search_list.sort()


    if len(search_list) > 0:
        if is_value_equal_to_middle_element(search_list, value)[0]:
            return is_value_equal_to_middle_element(search_list, value)[1]
        
        else:
            if value > search_list[middle_element_index]:
                # TODO: create new list with elements to right of middle element

    else:
        raise ValueError("value not in array")

def is_value_equal_to_middle_element(search_list, value):
    # first sort the list
    search_list.sort()

    # assume that search_list is not empty
    middle_element_index = int((len(search_list) - 1) / 2)

    if value == search_list[middle_element_index]:
        return [True, middle_element_index]






"""

Let's say we're looking for the number 23 in the following sorted list: [4, 8, 12, 16, 23, 28, 32].

We start by comparing 23 with the middle element, 16.
Since 23 is greater than 16, we can eliminate the left half of the list, leaving us with [23, 28, 32].
We then compare 23 with the new middle element, 28.
Since 23 is less than 28, we can eliminate the right half of the list: [23].
We've found our item.

"""