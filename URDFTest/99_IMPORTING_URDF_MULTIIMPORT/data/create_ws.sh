#! /bin/sh

cd ~ 
RED="\e[31m" 
GREEN="\e[32m" 
ENDCOLOR="\e[0m" 
export ROS2WS=$PWD/testing_ws 
rm -rf ${ROS2WS}/src || true 
mkdir -p ${ROS2WS}/src 

####
echo "${RED}-> ${GREEN}Clone UR10${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git 
cd ${ROS2WS}/src/Universal_Robots_ROS2_Description && git checkout --quiet 464864acfe85f600c3d3438e025805b5296f5aa8 
###
echo "${RED}-> ${GREEN}Clone Husky${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/husky/husky.git 
cd husky && git checkout --quiet  1e0b1d14d657f04ec3a86e73d6676a2cf7af6f79  
###
echo "${RED}-> ${GREEN}Clone MINPUPPER${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/mangdangroboticsclub/mini_pupper_ros.git 
cd mini_pupper_ros && git checkout --quiet  276875c09f3423cf307a2b0d0320944e41612712 
###
echo "${RED}-> ${GREEN}Clone ROSBOT${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/husarion/rosbot_xl_ros.git && cd rosbot_xl_ros && git checkout --quiet  94795ff30585b2b6faa595cd6519a8f9ca17f5d0 && cd .. 
git clone https://github.com/husarion/ros_components_description.git && cd ros_components_description && git checkout --quiet  5f94c332c866c8e39f6854f77d98651a2a3ae226 
###
echo "${RED}-> ${GREEN}Clone Jackal${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/jackal/jackal.git 
cd jackal && git checkout --quiet  017b8b581a90873047f7d6fe438bd87513be4a76  
##
echo "${RED}-> ${GREEN}Clone TechMan${ENDCOLOR}" && cd ${ROS2WS}/src 
git clone https://github.com/TechmanRobotInc/tmr_ros2.git 
cd tmr_ros2 && git checkout --quiet  13cf3b96746d750750312f0492a021a02d1ec34f 
touch ${ROS2WS}/src/tmr_ros2/custom_package/COLCON_IGNORE
touch ${ROS2WS}/src/tmr_ros2/demo/COLCON_IGNORE 
touch ${ROS2WS}/src/tmr_ros2/tm_driver/COLCON_IGNORE
##
echo "${RED} *** ${GREEN}BUILD$ ${RED} *** ${ENDCOLOR}" && cd ${ROS2WS}/src 
cd ${ROS2WS} 
colcon build --symlink-install