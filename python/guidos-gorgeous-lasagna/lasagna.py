"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

PREPARATION_TIME_PER_LAYER_IN_MIN = 2
def preparation_time_in_minutes(num_layers):
    """Calculate preparation time.

    :param num_layers: int - number of layers in lasagna.
    :return: int - preparation time to prepare the lasagna before it goes in the oven (in minutes)

    Function that takes the number of layers in the lasagna to return the time (in minutes) required 
    to prep the lasagna.
    """
    prep_time_in_min = num_layers * PREPARATION_TIME_PER_LAYER_IN_MIN
    return prep_time_in_min

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate time.

    :param num_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - baking time in minutes already elapsed.
    :return: int - total time elapsed in preparing the lasagna (prep and bake so far) (in minutes)

    Function that takes the number of layers of the lasagna, uses preparation_time_in_minutes to calculate prep time
    and adds to elapsed baking time to return how long the lasagna has taken so far to make (in minutes).
    """
    elapsed_time_in_min = preparation_time_in_minutes(layers) + elapsed_bake_time
    return elapsed_time_in_min
