# WallFollower

## Description

  * Portfolio_2 For Linux on Embedded Objects
  * Raspberry pi zero is used as the micro processor and CamJam Edukit 3 as the components
  * A TCP server runs on Pizero and receives various command from a client regarding following
  a wall.
  
## Contect
  
  * Distance.service : Systemd service that launches a python file which uses the Ultrasonic 
                       sensor to mesasure the distance and then saves it into a .txt file.
  * DistanceService.py: The .py file that is excecuted while the Distance.service is running. 
  It measures the distance using an ultrasonic sensor and the saves it into dist.txt
  * MaxSpeed.txt : This file contains the maximum speed for the controller. The value can be
  a number between -0.9 and 0.9.
  * MotorSpeed.txt : The output of the PID controller for each motor is saved at MotorSpeed.txt
  * StopMotors.py : This file is used to stop the motors.
  * TargetDist.txt : The distance from the wall is saved at TargetDist.txt
  * WallFollower.service : Systemd service that launches a python file which uses the Ultrasonic
  sensor in order to maintain a constant distance from the wall.
  * WallFollower.sh : This file is excecuted everytime the TCP server receives a command.
  * WallFollowerService.py : This file is excecuted by the WallFollwer.service in order to follow
  the wall. It contains the PID contoller that computes the speed for each motor depending on the
  target distance from the wall and the distance measured from the Ultrasonic sensor.
  * dist.txt : This files contains the distance measured from the Ultrasonic sensor.
  
## Dependencies

  * gpiozero library in order to use the pins
 
## Commands
  * on : Starts the service that measures the distance from the Wall
  * off : Stops the service that measures the distance from the Wall
  *getdist : Read the .txt that contains the distance measured from the sensor and returns the value
  to the caller
  * getmotors: Returns the current value for each motor
  * start : Starts the wallFolling service that tries to follow the wall
  * stop : Stops the wallFolling service that tries to follow the wall
  * maxspeed : Return the current max speed for the controller
  * maxspeed # : Assigns the # as the max speed
  * walldist : Returns the current target distance from the wall
  * walldist # : Assigns the # as the target distance from the wall
  
