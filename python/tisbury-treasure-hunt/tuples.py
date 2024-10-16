"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    
    :return: str - the extracted map coordinate.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return tuple(azara_record[1]) == rui_record[1]


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record):
        combined_record = azara_record + rui_record
    else:
        combined_record = 'not a match'
    return combined_record


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).

    (('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), 
    ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), 
    ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))
    """
    result_str = ''

    for outer_tuple in combined_record_group:
        result_list = []
        for i in outer_tuple:
            if len(i) == 2 and type(i) is str:
                pass
            else:
                result_list.append(i)
        result_str = result_str + str(tuple(result_list)) + '\n'
    return result_str
