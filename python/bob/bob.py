def is_bob_asked_a_question(said_to_bob):
    """
    This should be true if:
    * said_to_bob ends with ? followed by zero or more whitespaces at end of string
    """
    import re
    return len(re.findall(r'\?[\s]*$', said_to_bob)) > 0

def is_bob_shouted_at(said_to_bob):
    return said_to_bob.isupper()

def is_bob_responding_to_silence(said_to_bob):
    """
    This should be true if:
    * said_to_bob is (some series of) whitespace character(s) only
    """
    import re
    bob_got_silence = False
    if said_to_bob is '':
        bob_got_silence = True
    elif said_to_bob.isspace() is True:
        bob_got_silence = True  
    return bob_got_silence

def response(hey_bob):
    
    """
    Bob only ever answers one of five things:
    "Sure." This is his response if you ask him a question, such as "How are you?" 
    The convention used for questions is that it ends with a question mark.
    "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used 
    for yelling is ALL CAPITAL LETTERS.
    "Calm down, I know what I'm doing!" This is what he says if you yell a question 
    at him.
    "Fine. Be that way!" This is how he responds to silence. The convention used 
    for silence is nothing, or various combinations of whitespace characters.
    "Whatever." This is what he answers to anything else.
    """
    
    bob_response = None
    if is_bob_asked_a_question(hey_bob) is True and is_bob_shouted_at(hey_bob) is True:
        bob_response = 'Calm down, I know what I\'m doing!'
    elif is_bob_asked_a_question(hey_bob) is True:
        bob_response = 'Sure.'
    elif is_bob_shouted_at(hey_bob) is True:
        bob_response = 'Whoa, chill out!'
    elif is_bob_responding_to_silence(hey_bob) is True:
        bob_response = 'Fine. Be that way!'
    else:
        bob_response = 'Whatever.' 
    return bob_response