"""
Assignment 2
Shallow Copy vs Deep Copy
"""

import copy

original = [
    [1, 2],
    [3, 4]
]

shallow_copy = copy.copy(original)

deep_copy = copy.deepcopy(original)

original[0].append(99)

print("===== Original =====")
print(original)

print("\n===== Shallow Copy =====")
print(shallow_copy)

print("\n===== Deep Copy =====")
print(deep_copy)