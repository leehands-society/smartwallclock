#from gpiozero import LED
from time import sleep
import smbus
import adc081
import time


adc = adc081.ADC081(0x50)

while True:
    adc.readVoltage()
    sleep(0.25)


