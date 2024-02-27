#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import mozgas2

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#motorok
bm = Motor(Port.B)
jm = Motor(Port.C)
km = Motor(Port.A)

#szenzorok
us = UltrasonicSensor(Port.S4)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)
gs = GyroSensor(Port.S2)

#motor kezelés
robot = DriveBase(jm, bm, 56, 132)
#előre
robot.straight(100)
wait(1)
#hátra
robot.straight(-100)
wait(1)
#jobbra
robot.turn(90)
#balra
wait(1)
robot.turn(-90)

mozgas2.foprogram(robot)
# Write your program here.
ev3.speaker.beep()
