#!/bin/bash

sudo chmod 666 /dev/ttyUSB0
cd catkin_ws
source devel/setup.bash
roslaunch rplidar_ros rplidar.launch