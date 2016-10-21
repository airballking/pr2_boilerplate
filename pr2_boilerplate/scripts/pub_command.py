#!/usr/bin/env python
import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def joint_names():
    return ["r_shoulder_pan_joint", "r_shoulder_lift_joint", "r_upper_arm_roll_joint", "r_elbow_flex_joint", "r_forearm_roll_joint", "r_wrist_flex_joint", "r_wrist_roll_joint"]

def make_trajectory_point(duration, position):
    point = JointTrajectoryPoint()
    point.positions = [position] * 7
    point.velocities = [0] * 7
    point.time_from_start = rospy.Duration.from_sec(duration)
    return point

def make_trajectory():
    msg = JointTrajectory()
    msg.header.stamp = rospy.Time.now()
    msg.joint_names = joint_names() 
    msg.points.append(make_trajectory_point(3.0, -0.2))
    msg.points.append(make_trajectory_point(6.0, -0.7))
    return msg

def trajectory_publisher():
    rospy.init_node('trajectory_publisher')
    pub = rospy.Publisher('r_arm_controller/command', JointTrajectory, queue_size=1)
    rospy.sleep(.3)
    if not rospy.is_shutdown():
        msg = make_trajectory()
        pub.publish(msg)

if __name__ == '__main__':
    try:
        trajectory_publisher()
    except rospy.ROSInterruptException:
        pass
