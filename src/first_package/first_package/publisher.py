# Python publisher node
# Author: Destiny Obamwonyi
# Date: February 27

# rclp is a Python API for communicating and interacting with ROS2.
# API stands for the Application Programming Interface
# it is an interface between two programs
import rclpy 

# Here we will send string as message
from std_msgs.msg import String

# importing the node class
from rclpy.node import Node


# We create the class PublisherNode that is inherited from thee Node
# class
class PublisherNode(Node):
    """
    This class will be responsible for the publisher node
    functionality
    """
    def __init__(self):
        """
        class constructor, this would execute the code beneath
        immediately the class is instantiated .
        """
        super().__init__('node_publisher')

        # Create publisher with "communication_topic" as the topic
        # with a buffer size of 15
        self.publisher_ = self.create_publisher(String, 'communication_topic', 15)

        commRate = 1 # in seconds

        self.timer = self.create_timer(commRate, self.callbackFunction)
        # counter
        self.counter = 0

    def callbackFunction(self):
        # Create a message
        messagePublisher = String()
        # fill in the message data with a string
        messagePublisher.data = "Counter value: %d" % self.counter
        # publish the message to the topic
        self.publisher_.publish(messagePublisher)
        # publish the message to the logger that will display the message
        # in the same window in which the publisher node was started
        self.get_logger().info('Publisher node is publishing:"%s"' % messagePublisher.data)
        # increment the counter
        self.counter=self.counter+1



# main function / entry point
def main(args=None):
    # initialize
    rclpy.init(args=args)
    # create the object
    node_publisher = PublisherNode()
    #call the spin function that will spin the node and make sure that callbacks are called
    rclpy.spin(node_publisher)
    node_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()