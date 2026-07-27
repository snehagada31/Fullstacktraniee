class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector2D(
            self.x + other.x,
            self.y + other.y
        )


    def __eq__(self, other):
        return (
            self.x == other.x and
            self.y == other.y
        )


    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"



if __name__ == "__main__":

    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)

    print("Vector Addition:")
    print(v1 + v2)

    print()

    print("Equality Check:")
    print(v1 == Vector2D(2, 3))