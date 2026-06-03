import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import matplotlib.pyplot as plt

class RobotController(Node):

    def __init__(self):
        super().__init__('robot_controller')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

        # Initial position
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        # Goal position
        self.x_goal = 5.0
        self.y_goal = 5.0

        # Gains
        self.kp_dist = 0.8
        self.kp_angle = 3.0

        # Data storage for plotting
        self.history_x = []
        self.history_y = []
        self.history_error = []

    def control_loop(self):

        dx = self.x_goal - self.x
        dy = self.y_goal - self.y

        distance = math.sqrt(dx**2 + dy**2)
        angle_to_goal = math.atan2(dy, dx)

        angle_error = angle_to_goal - self.theta

        # Normalize angle
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        # Control
        v = self.kp_dist * distance
        omega = self.kp_angle * angle_error

        # Limit speeds
        v = min(v, 1.0)
        omega = max(min(omega, 2.0), -2.0)

        msg = Twist()
        msg.linear.x = v
        msg.angular.z = omega

        self.publisher_.publish(msg)

        # Simulated motion
        dt = 0.1
        self.x += v * math.cos(self.theta) * dt
        self.y += v * math.sin(self.theta) * dt
        self.theta += omega * dt

        # Store data
        self.history_x.append(self.x)
        self.history_y.append(self.y)
        self.history_error.append(distance)

        self.get_logger().info(f"x={self.x:.2f}, y={self.y:.2f}, error={distance:.2f}")

        # Stop condition
        if distance < 0.05:
            self.get_logger().info("Goal Reached!")

            # Plot trajectory
            plt.figure()
            plt.plot(self.history_x, self.history_y)
            plt.scatter(self.x_goal, self.y_goal)
            plt.title("Robot Trajectory")
            plt.xlabel("X Position")
            plt.ylabel("Y Position")
            plt.grid()

            # Plot error
            plt.figure()
            plt.plot(self.history_error)
            plt.title("Error vs Time")
            plt.xlabel("Time Step")
            plt.ylabel("Error")
            plt.grid()

            plt.show()

            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
