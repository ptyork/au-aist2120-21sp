pi = 3.14159265

def circle_area(radius):
    area = pi * (radius ** 2)
    return area


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        # TEST IT
        print(circle_area(3))
        print(circle_area(5))
        print(pi)
    elif len(sys.argv) == 2:
        # Assume an argument and run and print the function
        arg = sys.argv[1]
        num = float(arg)
        print(circle_area(num))
    else:
        # ERROR
        print("BAD SYNTAX")
