import RPi.GPIO as GPIO

MotorA1 = 18 
MotorA2 = 23 
MotorB1 = 24 
MotorB2 = 25 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(MotorA1,GPIO.OUT)
GPIO.setup(MotorA2,GPIO.OUT)
GPIO.setup(MotorB1,GPIO.OUT)
GPIO.setup(MotorB2,GPIO.OUT)



def forward():
    GPIO.output(MotorA1 , 1)
    GPIO.output(MotorA2 , 0)
    GPIO.output(MotorB1 , 0)
    GPIO.output(MotorB2 , 1)

def backward():
    GPIO.output(MotorA1 , 0)
    GPIO.output(MotorA2 , 1)
    GPIO.output(MotorB1 , 1)
    GPIO.output(MotorB2 , 0)

def turnRight():
    GPIO.output(MotorA1 , 1)
    GPIO.output(MotorA2 , 0)
    GPIO.output(MotorB1 , 1)
    GPIO.output(MotorB2 , 0)


def turnLeft():
    GPIO.output(MotorA1 , 0)
    GPIO.output(MotorA2 , 1)
    GPIO.output(MotorB1 , 0)
    GPIO.output(MotorB2 , 1)

def stop():
    GPIO.output(MotorA1 , 0)
    GPIO.output(MotorA2 , 0)
    GPIO.output(MotorB1 , 0)
    GPIO.output(MotorB2 , 0)
