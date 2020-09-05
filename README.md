# Balam
### Classical K'iche' jaguar

Boston Dynamics Spot inspired robot

* [Overview](#Overview)


## Overview
This project is the source code for a SpotMicroAI quadruped, a 4 legged open source robot. There are a few modification but the baseline quadruped is the SpotMicroAI 


### Hardware:

###### 3D printing
The model used is ThingVerse SpotMicro developed by KDY0523 (https://www.thingiverse.com/thing:3445283).
The plate adapted for the Jetson Nano can be found here: https://www.thingiverse.com/thing:3761340

###### Components:
* Computer: Nvidia Jetson Nano
* Front Camera: Intel Realsense camera D435i
* Servo control board: PCA9685, controlled via i2c
* Servos: 12 x MG996R
* LCD Panel: 16x2 i2c LCD panel
* Battery: 2s Lipo Battery 5200mah POVWAY 7.4V 50C
* UBEC: used as 5v voltage regulator to power pca9685 control board.



## SpotMicroAI Community
Visit the project website for more

Website: https://spotmicroai.readthedocs.io/en/latest/

Slack: https://spotmicroai-inviter.herokuapp.com/

Forum http://spotmicroai.org/

Repositories: https://gitlab.com/custom_robots/spotmicro
