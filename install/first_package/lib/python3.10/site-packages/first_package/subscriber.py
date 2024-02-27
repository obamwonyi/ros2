# Python subscriber node
# Author : Destiny Obamwonyi
# Date: February 27

import rclpy

from std_msgs.msg import String

from rclpy.node import Node

class SubscriberNode(Node):
    """
    This class will handle the subscriber 
    node functionality.
    """
    def __init__(self):
        super().__init__('node_subscriber')

        self.subscription = self.create_subscription(String, 'communication_topic', self.callbackFunction, 15)
        self.subscription


    def callbackFunction(self, message):
        self.get_logger().info('We received: "%s"' % message.data)



def main(args=None):

    rclpy.init(args=args)

    node_subscriber = SubscriberNode()

    rclpy.spin(node_subscriber)

    node_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()