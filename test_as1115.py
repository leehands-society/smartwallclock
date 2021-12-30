from time import sleep
from gpiozero import LED
import smbus

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1


ld_DP = LED(14)
ld_PM = LED(15)
ld_AM = LED(18)
ld_LUC = LED(23)
ld_ALM = LED(24)

CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY_GLOBAL  =	0x0A    #0xx0 (min) ~ 0xxF (max)
CTR_INTENSITY_DIGI10   = 0x10   #DIGI1 (xH), DIGI0 (Hx)
CTR_INTENSITY_DIGI32   = 0x11   #DIGI3 (xM), DIGI2 (Mx)
CTR_INTENSITY_DIGI54   = 0x12   #DIGI5 (Sx), DIGI4 (DOT)
CTR_INTENSITY_DIGI76   = 0x13   #DIGI7 (XX), DIGI6 (xS)
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E

FND_HR_10 = 0x01
FND_HR_01 = 0x02
FND_MN_10 = 0x03
FND_MN_01 = 0x04
FND_SS_10 = 0x06
FND_SS_01 = 0x07
FND_AC_01 = 0x05

bus.write_byte_data(0x00,CTR_FEATURE, 0x02)
sleep(0.01)
bus.write_byte_data(0x00,CTR_SHUTDOWN, 0x01)
sleep(0.01)
bus.write_byte_data(0x00,CTR_INTENSITY_GLOBAL, 0x08)
sleep(0.01)
bus.write_byte_data(0x00,CTR_INTENSITY_DIGI76, 0x00)
bus.write_byte_data(0x00,CTR_INTENSITY_DIGI54, 0x0A)
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
    bus.write_byte_data(0x00,FND_AC_01, 8)
    ld_DP.off()
    ld_PM.off()
    ld_AM.off()
    ld_LUC.off()
    ld_ALM.off()
    sleep(0.5)
    bus.write_byte_data(0x00,FND_HR_10, 6)
    bus.write_byte_data(0x00,FND_HR_01, 5)
    bus.write_byte_data(0x00,FND_MN_10, 4)
    bus.write_byte_data(0x00,FND_MN_01, 3)
    bus.write_byte_data(0x00,FND_SS_10, 2)
    bus.write_byte_data(0x00,FND_SS_01, 1)
    bus.write_byte_data(0x00,FND_AC_01, 0)
    ld_DP.on()
    ld_PM.on()
    ld_AM.on()
    ld_LUC.on()
    ld_ALM.on()


