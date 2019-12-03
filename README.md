# WallFollower

## Description

  * Portfolio_2 For Linux on Embedded Objects - Group 10
  * Raspberry pi zero is used as the micro processor and CamJam Edukit 3 as the components
  * A TCP server runs on Pizero and receives various command from a client regarding following
  a wall.
  * In order to run the WallFollower, a systemd service is used. Once the raspberrypi receives the
  command to start the WallFollowing, the WallFollower service begins which excecutes the script
  WallFollowerService.py. When the raspberrypi receeives the stop command the robot stops moving.
  The majority of the variables, (MaxSpeed, TargetDistance, dist, MotorSpeed) are saved in .txt files
  so that the can be easily manipulated. Once the TCP server is initialized, the script WallFollower.sh
  is excecuted everytime a client sends a command to the server
  
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
 
 ## How to use
 
  * go to /home/pi/ and type git clone https://github.com/antonikaras/LE01_portfolio_2.git to clone the project
  * Copy the .py service scripts to /usr/bin/ directory
   ** sudo cp DistanceService.py /usr/bin/DistanceService.py
   ** sudo cp WallFollowerService.py /usr/bin/WallFollowerService.py
  * Make the above two files excecutables:
   ** sudo chmod +x /usr/bin/DistanceService.py
   ** sudo chmod +x /usr/bin/WallFollowerService.py
  * Copy the service files to /etc/systemd/system directory
   ** sudo cp Distance.service /etc/systemd/system/Distance.service
   ** sudo cp WallFollower.service /etc/systemd/system/WallFollower.service
  * Change the permissions of the two above files
   ** sudo chmod 644 /etc/systemd/system/Distance.service
   ** sudo chmod 644 /etc/systemd/system/WallFollower.service
  * Start the socat server using the following command:
   ** socat tcp-listen:8080,fork,reuseaddr exec:/home/pi/LEO1_portfolio_2/WallFollower.sh
  * Use the following command to communicate with the raspberry pi:
   ** echo (command) | socat - tcp:(#ip):8080
   ** command is one of the commands described in the command section

  
