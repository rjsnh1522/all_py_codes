import itertools

# itertools.count
# Generates an infinite sequence of numbers.

counter = itertools.count(start=10, step=2)
for _ in range(5):
    print(next(counter))  # Output: 10, 12, 14, 16, 18


# itertools.cycle
# Cycles through an iterable infinitely.

cycle = itertools.cycle("ABC")
for _ in range(5):
    print(next(cycle))  # Output: A, B, C, A, B


# itertools.repeat
# Repeats a value infinitely or a specified number of times.

repeat = itertools.repeat(42, times=3)
for value in repeat:
    print(value)  # Output: 42, 42, 42


# itertools.combinations
# Generates all possible combinations of an iterable (order does not matter).

import itertools

combinations = itertools.combinations("ABC", r=2)
for item in combinations:
    print(item)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'C')

# itertools.chain
# Chains multiple iterables together.

import itertools

chain = itertools.chain("ABC", "DEF")
for item in chain:
    print(item)  # Output: A, B, C, D, E, F


# itertools.zip_longest
# Zips iterables, filling in missing values with a specified fill value.

import itertools

zip_longest = itertools.zip_longest("ABC", "DE", fillvalue="-")
for item in zip_longest:
    print(item)  # Output: ('A', 'D'), ('B', 'E'), ('C', '-')


# itertools.compress
# Filters elements from an iterable using a selector iterable.


import itertools

compress = itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 0])
for item in compress:
    print(item)  # Output: A, C, E

