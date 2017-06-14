#!/usr/bin/env python3


def add_fruit(inventory, fruit, quantity=0):
    """
    Adds quantity of fruit to inventory with 0 if quantity not given.

      >>> new_inventory = {}
      >>> add_fruit(new_inventory, 'strawberries', 10)
      >>> 'strawberries' in new_inventory
      True
      >>> new_inventory['strawberries']
      10
      >>> add_fruit(new_inventory, 'apples')
      >>> new_inventory['apples']
      0
      >>> add_fruit(new_inventory, 'strawberries', 25)
      >>> new_inventory['strawberries']
      35
    """
    inventory[fruit] = inventory.get(fruit, 0) + quantity


def show_inventory(inventory):
    """
      >>> old_inventory = {'apples': 35, 'pears': 10, 'kiwis': 45}
      >>> show_inventory(old_inventory)
      'ITEM\\tQUANTITY\\napples\\t35\\nkiwis\\t45\\npears\\t10'
      >>> old_inventory['bananas'] = 10
      >>> show_inventory(old_inventory)
      'ITEM\\tQUANTITY\\napples\\t35\\nbananas\\t10\\nkiwis\\t45\\npears\\t10'
    """
    s = 'ITEM\tQUANTITY'
    for item in sorted(inventory):
        s += '\n{0}\t{1}'.format(item, inventory[item])
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
