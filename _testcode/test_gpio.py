from gpiozero import LED
from time import sleep

ld_PWR = LED(17)
ld_STAT = LED(27)
ld_SYNC = LED(22)

while True:

    ld_PWR.on()
    ld_STAT.off()
    ld_SYNC.on()
    sleep(0.25)
    ld_PWR.off()
    ld_STAT.on()
    ld_SYNC.off()
    sleep(0.25)

