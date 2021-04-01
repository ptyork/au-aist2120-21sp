import os
from pathlib import Path
import shutil

# CREATE A NEW DIRECTORY
# first check if it exists
newdir = Path('./pywork')
if newdir.exists() == False:
    # if not, safe to create it
    os.mkdir('./pywork')

# SHOW current working directory
print(os.getcwd())

# CHANGE current working directory (ONLY changes for script, NOT for the command prompt)
os.chdir('pywork')
print(os.getcwd())

# Work with a "special" path object
#  (current...also Path.home() for home directory)
cpath = Path.cwd()

# Git a list of ALL files
#   * is a wildcard
files = cpath.glob('*')

# A "GENERATOR" is an object used in a for loop...basically CAN BECOME a list
print(files)

# Iterate over the "generator" (just like a list)
#  (will be empty the first time you run this since you just created the directory)
for fi in files:
    print(fi)

# Just some code to get back to the parent (starting in this case) directory
os.chdir('..')
print(os.getcwd())
cpath = Path.cwd()

# Print all files there...will actually have some
files = cpath.glob('*')
for fi in files:
    print(fi)

# Show (and copy) all TXT files to the new directory we just created
files = cpath.glob('*.txt')
for fi in files:
    print(fi)
    # I wanna copy these to pywork
    shutil.copy(fi, 'pywork')


