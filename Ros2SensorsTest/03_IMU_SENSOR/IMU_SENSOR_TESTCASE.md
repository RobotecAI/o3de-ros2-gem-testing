# TEST GOAL

Check if ROS2 IMU sensor component works properly.

## TEST PERQUISITES
- Empty default level
- ros2 gem activated

## TEST STEPS

### Step 1

Create a box (without collider - free fall) and add `ROS2 IMU Sensor` component to it.

### Step 2

Press `Ctrl+G` to start simulation

### Step 3

Check if the sensor publishes data `ros2 topic echo /imu` the acceleration should be close to 9.8 m/s^2 and the orientation should be close to 0.0.
Check also if the publish frequency is stable `ros2 topic hz /imu`

To check if data is correct use visual inspection with rviz2, check if the data is smooth and the orientation is correct. Also can add collider to the box and check if the data is correct when the box is not moving. Change the parameters (including frequency) of the sensor and repeat the test.

### Step 4 Extra

Initiate rosbot prefab from the  Add `ROS2 IMU Sensor` component to the `body_link`. Press `Ctrl+G` to start simulation. Check if the sensor publishes data `ros2 topic echo /imu` and how the data changes. 
