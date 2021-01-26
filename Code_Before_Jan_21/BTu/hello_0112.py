# COMMENT    NOT // (C#)
# C# had /*    Multi-line comment    */
'''
Python Multi-line comment

C#

using ...;

class Program
{
    public void Main(object args[])
    {
        THIS IS WHERE YOUR CODE GOES
    }
}
'''

print('hello')

'hello'   # string
"hello"   # ditto

'''
C#
string phrase;    // declaration
phrase = "Hello"; // assignment
'''
phrase = "Hello"

print(phrase)
print(type("HELLO"))
print(type(phrase))
print(phrase + " World")   # CONCATENATION

phrase = 42   # BAD!!!! Don't reuse variables, especially if changing type
print(type(phrase))

# print(phrase + " World")   # CONCATENATION  OOPS!!!!
str(42)  # "42"
str(phrase) # "42"
print(str(phrase) + " World")   # CONCATENATION


# floats -- have decimal
weight = 190.5
print(type(weight))

# bool -- True/False
is_cool = True
print(type(is_cool))
