import rclpy
from rclpy.node import Node

class TurtleController(Node):
    
    #Node name is turtle_controller
    super().__init__('turtle_controller')

    self.targetSub = self.create_subscription(geometry_msgs/msg/Point, /turtle/gps, self.get_logger().info(current_position.x, current_position.y), 10)

    