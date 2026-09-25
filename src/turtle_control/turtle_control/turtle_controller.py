import rclpy
from rclpy.node import Node

class TurtleController(Node):
    
    def __init__(self, current_position):
        #Node name is turtle_controller
        super().__init__('turtle_controller')

    self.targetSub = self.create_subscription(
        geometry_msgs/msg/Point, 
        '/turtle/gps', 
        self.callback, 
        10)

    self.path_publisher = self.create_publisher(geometry_msgs/msg/Twist, '/turtle/cmd_vel', 10)

    def callback(self, msg):
        # Update current position
        self.current_x = msg.x
        self.current_y = msg.y

        # Calculate distance and angle to target
        self.distance = sqrt((self.target_x - self.current_x)**2 + (self.target_y - self.current_y)**2)
        self.angle = atan2(self.target_y - self.current_y, self.target_x - self.current_x)

        # Create Twist message to control turtle
        twist_msg = geometry_msgs.msg.Twist()
        
        if self.distance > 0.1:  # If the turtle is not at the target position
            twist_msg.linear.x = 1.0  # Move forward
            twist_msg.angular.z = self.angle  # Rotate towards the target
        else:
            twist_msg.linear.x = 0.0  # Stop moving
            twist_msg.angular.z = 0.0  # Stop rotating

        # Publish the Twist message
        self.path_publisher.publish(twist_msg)