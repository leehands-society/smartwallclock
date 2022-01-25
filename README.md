<b> 1. TOOL CHAIN </b>

<font size = 7>sudo apt-get install git vim i2c-tools -y <br>
sudo pip3 install gpiozero smbus ftptool</font>


<b> 2. Enable I2C Interface by using "raspi-config" </b>

Typing in command line
  " ls /dev/*i2c* "
  " i2cdetect -y -a 1 "
   
<b> 3.excute python files  </b>
  " python3 main.py
