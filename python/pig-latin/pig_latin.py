def translate(text):
    """
    Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
    
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
    
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
    
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
    """
    import re
    vowel_match = re.match(r'^([AaEeIiOoUu])|(Xr|XR|xr)|(YT|Yt|yt)', text)
    single_consonant_match = re.match(r'^([^AaEeIiOoUu])', text)
    double_consonant_match = re.match(r'^(CH|Ch|ch)|(SH|Sh|sh)|(TR|Tr|tr)|(TW|Tw|tw)|(FR|Fr|fr)|(QU|Qu|qu)|(TH|Th|th)|(BR|Br|br)', text)
    triple_consonant_match = re.match(r'^(SQU|SQu|Squ|squ)|(STR|STr|Str|str)|(SHR|SHr|Shr|shr)|(SCH|SCh|Sch|sch)|(THR|THr|Thr|thr)', text)
    slice_loc_single_char = -(len(text)-1)
    slice_loc_double_char = -(len(text)-2)
    slice_loc_triple_char = -(len(text)-3)
    # Rule 1: vowel sound
    if vowel_match:
        text = text + 'ay'
    # Rule 2: consonant sound
    elif single_consonant_match:
        print('condition 3 is running')
        print(type(single_consonant_match), type(double_consonant_match), type(triple_consonant_match))
        # two letter word starting with consonant, ending with y
        if len(text) == 2 and text[-1:] == 'y':
            text = text[-1:] + single_consonant_match[0] + 'ay'
        elif bool(triple_consonant_match) is False:
            if bool(double_consonant_match) is False:
                print('only single char')
                print(text[slice_loc_single_char:])
                text = text[slice_loc_single_char:] + single_consonant_match[0] + 'ay'
            else:
                print('double char only')
                print(text[slice_loc_double_char:])
                print(double_consonant_match[0])
                text = text[slice_loc_double_char:] + double_consonant_match[0] + 'ay'
        else:
            print('triple char')
            print(text[slice_loc_triple_char:])
            print(bool(single_consonant_match))
            print(triple_consonant_match[0]) 
            text = text[slice_loc_triple_char:] + triple_consonant_match[0] + 'ay'
    else:
        print('hello')
    return text
