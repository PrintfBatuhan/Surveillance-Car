"""
    Gebze Technical University Faculty of Electronic Engineering
                        Graduation Project
    
                 Surveillance/Exploration Robot
                 
             Developed by Batuhan Dedeoğlu / 151024041
"""

#Importing required libraries.---------------------------------------------------------------------------

from flask import Flask, render_template, Response
from ultrasonic_sensor import hcsr04
from camera_pi import Camera
import RPi.GPIO as GPIO
import Adafruit_DHT
import motors
import time
import os

app = Flask(__name__)  #Creating a Flask object called app.




# Global variables definition and initialization.--------------------------------------------------------
sensor = hcsr04(trigger = 6 , echo = 5)
global horizonal
global vertical
horizonal = 90
vertical = 90





# Creating of necessary functions.-----------------------------------------------------------------------

def gen(camera): # Video streaming generator function.
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

def DHT11_data(): # Getting data from DHT11 sensor.
    DHT11 = Adafruit_DHT.DHT11
    DHT_pin = 16
    hum, temp = Adafruit_DHT.read_retry(DHT11, DHT_pin)
    return temp, hum




# App routing to provide Surveillance/Exploration Robot "LIVE STREAM CAMERA"-----------------------------

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# App routing to provide Surveillance/Exploration Robot "DIRECTION" control--------------------------------

@app.route('/left')
def left():
    motors.turnLeft()
    return render_template('index.html')

@app.route('/right')
def right():
   motors.turnRight()
   return render_template('index.html')

@app.route('/forward')
def forward():
   motors.forward()
   return render_template('index.html')

@app.route('/backward')
def backward():
    motors.backward()
    return render_template('index.html')

@app.route('/stop')
def stop():
   motors.stop()
   return  render_template('index.html')  



# App routing to provide Surveillance/Exploration Robot "CAMERA" Direction control-----------------------

@app.route("/<servo>/<angle>")
def move(servo, angle):
    global horizonal
    global vertical
    
    servo1_pin = 27
    servo2_pin = 22
    
    if servo == 'horizonal_angle':
        if angle == '+':
            horizonal = horizonal - 45
        else:
            horizonal = horizonal + 45
        os.system("python3 servo.py " + str(servo1_pin) + " " + str(horizonal))
    
    if servo == 'vertical_angle':
        if angle == '+':
            vertical = vertical - 10
        else:
            vertical = vertical + 10
        os.system("python3 servo.py " + str(servo2_pin) + " " + str(vertical))
    
    return render_template('index.html')

@app.route('/mode1')
def on():    # Main function
    sensor = hcsr04(trigger = 6 , echo = 5)
    while True:
        distance = sensor.hcsr04_getdata()
        if distance > 12:  
            motors.forward()
        else :
            motors.stop()
            time.sleep(0.5)
            motors.backward()
            time.sleep(0.5)
            motors.stop()
            time.sleep(2)
            motors.turnLeft()
            time.sleep(1)

    return render_template('index.html')

@app.route('/mode2')
def off():
    sensor = hcsr04(trigger = 6 , echo = 5)
    sensor.stop()
    while True:        
        motors.stop()
        time.sleep(2)
        motors.stop()
        break
      

    return render_template('index.html')
# App routing to get sensor and servo motors datas-------------------------------------------------------

@app.route('/')
def index():
    temp, hum = DHT11_data() 
    Data = {'temp':temp, 'hum':hum, 'horizonal'  : horizonal,'vertical' : vertical}
    
    return render_template('index.html', **Data)


if __name__ == '__main__': 
    app.run(debug=False, host='0.0.0.0') #host="0.0.0.0" will make the page accessable
    
#----------------------------------------------END-------------------------------------------------------