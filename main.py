import RPi.GPIO as GPIO
#from gpiozero import LED
import smbus
import adc081
import as1115
import time
import os

url = 'nas.nanots.co.kr'

previous_min = 0
bus = smbus.SMBus(0) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1


ld_PWR  = 11
ld_STAT = 13
ld_SYNC = 15

adc = adc081.ADC081(0x50)
asfnd = as1115.AS1115(0x00)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ld_PWR,GPIO.OUT)
GPIO.setup(ld_STAT,GPIO.OUT)
GPIO.setup(ld_SYNC,GPIO.OUT)

# POWER LED
GPIO.output(ld_PWR,False)
GPIO.output(ld_SYNC,True)

while True:

    Currenttime = time.localtime()

    if previous_min != Currenttime.tm_min :
        previous_min = Currenttime.tm_min
        response = os.system("ping -c 1 " + url)
        if response == 0:
          GPIO.output(ld_SYNC,False)
        else :
          GPIO.output(ld_SYNC,True)

    # STATUS LED
    if Currenttime.tm_sec%2 == 1 :
        GPIO.output(ld_STAT,True)
    else:
        GPIO.output(ld_STAT,False)
    # Read ADC (for bright)    
    buff = adc.readVoltage()
    asfnd.Brightless(buff)
    # Display Time clock
    asfnd.DisplayLocalTime(Currenttime)

    #debug
    #print("ADC : %.2f V , Time: %d: %d: %d " %(buff,Currenttime.tm_hour,Currenttime.tm_min,Currenttime.tm_sec))
    #print(" PING Response : %s" %(response))
    
    time.sleep(0.25)


