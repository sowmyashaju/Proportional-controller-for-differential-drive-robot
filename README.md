# Proportional-controller-for-differential-drive-robot

## Overview

This project implements a **Proportional (P) Controller** for autonomous navigation of a differential drive robot using **ROS2 Humble** and **Gazebo Simulator**. The controller drives the robot from an initial position to a desired goal position by continuously minimizing distance and orientation errors.

The project demonstrates closed-loop feedback control, robot kinematics, ROS2 communication, and simulation-based validation of control system concepts.

---

## Features

- Closed-loop navigation
- Proportional (P) control implementation
- Differential drive robot simulation
- Goal-based autonomous movement
- Error minimization using feedback
- Real-time velocity command generation
- Robot trajectory plotting
- Error vs Time analysis
- ROS2 and Gazebo integration

---

## System Architecture

```text
Goal Position
      │
      ▼
Error Calculation
      │
      ▼
Proportional Controller
      │
      ▼
Velocity Commands (/cmd_vel)
      │
      ▼
Differential Drive Robot
      │
      ▼
Odometry Feedback
      │
      └──────────────► Error Calculation
```

---

## Control Equations

### Position Error

```math
e_x = x_{goal} - x
```

```math
e_y = y_{goal} - y
```

### Distance Error

```math
d = \sqrt{e_x^2 + e_y^2}
```

### Angle to Goal

```math
\theta_g = atan2(e_y,e_x)
```

### Angle Error

```math
e_\theta = \theta_g - \theta
```

### Proportional Controller

Linear velocity:

```math
v = K_{p_{dist}} \times d
```

Angular velocity:

```math
\omega = K_{p_{angle}} \times e_\theta
```

---

## Software Requirements

- Ubuntu 22.04
- ROS2 Humble
- Gazebo Simulator
- Python 3
- Matplotlib
- TurtleBot3 Packages

---

## Project Structure

```text
Proportional-Controller-for-Differential-Drive-Robot/

├── diff_drive_pid/
│   └── controller.py
│
├── resource/
│   └── diff_drive_pid
│
├── package.xml
├── setup.py
├── README.md

```

---

## Installation

### Create Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

### Clone Repository

```bash
git clone https://github.com/your-github-Sowmya_Shaju/Proportional-Controller-for-Differential-Drive-Robot.git
```

### Build Package

```bash
cd ~/ros2_ws
colcon build
```

### Source Workspace

```bash
source install/setup.bash
```

---

## Running the Project

### Terminal 1 – Launch Gazebo

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo empty_world.launch.py
```

### Terminal 2 – Run Controller

```bash
source ~/ros2_ws/install/setup.bash
ros2 run diff_drive_pid controller
```

---

## Controller Parameters

### Goal Position

```python
self.x_goal = 5.0
self.y_goal = 5.0
```

### Controller Gains

```python
self.kp_dist = 0.8
self.kp_angle = 3.0
```

### Velocity Limits

```python
v = min(v, 1.0)
omega = max(min(omega, 2.0), -2.0)
```

---

## Algorithm

1. Start ROS2 node.
2. Initialize robot position.
3. Define goal position.
4. Calculate distance error.
5. Calculate angular error.
6. Apply proportional control law.
7. Generate linear and angular velocities.
8. Publish velocity commands to `/cmd_vel`.
9. Update robot position.
10. Repeat until goal is reached.
11. Plot trajectory and error graphs.
12. Stop the controller.

---

## Working Principle

The robot continuously calculates the distance and orientation difference between its current position and the target position.

The proportional controller generates:

- Linear velocity proportional to distance error.
- Angular velocity proportional to angle error.

As the robot approaches the target:

- Distance error decreases.
- Velocity decreases.
- Motion becomes stable.
- Robot stops near the goal.

---

## ROS2 Topics

| Topic | Description |
|---------|-------------|
| /cmd_vel | Velocity command sent to robot |

---
