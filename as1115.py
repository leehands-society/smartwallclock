#################################
## Python Module from Leehands ##
#################################
from gpiozero import LED
from time import sleep
import smbus
import time


ld_AM_CA = LED(7)
ld_PM_CA = LED(8)
ld_ALARM_CA = LED(21)
ld_LCUC_AN = LED(16)
ld_LCUC_CA = LED(12)

CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY =	0x0A
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E


FND_HR_10 = 0x01
FND_HR_01 = 0x02
FND_MN_10 = 0x03
FND_MN_01 = 0x04


class AS1115:
    def __init__(self,addr):
        self.addr = addr
        self.bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
        self.cnt = 0
        self.now = time.localtime()
        ld_LCUC_AN.off()     # always GND

    
        self.bus.write_byte_data(self.addr,CTR_FEATURE, 0x02)
        sleep(0.01)
        self.bus.write_byte_data(self.addr,CTR_SHUTDOWN, 0x01)
        sleep(0.01)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY, 0x01)
        sleep(0.01)
        self.bus.write_byte_data(self.addr,CTR_FEATURE, 0x00)
        sleep(0.01)
        self.bus.write_byte_data(self.addr,CTR_SCANLIMIT, 0x07)
        sleep(0.01)
        self.bus.write_byte_data(self.addr,CTR_DECODEEN, 0xFF)

    def print_test(self):
        print("test ok")

    def AutoCount(self):

        if self.cnt > 1000 :
            self.cnt = 0
        else :
            self.cnt = self.cnt + 1

        self.bus.write_byte_data(self.addr,FND_HR_10, 1)
        self.bus.write_byte_data(self.addr,FND_HR_01, 2)
        self.bus.write_byte_data(self.addr,FND_MN_10, 3)
        self.bus.write_byte_data(self.addr,FND_MN_01, 4)

    def DisplayLocalTime(self):
        self.now = time.localtime()
               
        if self.now.tm_hour > 12 :
            ld_PM_CA.on()
            ld_AM_CA.off()
            dis_hour = self.now.tm_hour - 12
            
            self.bus.write_byte_data(self.addr,FND_HR_01, dis_hour%10)
            if dis_hour < 10:   
                dis_hour = 0x0F
            else :
                dis_hour = dis_hour/10
            self.bus.write_byte_data(self.addr,FND_HR_10, dis_hour)
        else :
            ld_PM_CA.off()
            ld_AM_CA.on()
            dis_hour = self.now.tm_hour
            self.bus.write_byte_data(self.addr,FND_HR_10, dis_hour/10)
            self.bus.write_byte_data(self.addr,FND_HR_01, dis_hour%10)

        self.bus.write_byte_data(self.addr,FND_MN_10, self.now.tm_min/10)
        self.bus.write_byte_data(self.addr,FND_MN_01, self.now.tm_min%10)

        if(self.now.tm_sec % 2):
            ld_ALARM_CA.on()
            ld_LCUC_CA.on() 
        else:
            ld_ALARM_CA.off()
            ld_LCUC_CA.off() 
    def Brighless(self,adc_input)
        





