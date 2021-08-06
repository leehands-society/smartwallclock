#################################
## Python Module from Leehands ##
#################################
import smbus

class ADC081:
    def __init__(self,addr):
        self.addr = addr

    def readVoltage(self):
        buff = bus.read_word_data(self.addr, 0x00)
        MSB = (buff << 4) & 0x00F0
        LSB = (buff >> 12) & 0x000F
        buff = MSB | LSB
        buff = buff *(3.3 / 256)
        print("ADC : %.2f V" %(buff))

