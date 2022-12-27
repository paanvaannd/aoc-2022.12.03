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
elves_in_group: list = []

for line in range(len(data)):
    # Calculate badge priorities
    elves_in_group.append(set(data[line]))
    if len(elves_in_group) == 3:
        badge_priority += prioritize(elves_in_group[0] &
                                     elves_in_group[1] &
                                     elves_in_group[2])
        elves_in_group.clear()

    # Calculate item priorities
    line_length: int = len(data[line])
    separator: int = int(line_length / 2)
    compartment_1: set = set(data[line][:separator])
    compartment_2: set = set(data[line][separator:])
    dupes: set = set()
    if len(compartment_1 | compartment_2) != line_length:
        for item in compartment_1:
            if item in compartment_2:
                dupes.add(item)
        item_priority += prioritize(dupes)

print(f"\nThe sum of non-badge item priorities is {item_priority}.\n"
      f"The sum of badge priorities is {badge_priority}.\n")
