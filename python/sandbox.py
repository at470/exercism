# get user input for number, convert to int
number = int(input('number as integer '))
number_factor_list = []
check_num = 1

# check between 1 and number-1
while check_num in range(number):
    if number % check_num == 0:
        number_factor_list.append(check_num)
    check_num += 1
print(number_factor_list, sum(number_factor_list))