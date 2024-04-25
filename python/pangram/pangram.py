import re

def is_pangram(sentence):
    # if len(sentence) == 0:
    # 	return False

    # elif len(sentence) > 0:
        #set variable with unique values from string sentence where all whitespaces and _ has been removed
        #unique_list = set(sentence.replace(" ", "").replace("_", ""))

    #replace all non alphabet characters with "" and create a set
    letters_only = re.sub("[^a-zA-Z]", "", sentence)

    lower_case_only = letters_only.lower()
    
    unique_list = set(lower_case_only)

    #returns the True/False value of condition and sets new variable contains_all_letters
    contains_all_letters = len(unique_list) == 26
    
    return contains_all_letters

