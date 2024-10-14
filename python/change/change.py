def find_fewest_coins(coins, target):
    
    all_returned_change = []
    all_returned_change_len = []
    
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if target < min(coins):
        raise ValueError("can't make target with given coins")
        
    # start at the end of the coins list
    coins_reversed = coins[::-1]
    
    # number of check loops
    coin_distinct_count = len(coins)

    while coin_distinct_count > 0:
        print(coin_distinct_count, all_returned_change)
        # reset the inputs
        input_value = target
        change = []

        for coin in coins_reversed:
            #ignore coin larger than input
            if coin <= input_value:
                #modulo - remainder of a division
                remaining_target = input_value % coin
                #divisor
                num_returned_coins = input_value // coin
                #append coin value divisor times
                counter = 0
                while counter < num_returned_coins:
                    change.append(coin)
                    counter +=1             
                input_value = input_value % coin
        # TODO: this is missing when total remainder at the end is NOT zero
        # successful result - if sum of change == target then there are no remainders - 
        returned_change = change[::-1]

        if returned_change in all_returned_change:
            pass
        else:
            if len(returned_change) > 0:
                all_returned_change.append(returned_change)
                all_returned_change_len.append(len(returned_change))

        coins_reversed.pop(0)
        coin_distinct_count -= 1

    print('all done', all_returned_change, all_returned_change_len)
    
    # this is the happy path
    optimum_change_index = all_returned_change_len.index(min(all_returned_change_len))
    
    print(all_returned_change, all_returned_change_len, optimum_change_index)
    result = all_returned_change[optimum_change_index]
    return result



"""
this works for one solution - from the first biggest coin less than target


def find_fewest_coins(coins, target):
    change = []
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        pass
    # start at the end of the coins list
    coins_reversed = coins[::-1]

    coin_distinct_count = len(coins)
    all_returned_change = []
    change = []
    all_returned_change_len = []
    
    #while coin_distinct_count > 0:
    for coin in coins_reversed:
        #ignore coin larger than target
        if coin <= target:
            #modulo - remainder of a division
            a = target % coin
            #divisor
            returned = target // coin
            #append coin value divisor times
            counter = 0
            while counter < returned:
                change.append(coin)
                counter +=1             
            target = target % coin
    returned_change = change[::-1]
    print(returned_change)
    all_returned_change.append(returned_change)
    all_returned_change_len.append(len(returned_change))
    print(all_returned_change, all_returned_change_len)
       
    
    return all_returned_change

"""