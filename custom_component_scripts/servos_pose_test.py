from adafruit_servokit import ServoKit
import board
import busio
import time

# On the Jetson Nano
# Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
# Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
# Default is to Bus 1; We are using Bus 0
print("Initializing Servos")
i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
print("Initializing ServoKit")
kit = ServoKit(channels=16, i2c=i2c_bus0)
# kit[0] is the bottom servo

def lay_down():
    ########### FEET ################
    # Rear rigth
    kit.servo[0].angle=180
    # Rear left
    kit.servo[1].angle=0
    # Front rigth
    kit.servo[2].angle=180
    # Front left
    kit.servo[3].angle=0

    time.sleep(0.5)

    ########### LEG ################
    kit.servo[4].angle=90
    kit.servo[5].angle=90
    kit.servo[6].angle=90
    kit.servo[7].angle=90
    time.sleep(0.5)

    ########### SHOULDER ################
    kit.servo[8].angle=90
    kit.servo[9].angle=90
    kit.servo[10].angle=90
    kit.servo[11].angle=90



def stand_up():
    ########### FEET ################
    # Rear rigth
    kit.servo[0].angle=140
    # Rear left
    kit.servo[1].angle=40
    # Front rigth
    kit.servo[2].angle=140
    # Front left
    kit.servo[3].angle=40
    time.sleep(0.5)
    ########### LEG ################
    # Right
    #kit.servo[4].angle=110
    #kit.servo[6].angle=110
    # Left
    #kit.servo[5].angle=70
    #kit.servo[7].angle=70


lay_down()
time.sleep(0.5)
stand_up()
time.sleep(1)
lay_down()