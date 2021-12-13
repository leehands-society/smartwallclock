from time import sleep
import smbus

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1


CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY_GLOBAL  =	0x0A
CTR_INTENSITY_DIGI10   = 0x10
CTR_INTENSITY_DIGI32   = 0x11
CTR_INTENSITY_DIGI54   = 0x12
CTR_INTENSITY_DIGI76   = 0x13
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E

FND_HR_10 = 0x01
FND_HR_01 = 0x02
FND_MN_10 = 0x03
FND_MN_01 = 0x04
FND_SS_10 = 0x06
FND_SS_01 = 0x07

bus.write_byte_data(0x00,CTR_FEATURE, 0x02)
sleep(0.01)
bus.write_byte_data(0x00,CTR_SHUTDOWN, 0x01)
sleep(0.01)
bus.write_byte_data(0x00,CTR_INTENSITY_GLOBAL, 0x08)
sleep(0.01)
bus.write_byte_data(0x00,CTR_INTENSITY_DIGI76, 0x00)
bus.write_byte_data(0x00,CTR_INTENSITY_DIGI54, 0x00)
sleep(0.01)
bus.write_byte_data(0x00,CTR_FEATURE, 0x00)
sleep(0.01)
bus.write_byte_data(0x00,CTR_SCANLIMIT, 0x07)
sleep(0.01)
bus.write_byte_data(0x00,CTR_DECODEEN, 0xFF)


while True:
    sleep(0.5)
    bus.write_byte_data(0x00,FND_HR_10, 1)
    bus.write_byte_data(0x00,FND_HR_01, 2)
    bus.write_byte_data(0x00,FND_MN_10, 3)
    bus.write_byte_data(0x00,FND_MN_01, 4)
    bus.write_byte_data(0x00,FND_SS_10, 5)
    bus.write_byte_data(0x00,FND_SS_01, 6)
    sleep(0.5)
    bus.write_byte_data(0x00,FND_HR_10, 6)
    bus.write_byte_data(0x00,FND_HR_01, 5)
    bus.write_byte_data(0x00,FND_MN_10, 4)
    bus.write_byte_data(0x00,FND_MN_01, 3)
    bus.write_byte_data(0x00,FND_SS_10, 2)
    bus.write_byte_data(0x00,FND_SS_01, 1)


