# the untidy version!

def initialise_gift_variable(start_verse):
    gift_dict = {1 : 'and a Partridge in a Pear Tree',
                2 : 'two Turtle Doves, ',
                3 : 'three French Hens, ',
                4 : 'four Calling Birds, ',
                5 : 'five Gold Rings, ',
                6 : 'six Geese-a-Laying, ',
                7 : 'seven Swans-a-Swimming, ', 
                8 : 'eight Maids-a-Milking, ',
                9 : 'nine Ladies Dancing, ',
                10 : 'ten Lords-a-Leaping, ',
                11 : 'eleven Pipers Piping, ',
                12 : 'twelve Drummers Drumming, '}
    # construct initial list of gifts
    gifts_list_string = ''
    loop_counter = 1
    while loop_counter <= start_verse:
        gifts_list_string = gift_dict[loop_counter] + gifts_list_string
        loop_counter += 1
    return gifts_list_string

def recite(start_verse, end_verse):
    returned_lyrics = []
    verse_dict = {1 : 'first',
                 2 : 'second',
                 3 : 'third',
                 4 : 'fourth',
                 5 : 'fifth',
                 6 : 'sixth',
                 7 : 'seventh',
                 8 : 'eighth',
                 9 : 'ninth',
                  10 : 'tenth',
                  11 : 'eleventh',
                  12 : 'twelfth'}
    
    gift_dict = {1 : 'and a Partridge in a Pear Tree',
                2 : 'two Turtle Doves, ',
                3 : 'three French Hens, ',
                4 : 'four Calling Birds, ',
                5 : 'five Gold Rings, ',
                6 : 'six Geese-a-Laying, ',
                7 : 'seven Swans-a-Swimming, ', 
                8 : 'eight Maids-a-Milking, ',
                9 : 'nine Ladies Dancing, ',
                10 : 'ten Lords-a-Leaping, ',
                11 : 'eleven Pipers Piping, ',
                12 : 'twelve Drummers Drumming, '}
    
    first_verse_only = f'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.'

    # initialise list of gifts
    list_of_gifts = initialise_gift_variable(start_verse)
    
    # first verse only
    if start_verse == 1 and end_verse == 1:
        verse = first_verse_only
        returned_lyrics.append(verse)
    # when returning one verse only, not first verse
    elif start_verse - end_verse == 0:
    # construct initial value of gifts
        list_of_gifts = initialise_gift_variable(start_verse)
        verse = f'On the {verse_dict[start_verse]} day of Christmas my true love gave to me: {list_of_gifts}.'
        returned_lyrics.append(verse)
    # multiple verses, *not* starting first verse
    elif start_verse > 1:
        counter = start_verse
        while counter <= end_verse:
            verse = f'On the {verse_dict[counter]} day of Christmas my true love gave to me: {list_of_gifts}.'
            returned_lyrics.append(verse)
            counter += 1
            # increment list of gifts for next time
            list_of_gifts = gift_dict[counter] + list_of_gifts
    
    else:
        if start_verse == 1:
            verse = first_verse_only
            returned_lyrics.append(verse)

        loop_count = 2
        list_of_gifts_from_second_verse = initialise_gift_variable(2)

        while loop_count <= end_verse:
            verse = f'On the {verse_dict[loop_count]} day of Christmas my true love gave to me: {list_of_gifts_from_second_verse}.'
            returned_lyrics.append(verse)
            loop_count += 1
            # increment list of gifts for next time
            if loop_count > end_verse:
                pass
            else:
                list_of_gifts_from_second_verse = gift_dict[loop_count] + list_of_gifts_from_second_verse
    return returned_lyrics
