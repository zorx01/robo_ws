import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleMover(Node):
    def __init__(self):
        super().__init__('circle_mover')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move_in_circle)
        self.vel_msg = Twist()

    def move_in_circle(self):
        # Set linear and angular velocities
        linear_speed = 0.2  # meters per second
        angular_speed = 0.5  # radians per second

        # Update velocity message
        self.vel_msg.linear.x = linear_speed
        self.vel_msg.angular.z = angular_speed
        
        # Publish the velocity message
        self.publisher.publish(self.vel_msg)
        self.get_logger().info(f'Moving in a circle with linear speed: {linear_speed} and angular speed: {angular_speed}')

def main(args=None):
    rclpy.init(args=args)
    circle_mover = CircleMover()
    
    try:
        rclpy.spin(circle_mover)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop the robot when shutting down
        circle_mover.vel_msg.linear.x = 0.0
        circle_mover.vel_msg.angular.z = 0.0
        circle_mover.publisher.publish(circle_mover.vel_msg)
        circle_mover.get_logger().info('Stopping the robot.')
        circle_mover.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
