<p><img src="https://www.leehands.com/wp-content/uploads/2022/01/photo-2.jpg" alt="123" width="600" height="300" /></p>

<b>Target Board</b>
  <br>A. Raspberry Pi Zero W
  <br>B. FND Watch shield Board ( it's custom from Leehands )
  
  
<b> 1. TOOL CHAIN </b>

<font size = 7>sudo apt-get install git vim i2c-tools -y <br>
sudo pip3 install gpiozero smbus ftptool</font>


<b> 2. Enable I2C Interface by using "raspi-config" </b>

Typing in command line
  " ls /dev/*i2c* "<br>
  " i2cdetect -y -a 1 "<br>
   
<b> 3.excute python files  </b><br>
  " python3 main.py

<b> 4. Set Autostart </b><br>
  " sudo vim /etc/rc.local "<br>
  <br>
  add " sudo python3 /home/pi/smartwallclock/main.py & "<br>
