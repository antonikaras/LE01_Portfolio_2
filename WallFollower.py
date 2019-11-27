#! /usr/bin/python3

import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Library CamJam library
import math

# Define the robot
robot = CamJamKitRobot()

# Define the Distance sensor
pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)
er = 0
WallDist = .2 

def sgn(n):
	
    if (n > 0):
        return 1
    elif (n < 0):
        return -1
    else: 
        return 0

def clp(n, mi, ma):
	
    if (n < mi):
        n = mi
	
    if (n > ma):
        n = ma
	
    return n

# PI controller for the wall follower
def Controller(dist, pr_er, max_sp):
    # Get the error
    er = WallDist - dist
    
    # Compute the new speed
    kp = 0.45
    ki = 0.015
    Nsp = kp * er + ki * (pr_er + er)

    # Find the new speed for each wheel
    left = max_sp  - Nsp
    right = max_sp + Nsp
	
    left = sgn(left) * clp(abs(left), 0.05, 0.95)		# clip speed between 0.05, 0.95
    right = sgn(right) * clp(abs(right), 0.05, 0.95)		# clip speed between 0.05, 0.95

    return left, right, er + pr_er
try:
    prev_dist = math.ceil(1000 * sensor.distance) / 1000
    # Repeat the next indented block forever
    while True:
        dist = math.ceil(1000 * sensor.distance) / 1000
        dist = math.ceil( 1000 * 0.5 * (dist + prev_dist)) / 1000
        prev_dist = dist
       	#movement = (sp, sp)
       	#if (dist > WallDist):
      	#    movement = (0.8 * sp, sp)
        #elif (dist < WallDist):
        #    movement = (sp, 0.8 * sp)
        left, right, er = Controller(dist, er, 0.5)
        robot.value = (right, left)
        print(dist, left, right, er)
        time.sleep(0.25)
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")
