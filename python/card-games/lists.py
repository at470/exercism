"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    for val in rounds:
        if val == number:
            return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)



def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    last_index = len(hand) - 1
    middle_index = len(hand) // 2

    median_of_hand = hand[middle_index]
    avg_first_and_last_card = (hand[0] + hand[last_index]) / 2
    calculated_avg = card_average(hand)

    return calculated_avg in (median_of_hand, avg_first_and_last_card)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_index_card_values = []
    odd_index_card_values = []
    for index, val in enumerate(hand):
        if index % 2 == 0:
            even_index_card_values.append(val)
        else:
            odd_index_card_values.append(val)
    return card_average(even_index_card_values) == card_average(odd_index_card_values)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_index = len(hand) - 1

    if hand[last_index] == 11:
        hand[last_index] = 22
    return hand
