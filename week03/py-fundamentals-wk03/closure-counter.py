"""
Assignment 3
Closure-Based Counter
"""


def create_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print("===== Counter =====")

print(counter())
print(counter())
print(counter())
print(counter())