# TEST GOAL

Check if ROS2 GNSS sensor component works properly.

## TEST PERQUISITES
- Empty default level
- ros2 gem activated

## TEST STEPS

### Step 1

Create a box (without collider - free fall) and add `ROS2 GNSS Sensor` component to it.

### Step 2

Press `Ctrl+G` to start simulation.

### Step 3

Check if the data published is correct `ros2 topic echo /gnss` and changes over time. Also check the frequency. `ros2 topic hz /gnss` Modify the parameters of the sensor and repeat the test.

### Step 4 Extra

Add the `ROS2 GNSS Sensor` component to the `body_link` of the ROSBot prefab. Press `Ctrl+G` to start simulation. Check if the sensor publishes data `ros2 topic echo /gnss` and how the data changes.