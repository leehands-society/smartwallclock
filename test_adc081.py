#from gpiozero import LED
from time import sleep
import smbus
import adc081
import time

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

adc = adc081.ADC081(0x50)


while True:
    adc.readVoltage()
    sleep(0.25)


