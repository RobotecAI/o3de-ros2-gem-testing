import rclpy
from rclpy.node import Node

from tf2_msgs.msg import TFMessage


class TfStaticSubscriber(Node):

    def __init__(self):
        super().__init__('tf_static_subscriber')
        self.subscription = self.create_subscription(
            TFMessage,
            'tf_static',
            self.callback,
            10)
        self.subscription

    def callback(self, msg):
        for transform in msg.transforms:
            self.get_logger().info('Child frame: "%s"' % transform.child_frame_id)
            self.get_logger().info('Parent frame: "%s"' % transform.header.frame_id)
            if (transform.child_frame_id == transform.header.frame_id):
                self.get_logger().error('Child frame and parent frame are the same!')


def main(args=None):
    rclpy.init(args=args)

    tf_static_subscriber = TfStaticSubscriber()

    rclpy.spin(tf_static_subscriber)

    tf_static_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
