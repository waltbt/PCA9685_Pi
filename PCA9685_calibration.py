#!/usr/bin/env python3
"""
PCA9685_calibration.py
Function: Calibration of the oscillator on the PCA9685.
Author: Benjamin Walt
Date: 12/30/2022
Version: 0.1
"""

import PCA9685 as PCA # PWM driver
import time


pca = PCA.PCA9685(26000000)

pca.set_pwm(0,0,2048)
print("Current Frequency is 26.0MHz")
print("Response is to the first decimal place at best (Probably 2-300kHz only)")
while (True):
	new_freq = float(raw_input("New frequency (in Mhz): "))
	pca.set_oscillator_freq(int(new_freq*1000000))
	time.sleep(0.5)
	pca.set_pwm(0,0,2048)
