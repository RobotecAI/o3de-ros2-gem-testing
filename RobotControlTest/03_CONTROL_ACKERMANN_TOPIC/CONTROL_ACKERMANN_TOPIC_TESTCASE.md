# Test Goal

- Check if ROS2 Control creates proper topics
- Check if messages are received and processed

# Test Perquisite

- Empty default Level
- ROS2 Gem activated
- O3DE Editor running

# Steps

## Step 1

Launch the system terminal and run:

```bash
source /opt/ros/humble/setup.bash
ros2 topic list -t
```

Leave the terminal open - it will be needed in the next steps.

> Note: make sure, no ROS services are runing on your computer

### Expected result

- It should NOT include any messages of type: `geometry_msgs/msg/Twist`
- It should NOT include any messages of type: `ackermann_msgs/msg/AckermannDrive`

## Step 2 

Copy the file: [ackermann_robot.prefab](../Assets/ackermann_robot.prefab) into the Assets folder of your project and instantiate it. Move the robot to be located above the ground plane.

### Expected result

Your level should look like this:
![](images/control_initial_setup.png)

## Step 3

Press `Ctrl+G` to enter game mode.

## Step 4 

In the terminal run:

```bash
ros2 topic list
```

### Expected result

You should see something like this:

```bash
/base_link/ackermann_vel [ackermann_msgs/msg/AckermannDrive]
/clock [rosgraph_msgs/msg/Clock]
/parameter_events [rcl_interfaces/msg/ParameterEvent]
/rosout [rcl_interfaces/msg/Log]
/tf [tf2_msgs/msg/TFMessage]
/tf_static [tf2_msgs/msg/TFMessage]
```

Detailed list of topics may by different, but:
- It should include `/base_link/ackermann_vel` of type: `ackermann_msgs/msg/AckermannDrive`
- It should NOT include any messages of type: `geometry_msgs/msg/Twist`

## Step 5

In the terminal run:

```bash
ros2 topic pub -r 10 /base_link/ackermann_vel ackermann_msgs/msg/AckermannDrive "{steering_angle: 0.7, steering_angle_velocity: 0.0, speed: 2.0, acceleration: 0.0, jerk: 0.0}"
```

### Expected result

The robot should drive in circles.

![](images/control_result.gif)
