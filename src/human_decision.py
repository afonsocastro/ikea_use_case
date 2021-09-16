#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time


def listener():
    pub = rospy.Publisher('decision', String, queue_size=10)
    print("Evaluating human decision...")
    rospy.sleep(5)  # time that it takes to get the human decision
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    human_has_decided = "Decision made at " + str(current_time)
    print(human_has_decided)
    decision = "ok"
    rospy.set_param("/state", "object_placing")
    pub.publish(decision)


if __name__ == '__main__':

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('human_decision', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        global_state = rospy.get_param("/state")
        if global_state == "human_decision":
            listener()
        rate.sleep()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

