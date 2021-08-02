from gpiozero import LED
from time import sleep
import smbus

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

DEVICE_ADDRESS = 0x00

CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY =	0x0A
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E

buff = 0x03
ld_PWR = LED(17)
ld_STAT = LED(27)
ld_SYNC = LED(22)

bus.write_byte_data(DEVICE_ADDRESS,CTR_FEATURE, 0x02)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,CTR_SHUTDOWN, 0x01)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,CTR_INTENSITY, 0x01)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,CTR_FEATURE, 0x00)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,CTR_SCANLIMIT, 0x07)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,CTR_DECODEEN, 0xFF)
sleep(0.1)
bus.write_byte_data(DEVICE_ADDRESS,0x00,0x0D)


while True:

    buff = bus.read_byte_data(DEVICE_ADDRESS, 0x1C)
    print(buff)
    ld_PWR.on()
    ld_STAT.off()
    ld_SYNC.on()
    sleep(0.25)
    ld_PWR.off()
    ld_STAT.on()
    ld_SYNC.off()
    sleep(0.25)


