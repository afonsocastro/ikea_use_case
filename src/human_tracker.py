#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def talker():
    # pub = rospy.Publisher('trackers/human_pose', String, queue_size=10)  # use when launching each node separately
    pub = rospy.Publisher('human_pose', String, queue_size=10)  # use when launching the project by the launch file

    rospy.init_node('human_tracker', anonymous=False)
    # human_pose = "human xyz ; rpy"
    # pub.publish(human_pose)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        # global_state = rospy.get_param("/state")
        # if global_state == "approaching_human":
        human_pose = "human xyz ; rpy"
        pub.publish(human_pose)
        rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass