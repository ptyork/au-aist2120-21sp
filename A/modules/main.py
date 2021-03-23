# print(f"MAIN.PY: {__name__}")

# import mathy
import mathy as ma

print("HERE IN MAIN")

# summation(20)    NO, not in "main" namespace

# val = mathy.summation(20)
val = ma.summation(20)
print(val)

# print(mathy.factorial(5))
print(ma.factorial(5))
