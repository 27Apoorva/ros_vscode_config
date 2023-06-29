#!/usr/bin/env python3
import rclpy   ## ROS 2 client library for Python
from rclpy.node import Node    ## importing Node class from rclpy
from std_msgs.msg import String    # import built-in string message type from ROS data types

class HelloWorldSubscriber(Node):    ## creating a new class  inheriting from Node class
	def __init__(self):
		super().__init__("hello_world_sub_node")     ## ==> node name
        ## super().__init__() calls the Node class’s constructor and gives it your node name
		self.sub = self.create_subscription(String, "hello_world", self.subscriber_callback, qos_profile=10)
        # The node subscribes to messages of type std_msgs/String, over a topic
        # takes 4 args (topic type, topic name, callback function qos_profile)

	def subscriber_callback(self, msg):
		print("Recieved: " + msg.data)


def main(args=None):
	rclpy.init(args=args)     # Initialize the rclpy library
	my_sub = HelloWorldSubscriber()     ## create class object
	print("Waiting for data to be published...")

	try:
		rclpy.spin(my_sub)      ### allowing the ros node to keep running
	except KeyboardInterrupt:       ### stop the node using Ctrl + C
		print("Terminating Node...")
		my_sub.destroy_node()       ### destroy the node object
		rclpy.shutdown()     ### shutdown rclpy instances


if __name__ == '__main__':
	main()