#! /usr/bin/python3

import time  # Import the Time library
from gpiozero import DistanceSensor  # Import the GPIO Zero Library
import math
# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

path = '/home/pi/LEO1_portfolio_2/dist.txt'

try:
    # Repeat the next indented block forever
    while True:
        dist = math.ceil(1000 * sensor.distance) / 1000
        #print(dist)
        fl = open(path, 'w')
        fl.write(str(dist))
        fl.close()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")

