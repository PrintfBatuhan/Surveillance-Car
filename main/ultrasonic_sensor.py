#Batuhan DEDEOĞLU / 151024041

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import time 

class hcsr04:
    GPIO.setmode(GPIO.BCM) # Use physical pin numbering
    GPIO.setwarnings(False)        # To avoid warning messages because we don’t end
                               # the GPIO connection properly while interrupting the program
                               
    def __init__(self,trigger,echo):
        self.trigger=trigger
        self.echo=echo
        GPIO.setup(self.trigger, GPIO.OUT)  # Defining the 'trigger' pin:38 as an output pin
        GPIO.setup(self.echo, GPIO.IN)      # Defining the 'echo' pin:40 as an output pin

    def hcsr04_getdata(self):                   # Function to find distance
        GPIO.output(self.trigger, True)    # To set trigger to HIGH
        time.sleep(0.00001)           # Wait 10 microseconds
        GPIO.output(self.trigger, False)   # To set trigger to LOW
    
        start = time.time()           # Current time holders self
        stop = time.time()
    
        while GPIO.input(self.echo) == 0:  # Echo goes HIGH (until the wave is send)
            start = time.time()
    
        while GPIO.input(self.echo) == 1:  # The wave came back
           stop = time.time()
        
        total_time = stop - start           # Calculation of the total time of the wave 
        distance_both = total_time * 33112  # Travel distance by multiplying the total time by speed of sound
       # Divide the distance by 2 to get the actual distance
        distance = distance_both / 2
        return distance
    
    def stop(self) :
        GPIO.setmode(GPIO.BCM) # Use physical pin numbering
        GPIO.setwarnings(False)        # To avoid warning messages because we don’t end
               
        GPIO.cleanup( (self.trigger, self.echo) )
        


     




    
    