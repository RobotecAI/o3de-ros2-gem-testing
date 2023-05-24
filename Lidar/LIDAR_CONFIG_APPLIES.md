## Edit Lidar Component Parameters

### Objective: Ensure that the Lidar Component's editor parameters can be tweaked and the changes are reflected in the sensor output

### Prerequisites:

- O3DE Editor is running and the scene is already opened.
- ROS2 Gem is enabled for the project.
- A scene has been created in the O3DE Editor.
- A robot prefab has been imported into the scene and it already has a Lidar component added to it.
- ROS2 environment is sourced (`source /opt/ros/humble/setup.bash`)

### Test Steps:

- Select the entity in the prefab instance that represents the Lidar sensor.
- In the Entity Inspector panel, locate the ROS2 Lidar Sensor Component and expand it to view the available parameters.
- Modify the Lidar model by selecting a different option from the "Lidar Model" dropdown menu.
- Adjust other parameters, such as "Min range", "Max range", "Min horizontal angle [Deg]", "Max horizontal angle [Deg]", "Min vertical angle [Deg]", "Max vertical angle [Deg]", and "Points per layer".
- Switch to Game mode by clicking the Play button on the top toolbar (`Ctrl+G`).
- In Game mode, verify that the Lidar component is detecting objects according to the modified parameters.
- Run the `ros2 topic echo` in the terminal window and verify that the incoming messages reflect the updated parameters.
- In the O3DE Editor, move the robot in Game mode around the scene to verify that the Lidar data is being published to the appropriate topic and visualized in rviz2 according to the updated parameters.

### Expected Result:

The Lidar component's editor parameters can be successfully tweaked, and the changes are reflected in the sensor output when in Game mode. The Lidar data published to the appropriate topic and visualized in rviz2 should match the updated parameters.
