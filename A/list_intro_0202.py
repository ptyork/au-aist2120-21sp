# >>> []
# []
# >>> l = [5,10,15]
# >>> print(l)
# [5, 10, 15]
# >>> print(l[0])
# 5
# >>> print(l[2])
# 15
# >>> print(l[3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> l[1] = 11
# >>> print(l)
# [5, 11, 15]
# >>> dir(l)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> dir(l)[10]
# '__getattribute__'
# >>> help(list.extend)
# Help on method_descriptor:

# extend(self, iterable, /)
#     Extend list by appending elements from the iterable.

# >>> l.append(25)
# >>> print(l)
# [5, 11, 15, 25]
# >>> print(l[3])
# 25
# >>> l.append('big bird')
# >>> print(l)
# [5, 11, 15, 25, 'big bird']
# >>> l.append(['a','b','c'])
# >>> l
# [5, 11, 15, 25, 'big bird', ['a', 'b', 'c']]
# >>> print(l[5])
# ['a', 'b', 'c']
# >>> print(l[5][1])
# b
# >>> help(list.remove)
# Help on method_descriptor:

# remove(self, value, /)
#     Remove first occurrence of value.

#     Raises ValueError if the value is not present.

# >>> help(list.pop)
# Help on method_descriptor:

# pop(self, index=-1, /)
#     Remove and return item at index (default last).

#     Raises IndexError if list is empty or index is out of range.

# >>> l.pop()
# ['a', 'b', 'c']
# >>> print(l)
# [5, 11, 15, 25, 'big bird']>

# >>> nums = [2,4,6,8,10,12]
# >>> nums[5]
# 12
# >>> nums[-1]
# 12
# >>> nums[-2]
# 10
# >>> nums[-6]
# 2
# >>> nums[-7]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> len(nums)
# 6
# >>> nums[len(nums) - 1]
# 12
# >>> nums[0:2]   # a slice
# [2, 4]
# >>>

##############################################


nums = [2,4,6,8,10,12]
# SLICING  REMEMBER SECOND (END) VALUE IS EXCLUSIVE!!!!!
# list[START,END,STEP]

print(nums[0:3])    # [2,4,6]
print(nums[2:4])    # [6,8]
print(nums[-3:-1])  # [8,10]
print(nums[1:1])    # [4] or [] ???  >> []
print(nums[5:1])    # []
print(nums[5:1:-1]) # [12,10,8,6]
print(nums[-1:1:-1]) # [12,10,8,6]
print(nums[:1:-1]) # [12,10,8,6]
print(nums[:1:1])  # [2]
print(nums[:5:2])  # [2,6,10]   > INDICES 0,2,4

name = 'Paul York'

# A STRING IS AN IMMUTABLE COLLECTION OF CHARACTERS
print(name[2])  # u

# OH BY THE WAY
name_list = list(name)
print(name_list)

print(name[:4])   # start 0 go to 3
print(name[5:9])  # start 5 go to 8
print(name[5:-1]) # start 5 go to 7
print(name[5:])   # start 5 go to END (8)
print(name[:])    # full copy
name2 = name      # VALUE COPY
print(name2)
name2 = "Dufus"
print(name2)      # Dufus
print(name)       # Paul York

nums2 = nums      # REFERENCE COPY
print(nums2)
nums2[1] = 3
print(nums2)
print(nums)

nums3 = nums[:]   # VALUE COPY
print(nums3)
nums3[0] = 1
print(nums3)
print(nums)


print(name[::-1])    # kroY luaP   (REVERSE)

# name[0] = 'S'     NOOOOOO IT IS IMMUTABLE
# print(name)

# A TUPLE IS AN IMMUTABLE COLLECTION OF ANYTHING 
# (in other words a read only list)

pri_colors = ('red','yellow','blue')    # Paren start and end indicate TUPLE
print(pri_colors)
print(pri_colors[1])

# pri_colors[1] = 'green'     NOOOOOO IT IS READ ONLY --- IMMUTABLE
