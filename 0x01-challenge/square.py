#!/usr/bin/python3

class Square:
    """
    Class representing a Square

    Attributes:
    - width: width of the square
    - height: height of the square
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the square with given width and height.

        Args:
        - width: width of the square
        - height: height of the square
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculates and returns the area of the square.

        Returns:
        Area of the square
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
        Perimeter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Example usage
    s = Square(width=12, height=9)
    print("Square:", s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
