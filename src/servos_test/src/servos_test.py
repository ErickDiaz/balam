#!/usr/bin/env python3

import rospy
import board
import busio
import time
import yaml
from adafruit_servokit import ServoKit

def load_configuration(file_name):
    rospy.loginfo('Loading configuration ...')

    with open(file_name) as f:
        config = yaml.load(f, Loader=yaml.BaseLoader)
    rospy.loginfo('Done loading configuration')

    return config

def init_servo_driver():
    """
    On the Jetson Nano
    Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
    Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
    Default is to Bus 1; We are using Bus 0
    """
    rospy.loginfo("Initializing Servos")
    i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
    rospy.loginfo("Initializing ServoKit")
    kit = ServoKit(channels=16, i2c=i2c_bus0)
    rospy.loginfo("Done initializing")


def nodo():
    """
    Testing servos in rest and stand position
    """

    # Set up and title the ros node for this code
    rospy.init_node('servos_test')
    rospy.loginfo('===== Init servo testing =====')
    rospy.loginfo('Loading configuration ...')

    balam_config = load_configuration('config/balam.yaml')
    init_servo_driver()


    

if __name__ == '__main__':
    try:
        nodo()
    except:
        rospy.loginfo("Error on node for testing servos")
        pass