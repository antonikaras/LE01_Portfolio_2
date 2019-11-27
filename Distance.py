#! /usr/bin/python3

import time  # Import the Time library
from gpiozero import DistanceSensor  # Import the GPIO Zero Library

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

print("Ultrasonic Measurement")

try:
    # Repeat the next indented block forever
    while True:
        print("Distance: %.3f cm\n" % sensor.distance * 10)
        time.sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")

