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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
