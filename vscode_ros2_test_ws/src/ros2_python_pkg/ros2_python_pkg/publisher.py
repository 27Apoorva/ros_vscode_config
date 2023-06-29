#!/usr/bin/env python3
import rclpy   ## ROS 2 client library for Python
from rclpy.node import Node    ## importing Node class from rclpy
from std_msgs.msg import String    # import built-in string message type from ROS data types

class HelloWorldPublisher(Node):    ## creating a new class  inheriting from Node class
	def __init__(self):
		super().__init__("hello_world_pub_node")     ## ==> node name
        ## super().__init__() calls the Node class’s constructor and gives it your node name
		self.pub = self.create_publisher(String, "hello_world", qos_profile=10)
        ## declares that the node publishes messages, takes 3 args (topic type, topic name, qos_profile)
        ## qos_profile is a required QoS (quality of service) setting that limits the amount of queued messages if a subscriber is not receiving them fast enough
		self.timer = self.create_timer(0.5, self.publish_hello_world)
        ## timer is created with a callback to execute every 0.5 seconds
        ## 2 args (frequesncy at which to publish message, callback function)
		self.counter = 0   ## counter variable

	def publish_hello_world(self):    ### callback function ==> call this function from within your code – here as a callback in a timer
		msg = String()     ### create String message object
		msg.data = "Hello World " + str(self.counter)   
		self.pub.publish(msg)     ### publish() function from the publisher object to actually publish on the topic
		self.get_logger().info('Publishing: "%s"' % msg.data)	  ## print to console, similar to print statement	
		self.counter += 1     ## incrementing counter variable

def main(args=None):
	rclpy.init(args=args)     # Initialize the rclpy library
	my_pub = HelloWorldPublisher()     ## create class object
	print("Publisher Node Running...")

	try:
		rclpy.spin(my_pub)    ### allowing the ros node to keep running
	except KeyboardInterrupt:       ### stop the node using Ctrl + C
		print("Terminating Node...")
		my_pub.destroy_timer(timer=my_pub.timer)   ### destroy the timer attached to the node explicitly
		my_pub.destroy_node()               ### destroy the node object
		rclpy.shutdown()     ### shutdown rclpy instances


if __name__ == '__main__':
	main()