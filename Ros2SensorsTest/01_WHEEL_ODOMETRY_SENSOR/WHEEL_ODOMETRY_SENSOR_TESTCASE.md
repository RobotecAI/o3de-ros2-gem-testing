## TEST GOAL

Check if ROS2 wheel odometry sensor component works properly.

## TEST PERQUISITES
- Empty default level
- ros2 gem activated
- RosRobotSample gem activated
- O3DE editor launched

## TEST STEPS

### Step 1

Instantiate ROSbot.prefab from the RosRobotSample gem. Move the robot above the ground plane.

### Step 2

Add `ROS2 Wheel Odometry Sensor` (set the published topic name to `odom_wheel`) component to the `body_link` and `Odometry Sensor`


### Step 3

Press `Ctrl+G` to start simulation

### Step 4

Launch the script to move roboto in square-like trajectory and visualize the odometry data (`matplotlib`` is required)

```bash
import threading

import rclpy
from rclpy.qos import QoSProfile, ReliabilityPolicy
import time
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Twist, Quaternion
from nav_msgs.msg import Odometry
from tf2_msgs.msg import TFMessage
import tf2_ros
from tf_transformations import euler_from_quaternion

import math
import matplotlib.pyplot as plt


class SquareMoveRobot(Node):

    def __init__(self):
        super().__init__('square_move_robot')
        
        self.prefix = "" ##### Adjust the prefix to your robot name

        self.publisher_ = self.create_publisher(Twist, self.prefix + '/cmd_vel', 10)
        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.subscription_odom = self.create_subscription(Odometry, self.prefix + '/odom', self.odom_callback, qos)
        self.subscription_odom_wheel = self.create_subscription(Odometry, self.prefix + '/odom_wheel', self.odom_callback_wheel, qos)
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        self.pub_rate = 0.1
        self.t_init = self.get_clock().now()
        self.current_pose = (0,0)
        self.current_orientation = Odometry().pose.pose.orientation

        # Initialize lists to store x and y positions
        self.x_data = []
        self.y_data = []
        self.linear_velocity = []
        self.angular_velocity = []

        self.x_data_wheel = []
        self.y_data_wheel = []
        self.linear_velocity_wheel = []
        self.angular_velocity_wheel = []
    
    def spin_in_thread(self):
        rclpy.spin(self)


    def get_transform(self, target_frame, source_frame):
        try:
            trans = self.tf_buffer.lookup_transform(target_frame, source_frame, rclpy.time.Time())
            return trans
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            return None

    def odom_callback(self, msg: Odometry):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        linear_vel = msg.twist.twist.linear.x
        angular_vel = msg.twist.twist.angular.z
        self.current_pose = (x, y)
        self.current_orientation = msg.pose.pose.orientation

        # Store the values in the lists
        self.x_data.append(x)
        self.y_data.append(y)
        self.linear_velocity.append(linear_vel)
        self.angular_velocity.append(angular_vel)

    def odom_callback_wheel(self, msg: Odometry):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        linear_vel = msg.twist.twist.linear.x
        angular_vel = msg.twist.twist.angular.z

        # Store the values in the lists
        self.x_data_wheel.append(x)
        self.y_data_wheel.append(y)
        self.linear_velocity_wheel.append(linear_vel)
        self.angular_velocity_wheel.append(angular_vel)

    def drive_until_x(self, target_x, speed):
        while abs(target_x - self.current_pose[0]) > 0.1:  # threshold to stop the drive
            msg = Twist()
            msg.linear.x = speed
            self.publisher_.publish(msg)
            rclpy.spin_once(self, timeout_sec=self.pub_rate)

    def drive_until_y(self, target_y, speed):
        while abs(target_y - self.current_pose[1]) > 0.1:
            msg = Twist()
            msg.linear.x = speed
            self.publisher_.publish(msg)
            rclpy.spin_once(self, timeout_sec=self.pub_rate)

    def turn_by_degrees(self, degrees, ang_speed):
        initial_yaw = self.quaternion_to_yaw(self.current_orientation)
        target_yaw = initial_yaw + math.radians(degrees)

        # Adjust target_yaw if crossing the -π to π boundary
        if target_yaw > math.pi:
            target_yaw -= 2 * math.pi
        elif target_yaw < -math.pi:
            target_yaw += 2 * math.pi

        while abs(self.quaternion_to_yaw(self.current_orientation) - target_yaw) > 0.01:  # some threshold to stop the turning
            msg = Twist()
            msg.angular.z = ang_speed if self.quaternion_to_yaw(self.current_orientation) < target_yaw else -ang_speed
            self.publisher_.publish(msg)
            rclpy.spin_once(self, timeout_sec=self.pub_rate)

    def quaternion_to_yaw(self, quat: Quaternion) -> float:
        """Convert a Quaternion to a Yaw angle (z-axis rotation)"""
        euler = euler_from_quaternion([quat.x, quat.y, quat.z, quat.w])
        return euler[2]

    def visualize_trajectory(self):
        fig, axs = plt.subplots(2, 2, figsize=(15, 5))
        
        # Plot position trajectory on the first subplot
        
        axs[0][0].plot(self.x_data, self.y_data, '-r')
        axs[0][0].set_xlabel('X position')
        axs[0][0].set_ylabel('Y position')
        axs[0][0].set_title('Robot Trajectory')

        # Plot linear and angular velocities on the second subplot
        axs[1][0].plot(self.linear_velocity, label='Linear Velocity')
        axs[1][0].plot(self.angular_velocity, label='Angular Velocity')
        axs[1][0].set_xlabel('Time steps')
        axs[1][0].set_ylabel('Velocity')
        axs[1][0].set_title('Robot Velocities')

        # Plot odom wheel
        axs[0][1].plot(self.x_data_wheel, self.y_data_wheel, '-b')
        axs[0][1].set_xlabel('X position')
        axs[0][1].set_ylabel('Y position')
        axs[0][1].set_title('Robot Trajectory Wheel')

        # Plot linear and angular velocities on the second subplot
        axs[1][1].plot(self.linear_velocity_wheel, label='Linear Velocity')
        axs[1][1].plot(self.angular_velocity_wheel, label='Angular Velocity')
        axs[1][1].set_xlabel('Time steps')
        axs[1][1].set_ylabel('Velocity')

        # Legend
        axs[1][1].legend()

        plt.tight_layout()
        plt.show()

def main(args=None):
    rclpy.init(args=args)
    robot_mover = SquareMoveRobot()

    thread = threading.Thread(target=robot_mover.spin_in_thread)
    thread.start()

    robot_mover.drive_until_x(1, 0.5)
    robot_mover.turn_by_degrees(90, 0.5)
    robot_mover.drive_until_y(1, 0.5)
    robot_mover.turn_by_degrees(90, 0.5)
    robot_mover.drive_until_x(0, 0.5)
    robot_mover.turn_by_degrees(90, 0.5)
    robot_mover.drive_until_y(0, 0.5)
    robot_mover.turn_by_degrees(90, 0.5)


    thread.join(timeout=10)
    robot_mover.visualize_trajectory()

    robot_mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

#### Expected Result

Robot is moving in the square-like trajectory and the odometry and odom_wheel data is visualized in the plot after the move is finished. The trajectory from both sensors should be similar (the difference is caused by the friction).

