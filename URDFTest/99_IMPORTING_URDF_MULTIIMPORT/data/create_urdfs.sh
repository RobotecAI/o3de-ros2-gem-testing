#! /bin/sh

cd ~ 
RED="\e[31m" 
GREEN="\e[32m" 
ENDCOLOR="\e[0m" 
export ROS2WS=$PWD/testing_ws 
export URDFS=$PWD/testing_ws/urdfs
mkdir -p $URDFS
####
echo "${RED}-> ${GREEN}XACRO UR5${ENDCOLOR}" 
xacro ${ROS2WS}/src/Universal_Robots_ROS2_Description/urdf/ur.urdf.xacro name:=test_ur5 ur_type:=ur5 > $URDFS/000_urtest_ur5.urdf

echo "${RED}-> ${GREEN}XACRO UR5e${ENDCOLOR}" 
xacro ${ROS2WS}/src/Universal_Robots_ROS2_Description/urdf/ur.urdf.xacro name:=test_ur5e ur_type:=ur5e > $URDFS/001_test_ur5e.urdf

echo "${RED}-> ${GREEN}XACRO UR10${ENDCOLOR}" 
xacro ${ROS2WS}/src/Universal_Robots_ROS2_Description/urdf/ur.urdf.xacro name:=test_ur10 ur_type:=ur5e > $URDFS/002_test_ur10.urdf

echo "${RED}-> ${GREEN}XACRO UR10e${ENDCOLOR}" 
xacro ${ROS2WS}/src/Universal_Robots_ROS2_Description/urdf/ur.urdf.xacro name:=test_ur10e ur_type:=ur10e > $URDFS/003_test_ur10e.urdf

echo "${RED}-> ${GREEN}XACRO Husky${ENDCOLOR}" 
xacro ${ROS2WS}/src/husky/husky_description/urdf/husky.urdf.xacro > $URDFS/004_husky.urdf

echo "${RED}-> ${GREEN}XACRO MiniPupper${ENDCOLOR}" 
xacro ${ROS2WS}/src/mini_pupper_ros/mini_pupper_description/urdf/mini_pupper_description.urdf.xacro > $URDFS/005_minpupper.urdf

echo "${RED}-> ${GREEN}XACRO Rosbot${ENDCOLOR}" 
xacro ${ROS2WS}/src/rosbot_xl_ros/rosbot_xl_description/urdf/rosbot_xl.urdf.xacro engine:=o3de > $URDFS/006_rosbot_o3de.urdf

echo "${RED}-> ${GREEN}XACRO Jackal${ENDCOLOR}" 
xacro ${ROS2WS}/src/jackal/jackal_description/urdf/jackal.urdf.xacro > $URDFS/007_jackal.urdf

echo "${RED}-> ${GREEN}XACRO Techmans${ENDCOLOR}" 

xacro ${ROS2WS}/src/tmr_ros2/tm_description/urdf/tm5-900.urdf > $URDFS/008_tm5-900.urdf

xacro ${ROS2WS}/src/tmr_ros2/tm_description/urdf/tm12-nominal.urdf > $URDFS/009_tm12-nominal.urdf
xacro ${ROS2WS}/src/tmr_ros2/tm_description/urdf/tm12x-nominal.urdf > $URDFS/010_tm12x-nominal.urdf

xacro ${ROS2WS}/src/tmr_ros2/tm_description/urdf/tm14-nominal.urdf > $URDFS/011_tm14-nominal.urdf
xacro ${ROS2WS}/src/tmr_ros2/tm_description/urdf/tm14x-nominal.urdf > $URDFS/012_tm14x-nominal.urdf