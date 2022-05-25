# Flask Web Server Controlled Surveillance Car with  Raspberry Pi 4


<p align="center">
  <img width="42.2%" height="42.2%" src="https://user-images.githubusercontent.com/60669304/170241373-84cd21d2-a420-4adc-be6f-5e104ac136fa.jpg" /><img width="50%" height="50%" src="https://user-images.githubusercontent.com/60669304/170241402-10864f64-649e-4b13-86a8-6358e3d8f4d6.jpg" />
</p>

In this project, the mobile robot was designed by using various sensors and modules. The discovery robot, which can be controlled from the web interface designed as a user control panel, acts in accordance with the data coming from the user. There is also an obstacle avoiding autonomous robot mode.

<p align="center">
  <img width="50%" height="50%" src="https://user-images.githubusercontent.com/60669304/170247048-78fc0fb0-ee98-4d5d-a7c1-eecbafd1b204.jpg" />
  <img width="50%" height="50%" src="https://user-images.githubusercontent.com/60669304/170241434-dcc611b1-79f6-4e3a-8c91-6324c57fdbd2.jpg" />
</p>

Thanks to the ultrasonic distance sensor mounted on it, it can detect the obstacles in front of it, can detect the temperature and humidity value of the environment with the help of the heat and humidity sensor, and can transmit the image of the environment to the user simultaneously with the help of its camera from the control panel, thus allowing the user to get more detailed information about the robot's environment. It is aimed to design a reconnaissance robot that allows them to have information. In addition, the creation of an open source to create a mobile robot for education and research is one of the foundations of this purpose.

<p align="center">
  <img width="50%" height="50%" src="https://user-images.githubusercontent.com/60669304/170247631-5258bc7e-de03-48c1-ba1e-603bca3cf2ec.jpg" />
</p>

In the red numbered boxes on the exploration tool control panel;
1. The temperature and humidity information read by the DHT11 sensor is presented to the user through this panel,
2. It is the panel with simultaneous camera broadcast, 3. box shows the buttons that enable the camera to move in horizontal and vertical axes with the help of servo motors, 
4. It shows the buttons where the motion control of the reconnaissance vehicle is made.
 With the Autonomous button in the 5th box, the movement of the reconnaissance vehicle is provided independently of the user and continues its movement by avoiding the obstacles in front of it. The STOP button is used to end the autonomous mode. With the REFRESH button, the web application is restarted and the sensor data in Box 1 is updated.
