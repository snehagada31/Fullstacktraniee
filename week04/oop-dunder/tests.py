from vector import Vector2D
from shapes import Circle, Rectangle


def test_vector():

    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)

    assert v1 + v2 == Vector2D(6, 8)

    print("Vector test passed")



def test_shapes():

    circle = Circle(5)
    rectangle = Rectangle(4,5)

    assert round(circle.area(),2) == 78.54
    assert rectangle.area() == 20

    print("Shape test passed")



if __name__ == "__main__":

    test_vector()
    test_shapes()