def translate(text):
    """
    Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
    
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
    
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
    """
    import re
    vowel_match = re.match(r'^([AaEeIiOoUu])|(Xr|XR|xr)|(YT|Yt|yt)', text)
    single_consonent_match = re.match(r'^([^AaEeIiOoUu])', text)
    double_consonent_match = re.match(r'^(CH|Ch|ch)|(SH|Sh|sh)|(TR|Tr|tr)|(TW|Tw|tw)', text)
    # print(vowel_match, vowel_match[0], vowel_match[1], vowel_match[2], vowel_match[3])
    # Rule 1: vowel sound
    if vowel_match:
        text = text + 'ay'
    # Rule 2: consonsant sound
    elif len(consonent_match[0]) == 1 and double_consonent_match is False:
        text = text[-len(text)-1:] + single_consonent_match[0] + 'ay'
    else:
        text = text[-trunc_text_index-1:] + double_consonent_match[0] + 'ay'
            # foo = re.match(r'^[^AaEeIiOoUu]', text).groups()
    return text
