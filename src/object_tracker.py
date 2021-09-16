#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def talker():
    # pub = rospy.Publisher('trackers/object_pose', String, queue_size=10) # use when launching each node separately
    pub = rospy.Publisher('object_pose', String, queue_size=10) # use when launching the project by the launch file
    rospy.init_node('object_tracker', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        # global_state = rospy.get_param("/state")
        # if global_state =="picking_object":
        object_pose = "obj xyz ; rpy"
        pub.publish(object_pose)
        rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        rospy.set_param("/state", "picking_object")
        talker()
    except rospy.ROSInterruptException:
        pass
