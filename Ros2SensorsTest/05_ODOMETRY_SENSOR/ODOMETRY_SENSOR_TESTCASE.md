# TEST GOAL

Check if ROS2 Odometry sensor component works properly.

## TEST PERQUISITES
- Empty default level
- ros2 gem activated

## TEST STEPS

### Step 1

Create a box (without collider - free fall) and add `ROS2 Odometry Sensor` component to it.

### Step 2

Press `Ctrl+G` to start simulation.

### Step 3

Check if the data published is correct `ros2 topic echo /odom` and changes over time. Also check the frequency. `ros2 topic hz /odom` Modify the parameters of the sensor and repeat the test.

### Step 4 Extra

Add the `ROS2 Odometry Sensor` component to the `body_link` of the ROSBot prefab. Press `Ctrl+G` to start simulation. Check if the sensor publishes data `ros2 topic echo /odom` and how the data changes. Also the data visualization tool like plotjuggler can be used to visualize the data and check if the published data is smooth.