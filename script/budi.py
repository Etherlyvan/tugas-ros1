#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Int16

smartguys = ""
xs = 0

def callback_smartguys(msg):
    global smartguys
    smartguys = msg.data
    process_msg()

def callback_xs(msg):
    global xs
    xs = msg.data
    process_msg()

def process_msg():
    if smartguys == "HIGH" and xs > 50:
        rospy.loginfo("LANCAR")
    elif smartguys == "MEDIUM" and xs > 50:
        rospy.loginfo("PATAH-PATAH")
    elif smartguys == "LOW" and xs > 50:
        rospy.loginfo("NGE-LAG")
    else:
        rospy.loginfo("MENDING TURU")

def budi():
    rospy.init_node('budi', anonymous=True)
    rospy.Subscriber("/smartguys", String, callback_smartguys)
    rospy.Subscriber("/xs", Int16, callback_xs)
    rospy.spin()

if __name__ == '__main__':
    budi()
