print(f"MAIN: {__name__}")


# import mathy
# from mathy import *
# from mathy import circle_area, pi
from mathy import circle_area
from mathy import pi as pie     # ALIAS A VARIABLE OR FUNCTION
import mathy as m               # ALIAS AN ENTIRE MODULE
import __main__  # THANKFULLY DOESN'T WORK

pi = 123

print("HELLO FROM MAIN.PY")

r = 15

# area = mathy.circle_area(r)
area = circle_area(r)

print(f"r = {r} ==> area = {area}")

print(pi,pie)
# print(mathy.pi)
