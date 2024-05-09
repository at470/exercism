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
# question = 'What is 6 multiplied by 4?'

import re

a = re.findall(r'-{0,1}\d+ [plus]+[minus]+[multiplied\sby]+[divided\sby]+ -{0,1}\d+', question)

# Iteration 0 — Numbers
if re.match(r'^[Ww]hat is -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    value = int(answer[0]) #use findall(), convert to integer (string by default)

# Iteration 1 — Addition
# Handle large numbers and negative numbers.
elif re.match(r'^[Ww]hat is -{0,1}\d+ plus -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    value = int(answer[0]) + int(answer[1])

# Iteration 2 — Subtraction, Multiplication and Division
# A - Subtraction
elif re.match(r'^[Ww]hat is -{0,1}\d+ minus -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    value = int(answer[0]) - int(answer[1])

# B - Multiplication
elif re.match(r'^[Ww]hat is -{0,1}\d+ multiplied by -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    value = int(answer[0]) * int(answer[1])

# C - Division
elif re.match(r'^[Ww]hat is -{0,1}\d+ divided by -{0,1}\d+\?$', question):
    answer = re.findall(r'-{0,1}\d+', question)
    value = int(answer[0]) // int(answer[1])
else:
    raise ValueError("unknown operation")
    raise ValueError("syntax error")



# operation_match = '5 plus 13'

def find_operation(operation_match):
    # return re.findall(r'-{0,1}\d+\s(?:plus|minus|multiplied\sby|divided\sby)\s-{0,1}\d+', operation_match)
    if re.search(r'-{0,1}\d+ plus -{0,1}\d+', operation_match):
        value = 'plus'
    elif re.search(r'-{0,1}\d+ minus -{0,1}\d+', operation_match):
        value = 'minus'
    elif re.search(r'-{0,1}\d+ multiplied by -{0,1}\d+', operation_match):        
        value = 'multiply'
    elif re.search(r'-{0,1}\d+ divided by -{0,1}\d+', operation_match):
        value = 'divide'
    else:
        value = 'error'
    return value




example_list = [
    'what is 5?'
    , 'what is 19 plus 4?'
    , 'What is 7 minus 5?'
    , 'what is -5 plus 8?'
    , 'what is -5 plus -8?'
    , 'What is 5 plus 6?'
    , 'What is 5 plus 13 plus 6?'
    , 'What is 3 plus 2 multiplied by 3?'
    , 'What is 6 divided by 2?'
    , 'What is 5 multiplied by 10 divided by 25?'
]

output_words =[]
for example in example_list:
    # strip question mark
    example = example.replace('?', '')
    words_in_example_sentence = example.split(' ')
    output_words.append(words_in_example_sentence)
print(output_words)

pattern = r'(-{0,1}\d+)|(plus)|(minus)|(multiplied)|(divided)'
new =[]
for sentence in output_words:
    for word in sentence:
        print(word)
        if re.findall(pattern, word):
            numbers = re.findall(pattern, word)
            print(numbers)
            new.append(numbers[0])

print(new)

# bar = [['what', 'is', '5'], ['what', 'is', '19', 'plus', '4'], ['What', 'is', '7', 'minus', '5'], ['what', 'is', '-5', 'plus', '8'], ['what', 'is', '-5', 'plus', '-8'], ['What', 'is', '5', 'plus', '6'], ['What', 'is', '5', 'plus', '13', 'plus', '6'], ['What', 'is', '3', 'plus', '2', 'multiplied', 'by', '3'], ['What', 'is', '6', 'divided', 'by', '2'], ['What', 'is', '5', 'multiplied', 'by', '10', 'divided', 'by', '25']]


['5', 'multiplied', '10', 'divided', '25']

['5', 'multiplied', '10', 'divided', '25']