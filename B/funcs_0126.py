# C#
#    public int GetSum(int num1, int num2) { ...; return sum; }
#    GetSum(5,4);
#    int sum = GetSum(5,4);

# Python convention is to define funcitons at the top of a script

# greet()    NOOOOO, can't call before defining (usually)

def greet():    # function definition
    print("HELLO THERE")

def greetMe(name):
    print("HELLO " + name)

def getSum(num1, num2):
    # DEFENSIVE CODING
    # if type(num1) != int:
    #     print("num1 is a bad value")
    # elif type(num2) != int:
    #     print("num2 is a bad value")
    # else:
    #     sum = num1 + num2
    #     return sum
    if type(num1) != int:
        print("num1 is a bad value")
        return
    if type(num2) != int:
        print("num2 is a bad value")
        return

    sum = num1 + num2
    return sum

def countTo(max):
    for num in range(1, (max + 1)):
        # print("Number " + str(num))
        # print("Number", num)
        print(f"Number {num}")
                      # in Python, an f-string is an interpolated string
                      # same as $"" in C#


greet()
greet()
greet()
greet()

print(greet)
print(type(greet))

# greet = "HELLO"
# greet()

# print = "JOE"
# print("JOE")

# greetMe()     gotta pass an argument
greetMe("UGA")
name = "Buzz"
greetMe(name)

sum = getSum(3,4)
if sum != None:
    print(sum)

sum = getSum("THREE","FOUR")
if sum != None:
    print(sum)

sum = getSum("THREE",4)
if sum != None:
    print(sum)

countTo(5)
countTo(15)

#############################################################

y = 10    # global scope

def scopeIt():
    # y from global scope is read only
    y = 15
    x = 5 # function scope
    print(x)
    print(y)

subtotal = 0

def addItem(cost):
    global subtotal
    # subtotal = 0
    subtotal += cost

scopeIt()
print(y)
# print(x)    OUT OF SCOPE (x is in function scope)

addItem(5)
addItem(10)
addItem(15)
print(subtotal)
