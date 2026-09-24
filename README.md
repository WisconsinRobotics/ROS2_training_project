# ROS2 & Git Onboarding: Turtle GPS Controller

Welcome to your first hands-on ROS2 mini-project! Today you will create a custom ROS2 package from scratch, write a controller node in Python, and drive a simulated turtle to a target GPS coordinate.

**Timeframe:** 1 Hour  
**Tooling:** Working with the Wisconsin Robotics workspace and Dev containers / ROS2 Humble / Python (`rclpy`)  
**AI Usage:** Strongly encouraged! Ask strategic questions about ROS2 architecture, `rclpy` callbacks, and control logic.

---

## Setup

Clone this git repository in your WroverSoftware_Docker/workspace directory, and then launch the docker container for main.

### Update package list and install turtlesim inside the main container.
```bash
sudo apt update && sudo apt install -y ros-humble-turtlesim
```
## Workspace Layout

Your workspace contains a pre-built package:
- `mock_gps`: Publishes simulated turtle location data to `/turtle/gps`.

You will create a **new package** called `turtle_control` alongside it.

---

## Setup Instructions

### Step 1: Create Your ROS2 Package
Navigate to your workspace `src` directory and generate a new Python package with pre-configured dependencies:

```bash
cd /workspace/ROS2_training_project/src
ros2 pkg create --build-type ament_python turtle_control --dependencies rclpy geometry_msgs
```

### Step 2: Create Your Controller Node File
Inside `src/turtle_control/turtle_control/`, create a new Python file named `turtle_controller.py`:

### Step 3: Register the Executable in `setup.py`
Open `src/turtle_control/setup.py` and register your node under `entry_points`. This is something you will be doing for all the executables (nodes - pubs, subs etc) you write:

```python
entry_points={
    'console_scripts': [
        'turtle_controller = turtle_control.turtle_controller:main',
    ],
},
```

---

## Project Requirements

### Step 1 & 2: Subscribe to GPS & Log Coordinates
1. In `turtle_controller.py`, set up a basic `rclpy` Node class.
2. Create a subscriber listening to `/turtle/gps` using message type `geometry_msgs/msg/Point`.
3. In the callback function, print the current `x` (lat) and `y` (lon) coordinates to the console using `self.get_logger().info(...)`.

### Step 3: Drive to Target GPS Coordinate
1. Define a target coordinate inside your node (e.g., `target_x = ???`, `target_y = ???`). This will be provided during the meeting (probably will be 10,10).
2. Create a publisher on topic `/turtle1/cmd_vel` using message type `geometry_msgs/msg/Twist`.
3. In your GPS callback, compute:
   - **Distance error:** `distance = sqrt((target_x - current_x)^2 + (target_y - current_y)^2)` - This is the Euclidean distance formula
   - **Desired heading:** `angle = atan2(target_y - current_y, target_x - current_x)` - This is the formula to compute angle between your current heading and the desired heading.
4. Publish linear velocity (`linear.x`) and angular velocity (`angular.z`) commands to steer and move the turtle toward the target coordinate. You must publish to ???

### Step 4 (Advanced Challenge)
If you finish Steps 1–3 early:
1. Make the target coordinate dynamic by subscribing to `/target_gps` (`geometry_msgs/msg/Point`).
2. When distance to target is less than `0.2` units:
   - Set linear velocity to `0.0`.
   - Print `"Target Reached!"` to the logger.
   - Perform a 360-degree spin in place.

---

## Build & Test Workflow

Every time you modify your code:

1. **Build the workspace:**
   ```bash
   cd /workspace/ROS2_training_project/
   colcon build --packages-select turtle_control
   ```

2. **Source the workspace (In EVERY new terminal):**
   ```bash
   source install/setup.bash
   ```

3. **Execution Order:**
   - **Terminal 1:** Launch turtlesim (`ros2 run turtlesim turtlesim_node`)
   - **Terminal 2:** Launch the mock GPS node (`ros2 run mock_gps mock_gps_node`)
   - **Terminal 3:** Run your new controller (`ros2 run turtle_control turtle_controller`)

---

## Strategic AI Prompts

Avoid asking AI to write the whole project at once. Break it down:
- *"Show me a minimal boilerplate for a ROS2 Python node using rclpy."*
- *"How do I create a subscriber for geometry_msgs/msg/Point in rclpy?"*
- *"How do I compute proportional angular steering towards a 2D point given current position?"*

---

## Git Workflow Requirements
1. Create a branch: `git checkout -b feature/yourname-turtle-control`
2. Commit incrementally: `git commit -m "feat: added gps subscriber"`
3. Push when done to your feature branch.
