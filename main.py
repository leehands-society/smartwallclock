from gpiozero import LED
from time import sleep
import smbus
import adc081
import as1115
import time

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

buff = 0x03
ld_PWR = LED(17)
ld_STAT = LED(27)
ld_SYNC = LED(22)
ld_DP_CA = LED(20)

adc = adc081.ADC081(0x52)
asfnd = as1115.AS1115(0x00)


        #
ld_DP_CA.off()


while True:
    buff = adc.readVoltage()
    #print("ADC : %.2f V" %(buff))
    asfnd.DisplayLocalTime()
    asfnd.Brightless(buff)
    sleep(0.25)


