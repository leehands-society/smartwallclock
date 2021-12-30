from gpiozero import LED
import smbus
import adc081
import as1115
import time
import os

url = 'nas.nanots.co.kr'

previous_min = 0
bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1

ld_PWR  = LED(22)
ld_STAT = LED(27)
ld_SYNC = LED(17)

adc = adc081.ADC081(0x50)
asfnd = as1115.AS1115(0x00)

# POWER LED
ld_PWR.off()
ld_SYNC.on()

while True:

    Currenttime = time.localtime()

    if previous_min != Currenttime.tm_min :
        previous_min = Currenttime.tm_min
        response = os.system("ping -c 1 " + url)
        if response == 0:
           ld_SYNC.off()
        else :
           ld_SYNC.on()

    # STATUS LED
    if Currenttime.tm_sec%2 == 1 :
        ld_STAT.off()
    else:
        ld_STAT.on()
    # Read ADC (for bright)    
    buff = adc.readVoltage()
    asfnd.Brightless(buff)
    # Display Time clock
    asfnd.DisplayLocalTime(Currenttime)

    #debug
    #print("ADC : %.2f V , Time: %d: %d: %d " %(buff,Currenttime.tm_hour,Currenttime.tm_min,Currenttime.tm_sec))
    #print(" PING Response : %s" %(response))
    
    time.sleep(0.25)


