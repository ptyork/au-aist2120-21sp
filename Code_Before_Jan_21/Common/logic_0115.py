'''
True ==> Yes
False ==> No

>>> 5 == 6
False
>>> 5 != 6
True
>>> 5 > 6
False
>>> 5 < 6
True
>>> 5 == 6 or 5 > 6
False
>>> 5 >= 6
False
>>> 5 == 6 or 5 < 6
True
>>> 5 <= 6
True
>>> 5 < 6 and 5 > 3
True
>>> 5 > 6 and 5 < 12
False
>>> not 5 == 6
True
>>> not 5 > 6  # 5 <= 6
True

'''


'''
C#
int x;
x = 3;
if (x > 0)
{
    Console.Writeline("It's positive!!");
}
'''

# Single Branch
x = -3
if x > 0:
    print("It's positive")
print("It'm done")


# Two Branch
age = 16
if age >= 14 and age <= 18:
    print("Whud up, high school")
else:
    print("Howdy baby boomer")


'''
C#
if (x > 5)
{

}
else 
{
    if (x > 0)
    {

    }
    else
    {

    }
}
'''

# Multi Branch
age = 17
print("I see you're " + str(age))
print("I see you're", age)
if age >= 14 and age <= 18:
    print("Stick around, high school")
    if age >= 14 and age < 16:
        print("Go left")
    else:
        print("Go right")
elif age < 14:
    print("Go home baby")
else:
    print("Go home boomer")



'''
C#
while (generic)
do/while (generic)
for (counter controlled repitition)
foreach (enumeration)

int x = 5;
while (x > 0)
{
    do something
    x = x - 1;
}

int x = 0;
while (x < 5)
{
    do something
    x++;
}

for (int x = 0; x < 5; x++)
{
    do something
}

string[] strs = ["Hello", "World"];
for (int i = 0; i < strs.lenght; i++)
{
    string val = strs[i];
    Console.Writeline(val);
}

foreach (string val in strs)
{
    Console.Writeline(val);
}

'''

'''
Python:

while (generic)
for (enumeration)
'''
