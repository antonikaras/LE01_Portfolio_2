#! /usr/bin/python3

from gpiozero import CamJamKitRobot, DistanceSensor  # Import the GPIO Zero Library CamJam library

# Define the robot
robot = CamJamKitRobot()

# Stop the motors
robot.value = (0, 0)
