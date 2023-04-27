from rclpy.node import Node
from nav_msgs.msg import Odometry
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
import rclpy

import subprocess

class Subscriber(Node):
    def __init__(self):
        super().__init__('test_subscriber')
        
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        received_msg = False
        self.subscription = self.create_subscription(
            Odometry,
            '/TestEntity/odom',
            self.callback,
            qos_profile=qos_profile)
    
    def callback(self, msg):
        self.received_msg = True



if __name__ == "__main__":
    rclpy.init(args=None)
    subscriber = Subscriber()
    rclpy.spin_once(subscriber, timeout_sec=1.0)
    subscriber.destroy_node()
    rclpy.shutdown()
    
    assert subscriber.received_msg
