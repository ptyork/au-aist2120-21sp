# NOT // is COMMENT
'''
This is also a comment.
It spans multiple lines.

C#
class Program
{
    public void Main(object[] args)
    {
        FINALLY CODE GOES HERE
    }
}

Python 
Just start a typin'

STRINGS start and end with EITHER a ' or a "
'''

print('hello')

# C#
# string name;
# name = "Paul";

name = 'Paul'    # VARIABLE ASSIGNMENT
# NOT statically typed, i.e., NO VARIABLE TYPE

print('hello + name') # bad
print('hello ' + name)   # CONCATENATION string merging

name = 42   # BAD IDEA don't reuse variables, ESPECIALLY if you change types
Name = 42
NAme = 42
NaMe = 42 # ALL DIFFERENT VARIABLES...case sensitive

print(name)
# print('Hello ' + name)
val = str(name)  # not needed, but val would be a string version of 42
print('Hello ' + str(name))   # can put the conversion inline

print(type('hello'))
print(type(42))
print(type(name))
print(type(str(name)))

weight = 180.7

print(weight)
print('my weight is ' + str(weight))
print(type(weight))

is_of_age = True
print(is_of_age)
print(type(is_of_age))

