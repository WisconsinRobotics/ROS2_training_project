# ROS2 & Git Onboarding: Turtle GPS Controller

Welcome to your first hands-on ROS2 mini-project! Today you will create a custom ROS2 package from scratch, write a controller node in Python, and drive a simulated turtle to a target GPS coordinate.

**Timeframe:** 1 Hour (its fine if you go over) 
**Tooling:** Using the Wisconsin Robotics Dev container based workspace / ROS2 Humble / Python (`rclpy`)  
**AI Usage:** Strongly encouraged! Ask strategic questions about ROS2 architecture, `rclpy` callbacks, and control logic.

---

## Workspace Layout
Your workspace contains a pre-built package:
* `mock_gps`: Publishes simulated turtle location data to `/turtle/gps`.

You will create a **new package** called `turtle_control` alongside it.

---

## Setup Instructions

### Step 1: Create Your ROS2 Package
Navigate to your workspace `src` directory and generate a new Python package with pre-configured dependencies:

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python turtle_control --dependencies rclpy geometry_msgs
