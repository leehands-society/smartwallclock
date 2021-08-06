#################################
## Python Module from Leehands ##
#################################

from time import sleep
import smbus


CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY =	0x0A
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E

FND_4 = 0x01
FND_3 = 0x06
FND_2 = 0x05
FND_1 = 0x07

class AS1115:
    def __init__(self,addr):
        self.addr = addr
        self.bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
        self.cnt = 0
    
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

        self.bus.write_byte_data(self.addr,FND_1, self.cnt)
        self.bus.write_byte_data(self.addr,FND_2, self.cnt%10)
        self.bus.write_byte_data(self.addr,FND_3, self.cnt%100)
        self.bus.write_byte_data(self.addr,FND_4, self.cnt%1000)



