import motors
from ultrasonic_sensor import hcsr04
import time

sensor = hcsr04(trigger = 6 , echo = 5)

 
def main():    # Main function
    while True:
        distance = sensor.hcsr04_getdata()
        if distance > 10:  # Not blink on led
            motors.forward()
        else :
            motors.stop()
            time.sleep(2)
            motors.turnLeft()
            time.sleep(1.5)
            motors.stop()
            time.sleep(2)


if __name__ == "__main__":
    main() #when your script is run directly, the main() function will be invoked