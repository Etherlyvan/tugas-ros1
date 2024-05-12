#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
import random

if __name__ == '__main__':
    rospy.init_node('xs_publisher', anonymous=True)
    pub = rospy.Publisher('/xs', Int16, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = random.randint(0, 100)
        pub.publish(msg)
        rate.sleep()