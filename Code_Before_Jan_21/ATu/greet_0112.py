print('AWESOME GREETER')

# OPTION 1 (book way, not MY way)
print('What is your name')
name = input()

print("Oh, hello " + name)

# OPTION 2 (my way...also the right way for Mimir)
name = input('What is your name: ')

print("Oh, hello " + name)

print("-"*80)

age_str = input("How old are you: ")
age = int(age_str)
real_age = age*2
print("Yeah right. You are actually " + str(real_age))
