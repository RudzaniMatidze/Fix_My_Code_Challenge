#!/usr/bin/python3
"""
A script that calculates a square
"""


class square():
    """Sqaure class"""
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """inititalizing the square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String Rep of the square instance"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """creating an instance"""

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
