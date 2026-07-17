"""
Assignment 1
Mutable Default Argument Pitfall
"""


def add_item(item, items=[]):
    items.append(item)
    return items


print("===== Bug Demonstration =====")

print(add_item("Apple"))
print(add_item("Banana"))
print(add_item("Orange"))


print("\n===== Fixed Version =====")


def add_item_fixed(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item_fixed("Apple"))
print(add_item_fixed("Banana"))
print(add_item_fixed("Orange"))