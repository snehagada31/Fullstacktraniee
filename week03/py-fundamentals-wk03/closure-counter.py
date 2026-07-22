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

def greet(required_arg, *args, **kwargs):
    print(required_arg)
    print(*args, **kwargs)
greet("Hello, World!", 1, 2, 3, 4, name="sneha", age=22)