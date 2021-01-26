# SINGLE LINE COMMENT    C# ==>  //
'''
MULTI-LINE COMMENT     C# ==> /*    STUFF   */

C#
using System;
using ....;

class Program
{
    public void Main(string args[])
    {
        // CODE GOES HERE --> ENTRY POINT
        Consloe.Writeline("HELLO");
    }
}
'''

print("HELLO")

"STRING"
'string'
'''
string
'''

'''
C#
string name;    // DECLARATION
name = "Paul";  // ASSIGNMENT
'''

# name = None
name = "Paul"     # string
print(name)
print(type(name))

name = 42       # int  (BADDDDD. Don't reuse variables for other purposes])
print(name)
print(type(name))

weight = 172.6   # float
print(weight)
print(type(weight))

is_overweight = False   # bool (proper case for values)
print(is_overweight)
print(type(is_overweight))

name = "Paul"

print(name + " weighs " + str(weight) + " pounds")
