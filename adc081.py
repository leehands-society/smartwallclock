#################################
## Python Module from Leehands ##
#################################
import smbus

class ADC081:
    def __init__(self,addr):
        self.addr = addr
        self.bus = smbus.SMBus(0) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
    
    def print_test(self):
        print("test ok")

    def readVoltage(self):
        buff = self.bus.read_word_data(self.addr, 0x00)
        MSB = (buff << 4) & 0x00F0
        LSB = (buff >> 12) & 0x000F
        buff = MSB | LSB
        buff = buff *(3.3 / 256)
        #print("ADC : %.2f V" %(buff))
        return buff

