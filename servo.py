# started on 9 AUG 2019
# Base script was provided by Nohara

import RPi.GPIO as GPIO
import time

class SG90_92R_Class:
    def __init__(self, Pin, ZeroOffsetDuty):
        self.mPin = Pin
        self.m_ZeroOffsetDuty = ZeroOffsetDuty
        GPIO.setup(self.mPin, GPIO.OUT)
        self.mPwm = GPIO.PWM(self.mPin , 50)

    def SetPos(self,pos):
        duty = (12-2.5)/180*pos+2.5 + self.m_ZeroOffsetDuty
        self.mPwm.start(duty)

    def Cleanup(self):
        self.SetPos(90)
        time.sleep(1)
        GPIO.setup(self.mPin, GPIO.IN)

def servo():
    GPIO.setmode(GPIO.BCM)
    Servo = SG90_92R_Class(Pin=4,ZeroOffsetDuty=0)
    Servo.SetPos(90)
    time.sleep(1)
    Servo.SetPos(150)
    time.sleep(1)
    Servo.SetPos(90)
    time.sleep(1)
    Servo.Cleanup()

if __name__ == '__main__':
    servo()
