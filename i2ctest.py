from gpiozero import LED
from time import sleep
import smbus
import adc081
import as1115

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

buff = 0x03
ld_PWR = LED(17)
ld_STAT = LED(27)
ld_SYNC = LED(22)

adc = adc081.ADC081(0x52)
asfnd = as1115.AS1115(0x00)

while True:
    adc.readVoltage()
    sleep(0.25)
    asfnd.AutoCount()
    ld_PWR.on()
    ld_STAT.off()
    ld_SYNC.on()
    sleep(0.25)
    ld_PWR.off()
    ld_STAT.on()
    ld_SYNC.off()
    sleep(0.25)


