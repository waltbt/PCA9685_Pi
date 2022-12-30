![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
# PCA9685 16-Channel, 12-bit PWM/Servo Driver

The PCA9685 is an i2c, 16-Channel, 12-bit PWM/Servo Driver.  It allows you to independently control 16 devices with PWM signals.  

## Python code for the Raspberry Pi
This is a very basic program to allow you to use the PCA965 with a Raspberry Pi. It does not have any special features, but can easily be modified to include them.  The code is focused on driving servos and may need some changes to work with LEDs. The oscillator frequency varies with the board and must be calibrated.  It was written for Python 3.x, but should work for Python 2.x with minimal changes.  

## Calibration
Using an oscilloscope, monitor the output frequency of a channel.  Example: If the servo frequency is set to 50Hz, adjust the oscillator frequency until the output is 50Hz.  
Use the included program to aid in calibration.  

## SMBus
This program uses smbus.  Any recent version is likely to work as only basic functions are used.  
  
This project is licensed under the terms of the MIT license.  
