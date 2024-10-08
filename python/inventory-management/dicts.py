"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    #set up initial dictionary
    inventory = {}
    for item in items:
        inventory[item] = 0

    #add count
    for item in items:
        inventory[item] = inventory[item] + 1
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    
    for item in items:
        if item in inventory.keys():
            inventory[item] = inventory[item] +1
        else:
            inventory[item] = 1
            
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    
    for item in items:
        if item in inventory.keys():
            inventory[item] = inventory[item] - 1
            if inventory[item] < 0:
                inventory[item] = 0            
    return inventory



def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory.keys():
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    item_list = []
    for item in inventory:
        print(item, inventory[item])
        if inventory[item] == 0:
            #skip over if item is 0
            pass
        else:
            item_inventory = (item, inventory[item])
            item_list.append(item_inventory)
    return item_list