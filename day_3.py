#!/usr/bin/env python

# Import built-in libraries
import string


def prioritize(x: list | set | tuple) -> int:
    _letters: tuple = tuple(string.ascii_letters)
    _points: tuple = tuple(n for n in range(1, len(_letters) + 1))
    _codec: dict = {}
    for key, value in zip(_letters, _points):
        _codec[key] = value

    _total_priority: int = 0
    for _item in x:
        _total_priority += _codec[_item]
    
    return _total_priority


with open("data.txt", "r") as file:
    data = file.read().splitlines()

badge_priority: int = 0
item_priority: int = 0
group_items: list = []

for line in data:
    # Calculate badge priorities
    group_items.append(set(line))
    if len(group_items) == 3:
        badge_priority += prioritize(group_items[0] &
                                     group_items[1] &
                                     group_items[2])
        group_items.clear()

    # Calculate item priorities
    line_length: int = len(line)
    separator: int = int(line_length / 2)
    compartment_1: set = set(line[:separator])
    compartment_2: set = set(line[separator:])
    dupes: set = set()
    if len(compartment_1 | compartment_2) != line_length:
        for item in compartment_1:
            if item in compartment_2:
                dupes.add(item)
        item_priority += prioritize(dupes)

print(f"\nThe sum of non-badge item priorities is {item_priority}.\n"
      f"The sum of badge priorities is {badge_priority}.\n")
