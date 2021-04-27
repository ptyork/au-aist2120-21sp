import time
import subprocess

proc = subprocess.Popen('notepad')
print(type(proc))

print(proc.poll())

# WAIT UNTIL DONE
# while proc.poll() == None:
#     # DO STUFF HERE
#     time.sleep(.1)

proc.wait()

print("DONE!!!")

script = subprocess.Popen(['python', "api_weather_0415.py", '30907'])

script.wait()

print("DONE AGAIN!!!!")

# proc = subprocess.Popen(['start','Gone.jpg'], shell=True)
proc = subprocess.Popen(['start','simple.csv'], shell=True)

proc.wait()

print("DONE FINALLY!!!")
