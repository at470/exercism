input_string = '[]]'

input_string_list = []
for char in input_string:
    input_string_list.append(char)

stack = []
bracket_pairs = {
    '(' : ')',
    ')' : '(',
    '{' : '}',
    '}' : '{',
    '[' : ']',
    ']' : '['
}

for index, char in enumerate(input_string_list):
    if char in ('{', '(', '['):
        stack.append(char)
    if char in ('}', ')', ']'):
        if len(stack) > 0 and bracket_pairs[char] == stack[-1]:
            stack.pop()
        else:
            break

if stack == []:
    print('all matching')
else:
    print('not matching')