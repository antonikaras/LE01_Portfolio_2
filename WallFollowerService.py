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
er_sum = 0
WallDist = .2
delay = .01
avg_dist = 0
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

# PID controller for the wall follower
def ControllerPID(dist,er_sum, pr_er, max_sp):
    # Get the error
    er = WallDist - dist
    er_sum = er_sum + er

    # Compute the new speed
    # 1.2 0.16 0.22
    # 0.39 0.002 0.015
    kp = 1.5
    ki = 0.3
    kd = 0.6

    Nsp = kp * er + ki * er_sum * delay + kd * (er - pr_er) / delay

    # Find the new speed for each wheel
    left = max_sp  + Nsp
    right = max_sp - Nsp

    left = sgn(max_sp) * clp(abs(left), 0.05, 0.95)               # clip speed between 0.05 and 0.95
    right = sgn(max_sp) * clp(abs(right), 0.05, 0.95)             # clip speed between 0.05 and 0.95

    return left, right, er_sum, er

try:
    prev_dist = int(100 * sensor.distance) / 100

    cnt = 0
    # Repeat the next indented block forever
    while True:
        dist = int(100 * sensor.distance) / 100
        dist = int( 100 * 0.5 * (dist + prev_dist)) / 100
        # Read the target distance from the .txt file
        fl = open('/home/pi/LEO1_portfolio_2/TargetDist.txt', 'r')
        WallDist = float(fl.readline())
        fl.close()

        avg_dist = avg_dist + dist
        cnt = cnt + 1
        prev_dist = dist
        
        fl = open('/home/pi/LEO1_portfolio_2/MaxSpeed.txt', 'r')
        MaxSpeed = float(fl.readline())
        fl.close()
        if (MaxSpeed != 0):
            left, right, er_sum, er = ControllerPID(dist, er_sum, er, MaxSpeed)
        else:
            left = 0
            right = 0
        robot.value = (left, right)
        print(dist, left, right, er_sum, er, avg_dist / cnt)
        # Save the motor values in a .txt file
        fl = open("/home/pi/LEO1_portfolio_2/MotorSpeed.txt", 'w')
        fl.write(str(left) + " " + str(right))
        fl.close()
        fl = open("/home/pi/LEO1_portfolio_2/dist.txt", 'w')
        fl.write(str(dist))
        fl.close()
        time.sleep(delay)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")

