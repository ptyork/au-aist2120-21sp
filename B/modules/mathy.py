print(f"MATHY: {__name__}")

# print("HELLO FROM MATHY")

pi = 3.14159265

def circle_area(radius):
    '''
    Returns the area of a circle of a given radius.

    EXAMPLE USAGE:

    >>> circle_area(1)
    3.14159265
    >>> circle_area(0)
    0.0
    >>> circle_area(12.5)
    490.8738515625
    '''
    area = pi * (radius ** 2)
    return area


if __name__ == "__main__":
    # import sys

    # if len(sys.argv) == 1:
    #     # TEST IT
    #     print(circle_area(3))
    #     print(circle_area(5))
    #     print(pi)
    # elif len(sys.argv) == 2:
    #     # Assume an argument and run and print the function
    #     arg = sys.argv[1]
    #     num = float(arg)
    #     print(circle_area(num))
    # else:
    #     # ERROR
    #     print("BAD SYNTAX")

    # SUPER SIMPLE unit test framework
    print("TESTING 1..2..3")
    import doctest
    doctest.testmod()
