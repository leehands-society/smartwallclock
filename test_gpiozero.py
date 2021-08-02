from gpiozero import LED
from time import sleep
import smbus

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

DEVICE_ADDRESS = 0x00
AS1115_CTR = 0x0F
AS1115_CTR_TEST = 0x01

buff = 0x03
ld_PWR = LED(17)
ld_STAT = LED(27)
ld_SYNC = LED(22)

bus.write_byte_data(DEVICE_ADDRESS,AS1115_CTR, 0x01)


print(buff)
while True:

    ld_PWR.on()
    ld_STAT.off()
    ld_SYNC.on()
    sleep(0.25)
    ld_PWR.off()
    ld_STAT.on()
    ld_SYNC.off()
    sleep(0.25)

