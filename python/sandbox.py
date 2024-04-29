def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    last_index = len(hand) - 1
    middle_index = len(hand) // 2 + 1

    median_of_hand = hand[middle_index]
    avg_first_and_last_card = (hand[0] + hand[last_index])/2
    calculated_avg = card_average(hand)

    return median_of_hand == calculated_avg or avg_first_and_last_card == calculated_avg