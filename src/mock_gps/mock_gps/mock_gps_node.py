import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Point


class MockGpsNode(Node):
    def __init__(self):
        super().__init__('mock_gps_node')

        self.turtle_sub = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.pose_callback,
            10
            )

        self.gps_pub = self.create_publisher(
            Point,
            '/turtle/gps',
            10
        )

        self.get_logger().info('Mock GPS node is running. Translating /turtle1/pose into /turtle/gps...')

    def pose_callback(self, msg: Pose):

        gps_msg = Point()

        gps_msg.x = float(msg.x)
        gps_msg.y = float(msg.y)
        gps_msg.z = 0.0

        self.gps_pub.publish(gps_msg)


def main(args=None):

    rclpy.init(args=args)
    node = MockGpsNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()