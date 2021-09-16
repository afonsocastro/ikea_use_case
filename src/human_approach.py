#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time


def callback_approach_human(data):
    # pub = rospy.Publisher('human_approached', String, queue_size=10)

    global_state = rospy.get_param("/state")
    # print(global_state)

    if global_state == "approaching_human":
        print("Getting closer to the human...")
        rospy.sleep(5)  # time that it takes to get closer to the human
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        is_close_human = "human caught at " + str(current_time)
        print(is_close_human)
        # pub.publish(is_close_human)
        rospy.set_param("/state", "human_decision")


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node('human_approach', anonymous=False)
    rospy.Subscriber("trackers/human_pose", String, callback_approach_human)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()

