def recite(start, take=1):
    num_lookup = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 0:'no'}
    lyrics = []
    while start > 0:
        if take == 0:
            break
        remaining_bottles = start - 1
        #basic lyric - for 10,9,8,7,6,5,4,3 bottles
        beg = f'{num_lookup[start]} green bottles hanging on the wall,'
        mid = 'And if one green bottle should accidentally fall,'
        end = f'There\'ll be {num_lookup[remaining_bottles]} green bottles hanging on the wall.'
    
        #lyrics for 2 bottles - handle plural
        if start == 2:
            end = f'There\'ll be {num_lookup[remaining_bottles]} green bottle hanging on the wall.'
        #lyrics for 1 bottle - handle plural
        elif start == 1:
            beg = f'{num_lookup[start]} green bottle hanging on the wall,'
    
        lyrics.append(beg.capitalize())
        lyrics.append(beg.capitalize())
        lyrics.append(mid)
        lyrics.append(end)
        if take > 1:
            lyrics.append('')
        #reduce number of bottles, counter
        start -= 1
        take -= 1
    
    return lyrics