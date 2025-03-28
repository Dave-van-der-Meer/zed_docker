#!/bin/bash
# Build the package
echo "BUILDING ROS PACKAGES ..."
colcon build --packages-select zed2_camera

# Source the ROS 2 setup file
echo "SOURCING SETUP FILE ..."
source /root/ros2_ws/install/setup.bash

# Set the namespace environment variable
echo "SETTING ROS_NAMESPACE VARIABLE ..."
export ROS_NAMESPACE=leo01

# Launch the node
echo "LAUNCHING ZED2 CAMERA ..."
#ros2 launch zed_wrapper zed_camera.launch.py camera_model:=zed2
ros2 launch zed2_camera zed2.launch.py
