# TEST GOAL

Check if contact sensor works properly.

## TEST PERQUISITES

- ROS2 Template Demo Level
- ROSBot prefab

## TEST STEPS

### Step 1

Add contact sensor to the ROSBot prefab, add to the `body_link`.

### Step 2
Run the simulation

### Step 3

Check if the contact sensor publishes data `ros2 topic echo /contact_sensor` the sensor publishes only when there is a hit so drive a robot into a wall and check if the data is published.

