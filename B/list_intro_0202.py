# >>> []
# []
# >>> [2,4,6,8,10,12]
# [2, 4, 6, 8, 10, 12]
# >>> ar = [2,4,6,8,10,12]
# >>> print(ar)
# [2, 4, 6, 8, 10, 12]
# >>> ar
# [2, 4, 6, 8, 10, 12]
# >>> print(ar[3])
# 8
# >>> ar[3] = 18
# >>> ar
# [2, 4, 6, 18, 10, 12]
# >>> dir(ar)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> dir(ar)[10]
# '__getattribute__'
# >>> help(list.insert)
# Help on method_descriptor:

# insert(self, index, object, /)
#     Insert object before index.

# >>> help(list.append)
# Help on method_descriptor:

# append(self, object, /)
#     Append object to the end of the list.

# >>> ar.append(15)
# >>> ar
# [2, 4, 6, 18, 10, 12, 15]
# >>> ar.append('bob')
# >>> ar
# [2, 4, 6, 18, 10, 12, 15, 'bob']
# >>> help(list.pop)
# Help on method_descriptor:

# pop(self, index=-1, /)
#     Remove and return item at index (default last).

#     Raises IndexError if list is empty or index is out of range.

# >>> help(list.remove)
# Help on method_descriptor:

# remove(self, value, /)
#     Remove first occurrence of value.

#     Raises ValueError if the value is not present.

# >>> ar.pop()
# 'bob'
# >>> ar.pop(len(ar))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: pop index out of range
# >>> ar.pop(len(ar) - 1)
# 15
# >>> ar.append['tom','jerry']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'builtin_function_or_method' object is not subscriptable
# >>> ar.append(['tom','jerry'])
# >>> ar
# [2, 4, 6, 18, 10, 12, ['tom', 'jerry']]
# >>> ar[6]
# ['tom', 'jerry']
# >>> ar[6][1]
# 'jerry'
# >>> del ar[6][1]
# >>> ar
# [2, 4, 6, 18, 10, 12, ['tom']]
# >>> ar[6].pop()
# 'tom'
# >>> ar
# [2, 4, 6, 18, 10, 12, []]
# >>> ar[5].pop()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'pop'
# >

# >>> ar
# [2, 4, 6, 18, 10, 12, []]
# >>> ar.pop()
# []
# >>> ar
# [2, 4, 6, 18, 10, 12]
# >>> ar[len(ar) - 1]
# 12
# >>> ar[-1]
# 12
# >>> ar[-2]
# 10
# >>> ar[6]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> ar[-6]
# 2
# >>> ar[-7]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# SLICING!!!! ar[START:STOP:STEP]

# >>> ar[0:5]
# [2, 4, 6, 18, 10]
# >>> ar
# [2, 4, 6, 18, 10, 12]
# >>> ar[2:4]
# [6, 18]
# >>> ar[2:2]
# []
# >>> ar[2:3]
# [6]
# >>> ar[2]
# 6
# >>> ar[4:2]
# []
# >>> ar[4:-1]
# [10]
# >>> ar[4:1000]
# [10, 12]
# >>> ar[4:]
# [10, 12]
# >>> ar[0:3]
# [2, 4, 6]
# >>> ar[:3]
# [2, 4, 6]
# >>> ar[:]
# [2, 4, 6, 18, 10, 12]
# >>> ar2 = ar
# >>> ar2
# [2, 4, 6, 18, 10, 12]
# >>> name = "Paul"
# >>> name2 = name
# >>> # VALUE COPY
# >>> name2 = "Other"
# >>> print(name2)
# Other
# >>> print(name)
# Paul
# >>> ar2[1] = 3
# >>> print(ar2)
# [2, 3, 6, 18, 10, 12]
# >>> print(ar)
# [2, 3, 6, 18, 10, 12]
# >>> # REFERENCE COPY
# >>> # INSTEAD USE A VALUE COPY
# >>> ar2 = ar[:]
# >>>

# >>> name = 'Paul York'
# >>> name[5]
# 'Y'
# >>> list(name)
# ['P', 'a', 'u', 'l', ' ', 'Y', 'o', 'r', 'k']
# >>> fname = name[0:4]
# >>> print(fname)
# Paul
# >>> fname
# 'Paul'
# >>> name[:4]
# 'Paul'
# >>> lname = name[5:]
# >>> print(lname)
# York
# >>> name[5:9]
# 'York'
# >>> name[5:len(name)]
# 'York'
# >>> name[5:-1]
# 'Yor'
# >>> skipper = name[0:9:2]
# >>> print(skipper)
# Pu ok
# >>> skipper = name[0:9:-1]
# >>> print(skipper)

# >>> skipper = name[9:0:-1]
# >>> print(skipper)
# kroY lua
# >>> skipper = name[10:0:-1]
# >>> print(skipper)
# kroY lua
# >>> reverse = name[::-1]
# >>> print(reverse)
# kroY luaP
# >>>

# >>> name = 'Paul York'
# >>> name[5]
# 'Y'
# >>> list(name)
# ['P', 'a', 'u', 'l', ' ', 'Y', 'o', 'r', 'k']
# >>> fname = name[0:4]
# >>> print(fname)
# Paul
# >>> fname
# 'Paul'
# >>> name[:4]
# 'Paul'
# >>> lname = name[5:]
# >>> print(lname)
# York
# >>> name[5:9]
# 'York'
# >>> name[5:len(name)]
# 'York'
# >>> name[5:-1]
# 'Yor'
# >>> skipper = name[0:9:2]
# >>> print(skipper)
# Pu ok
# >>> skipper = name[0:9:-1]
# >>> print(skipper)

# >>> skipper = name[9:0:-1]
# >>> print(skipper)
# kroY lua
# >>> skipper = name[10:0:-1]
# >>> print(skipper)
# kroY lua
# >>> reverse = name[::-1]
# >>> print(reverse)
# kroY luaP
# >>>
# >>> name
# 'Paul York'
# >>> namelist = list(name)
# >>> namelist
# ['P', 'a', 'u', 'l', ' ', 'Y', 'o', 'r', 'k']
# >>> namelist[0] = 'S'
# >>> namelist
# ['S', 'a', 'u', 'l', ' ', 'Y', 'o', 'r', 'k']
# >>> name[0] = 'S'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# >>> # STRING IS IMMUTABLE (THOUGH LIST LIKE)
# >>> colors = ('red','yellow','blue')
# >>> colors
# ('red', 'yellow', 'blue')
# >>> altcolors = 'green','orange','purple'
# >>> altcolors
# ('green', 'orange', 'purple')
# >>> colors[1]
# 'yellow'
# >>> colors[::-1]
# ('blue', 'yellow', 'red')
# >>> dir(colors)
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
# >>> colors[1] = 'green'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> # TUPLE IS AN IMMUTABLE LIST LIKE STRUCTURE
# >>> tuple(name)
# ('P', 'a', 'u', 'l', ' ', 'Y', 'o', 'r', 'k')
# >>>
