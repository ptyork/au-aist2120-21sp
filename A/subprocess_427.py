# SUB PROCESSES

import subprocess

phandle = subprocess.Popen("notepad")

# print(phandle.poll())
# phandle.kill()
# print(phandle.poll())

phandle.wait()

print("ALL DONE!!!")

# RUN ANOTHER PYTHON SCRIPT

phandle = subprocess.Popen(['python','soup_413.py'])
phandle.wait()

print("ALL DONE!!!")

# OPEN FILE IN DEFAULT APPLICATION

# phandle = subprocess.Popen(['start','','Gone with the Wind.jpg'], shell=True)
# phandle = subprocess.Popen(['start',r'Gone\ with\ the\ Wind.jpg'], shell=True)
# phandle = subprocess.Popen(['start',' '.join(['Gone", "with', 'the', 'Wind.jpg'])], shell=True)
# phandle = subprocess.Popen(['cmd', '/c', '"Gone with the Wind.jpg"'], shell=True)
# import os
# print(os.system('cmd /c "Gone with the Wind.jpg"'))
# phandle = subprocess.Popen(['start','','Gone%20with%20the%20Wind.jpg'], shell=True)
# phandle = subprocess.Popen('cmd /c "Gone with the Wind.jpg"')
# phandle = subprocess.Popen('mspaint "Gone with the Wind.jpg"') # FINALLY!!!!!!!!!

# GONNA HAVE TO FIGURE THE ABOVE OUT

# phandle = subprocess.Popen(['start','gwtw.jpg'], shell=True)
# phandle.wait()

print("ALL DONE!!!")
