import os
import shutil
from pathlib import Path

print(os.getcwd())

pyworkdir = Path('pywork')
print(pyworkdir)

if pyworkdir.exists() == False:
    # os.mkdir('pywork')
    os.mkdir(pyworkdir)
    print("Created pywork")

# os.chdir('pywork')
os.chdir(pyworkdir)
cwdpath = Path.cwd()
# Also Path.home() is quite useful
# print(os.getcwd())
print(cwdpath)

with open('frompython.txt', 'wt') as fi:
    fi.write("I'm a cool python prog")

d = Path.cwd()

ls = d.glob('*')
print(ls)
for fi in ls:
    print(fi)

os.chdir('..')

d = Path.cwd()
txtfiles = d.glob('*.txt')
for fi in txtfiles:
    print(f"copying {fi}")
    shutil.copy(fi, 'pywork')
