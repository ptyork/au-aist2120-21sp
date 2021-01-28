#functions

# By convention, functions are definted at the top
# of the script.

# greet()    # CANNOT CALL BEFORE DEFINING

def greet():
    print("Hello there")


def greet2(name):
    print("Hello " + name)


def getSum(num1, num2):
    # DEFENSIVE CODING (good but I'm gonn just skip it from now on)
    if type(num1) != int:
        print("num1 is BAD")
        return
    if type(num2) != int:
        print("num2 is BAD")
        return
    sum = num1 + num2
    return sum


def count(max):
    for num in range(1,(max + 1)):
        # print("Number " + str(num))
        # print("Number", num)
        print(f"Number {num}")  # string interpolation of "f-string"



print(type(greet))
greet()

# greet = "Hello"
# greet()   # DO NOT REASSIGN YOUR FUNCTION NAMES TO VARIABLES
#  BECAUSE FUNCTIONS ARE VARIABLES

# print = 2     # BAAAAAAAD
# print("HELLO") 

greet2("Paul")
name = "Old Yeller"
greet2(name)


answer = getSum(2,5)
if answer != None:
    print(answer)
# x = print(answer)
# print(x)

answer = getSum("one","two")
if answer != None:
    print(answer)

answer = getSum("one",2)
if answer != None:
    print(answer)


count(5)
count(10)
count(20)


#####################################################################

xx = 1
def plusplus():
    global xx
    xx = xx + 1
    print(xx)

print(xx)
plusplus()
print(xx)
plusplus()
print(xx)



########################################################


def p(text):
    print("<p>")
    print(f"  {text}")
    print("</p>")

def h1(text):
    print("<h1>")
    print(f"  {text}")
    print("  ", end="")
    img("awesome.jpg")
    print("</h1>")

def img(src):
    print(f'<img src="{src}" />')

h1("PAUL IS GREAT")
p("HELLO")
img("paul.gif")

