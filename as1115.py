#################################
## Python Module from Leehands ##
#################################
from gpiozero import LED
from time import sleep
import smbus
import time


ld_DP = LED(14)
ld_PM = LED(15)
ld_AM = LED(18)
ld_LUC = LED(23)
ld_ALM = LED(24)


CTR_SHUTDOWN =	0x0C
CTR_DECODEEN =	0x09
CTR_INTENSITY_GLOBAL    = 0x0A   #0xx0 (min) ~ 0xxF (max)
CTR_INTENSITY_DIGI10    = 0x10   #DIGI1 (xH), DIGI0 (Hx)
CTR_INTENSITY_DIGI32    = 0x11   #DIGI3 (xM), DIGI2 (Mx)
CTR_INTENSITY_DIGI54    = 0x12   #DIGI5 (Sx), DIGI4 (DOT)
CTR_INTENSITY_DIGI76    = 0x13   #DIGI7 (XX), DIGI6 (xS)
CTR_SCANLIMIT =	0x0B
CTR_FEATURE =	0x0E


FND_HR_10 = 0x01
FND_HR_01 = 0x02
FND_MN_10 = 0x03
FND_MN_01 = 0x04
FND_SS_10 = 0x06
FND_SS_01 = 0x07
FND_AC_01 = 0x05


class AS1115:
    def __init__(self,addr):
        self.addr = addr
        self.bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
        self.cnt = 0
        self.previous_min = 0;
        self.defaultbright = 0x1
        self.bright_avg = [1,1,1] # 3 value array

        ld_DP.off()
        ld_PM.off()
        ld_AM.off()
        ld_LUC.off()     
        ld_ALM.off()
    
        self.bus.write_byte_data(self.addr,CTR_FEATURE, 0x02)
        self.bus.write_byte_data(self.addr,CTR_SHUTDOWN, 0x01)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI10, self.defaultbright<<4 | self.defaultbright)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI32, self.defaultbright<<4 | self.defaultbright)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI54, self.defaultbright)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI76, 0x00)
        self.bus.write_byte_data(self.addr,CTR_FEATURE, 0x00)
        self.bus.write_byte_data(self.addr,CTR_SCANLIMIT, 0x07)
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

    def DisplayLocalTime(self,time):      

        # SECOND
        self.bus.write_byte_data(self.addr,FND_SS_10,(int)(time.tm_sec/10))
        self.bus.write_byte_data(self.addr,FND_SS_01,(int)(time.tm_sec%10))
        # DOT
        if(time.tm_sec%2):
            ld_LUC.on()
        else:
            ld_LUC.off()

        # CHECK to update
        if self.previous_min != time.tm_min:
            self.previous_min = time.tm_min
            # HOUR
            if time.tm_hour >= 12 :
                ld_PM.off()
                ld_AM.on()
                if time.tm_hour == 12 :
                  dis_hour = 12
                else :
                  dis_hour = time.tm_hour - 12
                
                self.bus.write_byte_data(self.addr,FND_HR_01,(int)(dis_hour%10))
                if dis_hour < 10:   
                    dis_hour = 0x0F
                else :
                    dis_hour = (int)(dis_hour/10)
                    
                self.bus.write_byte_data(self.addr,FND_HR_10, dis_hour)
            else : # < 12
                ld_PM.on()   # LED OFF
                ld_AM.off()  # LED ON
                
                # if midnight , display is 12
                if time.tm_hour == 0 :
                  dis_hour = 12
                else :
                  dis_hour = time.tm_hour
                  
                if dis_hour < 10 :
                    self.bus.write_byte_data(self.addr,FND_HR_10,0x0F)
                else:
                    self.bus.write_byte_data(self.addr,FND_HR_10,(int)(dis_hour/10))
                
                self.bus.write_byte_data(self.addr,FND_HR_01,(int)(dis_hour%10))

            # MINITE
            self.bus.write_byte_data(self.addr,FND_MN_10,(int)(time.tm_min/10))
            self.bus.write_byte_data(self.addr,FND_MN_01,(int)(time.tm_min%10))
        
               
    def Brightless(self, adcinput):
        buff = (int)((float)(adcinput / 1.4) * 16)
        if buff < 0 :
            buff = 0
        
        self.bright_avg[0] = self.bright_avg[1]
        self.bright_avg[1] = self.bright_avg[2]
        self.bright_avg[2] = buff
        
        buff = (int)((self.bright_avg[0] + self.bright_avg[1] + self.bright_avg[2]) / 3)
        #print (buff)
        brightvalue = self.defaultbright + buff;
        if brightvalue > 0x0F :
            brightvalue = 0x0F
        
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI10, brightvalue<<4 | brightvalue)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI32, brightvalue<<4 | brightvalue)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI54, brightvalue)
        self.bus.write_byte_data(self.addr,CTR_INTENSITY_DIGI76, 0x00)
