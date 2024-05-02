# BINARY SEARCH
# # search_list = [1,2,3]
# search_list = [1]
# value = 3

# # sort the list
# search_list.sort()
# print(search_list)

# if len(search_list) == 0:
#     raise ValueError("value not in array")

# else:
#     # find the middle index - use quotient
#     middle_element_index = len(search_list) // 2
#     print(middle_element_index)
#     middle_element = search_list[middle_element_index]

#     if value == middle_element:
#         print('found it at index: ', middle_element_index)

#     elif value > middle_element:
#         print('value is greater than middle')
#         # search new list with elements right of middle element
#         new_list = search_list[middle_element_index+1:len(search_list)]
#         print(new_list)
#         # check again


#     elif value < middle_element:
#         print('value is less than middle')
#         new_list = search_list[0:middle_element_index-1]
#         print(new_list)
#         # check again

#     else:
#         raise ValueError("value not in array")


# question = 'What is 5?'
question = 'What is 5 plus 13?'
# question = 'What is 53 plus 2?'
import re

value = 0
if re.match(r'^[Ww]hat is \d+\?$', question):
    value = int(re.findall(r'[\d]+', question)[0]) #use findall(), convert to integer (string by default)
    print(value)

# Iteration 1 — Addition
# Handle large numbers and negative numbers.
elif re.match(r'^[Ww]hat is -{0,1}\d+ plus -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    for number in answer:
        value = value + int(number)
    # value = int(answer[0]) + int(answer[1])
    print(value)