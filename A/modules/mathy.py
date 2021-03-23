print(f"MATHY.PY: {__name__}")


def summation(n):
    # sum = 0
    # for i in range(1,n+1):
    #     sum += i
    # return sum
    return sumrange(1,n)

def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def sumrange(m,n):
    sum = 0
    for i in range(m,n+1):
        sum += i
    return sum



if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        # assume test code
        print("HERE IN MATHY")
        print(summation(5))
        print(summation(10))
    elif len(sys.argv) == 2:
        # assume RUN it
        arg = sys.argv[1]
        num = int(arg)
        print(summation(num))
    else:
        # assume idiot
        print("BAD JOB")
