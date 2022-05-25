from time import sleep
import RPi.GPIO as GPIO

fPWM = 50  

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def servo_direction(servo, angle):
    
    assert angle >=0 and angle <= 180
    pwm = GPIO.PWM(servo, fPWM)
    pwm.start(0)
    dutyCycle = angle / 18. + 2.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.15)
    pwm.stop()

if __name__ == '__main__':
    import sys
    servo = int(sys.argv[1])
    GPIO.setup(servo, GPIO.OUT)
    servo_direction(servo, int(sys.argv[2]))
    GPIO.cleanup()