#! /bin/bash

read inp val

if [ -z "$val" ]
then
    val=-1
fi

if [ $inp == "on" ]
then
    echo "Starting getting distance from the ultrasonic sensor"
    sudo systemctl start Distance.service
elif [ $inp == "off" ]
then
    echo "Stopping getting distance from the ultrasonic sensor"
    sudo systemctl stop Distance.service
elif [ $inp == "getdist" ]
then
    line=$(head -n 1 "/home/pi/LEO1_portfolio_2/dist.txt")
    while [ -z "$line" ]
    do
        line=$(head -n 1 "/home/pi/LEO1_portfolio_2/dist.txt") 
    done

    echo $line
elif [ $inp == "getmotors" ]
then
    line=$(head -n 1 "/home/pi/LEO1_portfolio_2/MotorSpeed.txt")
    while [ -z "$line" ]
    do
        line=$(head -n 1 "/home/pi/LEO1_portfolio_2/MotorSpeed.txt") 
    done

    echo $line

elif [ $inp == "start" ]
then
    echo "Starting the Wall follower"
    sudo systemctl restart WallFollower.service
elif [ $inp == "stop" ]
then
    echo "Stopping the Wall Follower"
    line=$(head -n 1 "/home/pi/LEO1_portfolio_2/MaxSpeed.txt")
    echo 0 > /home/pi/LEO1_portfolio_2/MaxSpeed.txt
    sleep 0.015
    sudo systemctl stop WallFollower.service
    echo $line > /home/pi/LEO1_portfolio_2/MaxSpeed.txt
elif [ $inp == "maxspeed" ]
then
    if (( $(echo "$val > 0" |bc -l) )) 
    then
        echo "Change Max Speed to " $val
        echo $val > /home/pi/LEO1_portfolio_2/MaxSpeed.txt
    else
        line=$(head -n 1 "/home/pi/LEO1_portfolio_2/MaxSpeed.txt")
        echo "Current Max Speed " $line
    fi
elif [ $inp == "walldist" ]
then
    if (( $(echo "$val > 0" |bc -l) ))
    then
        echo "Changing wall distance to " $val
        echo $val > /home/pi/LEO1_portfolio_2/TargetDist.txt 
    else
        line=$(head -n 1 "/home/pi/LEO1_portfolio_2/TargetDist.txt")
        echo "Current Target Distance =  " $line
    fi
fi

#echo "end"
