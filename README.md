<h1><strong>SMART WALL CLOCK</strong></h1>
<p><strong><img src="https://www.leehands.com/wp-content/uploads/2022/01/KakaoTalk_Photo_2022-01-26-12-36-17-1200x901.jpeg" alt="SmartwallClock" width="499" height="375" /></strong></p>
<br> Requires internet connection and syncs via internet watch.
<br> Very accurate time display.
<h2><span style="color: #3366ff;">ENVIRONMENTS</span></h2>
<p>you need to two board is</p>
<p><strong>1) BANANA PI M2 ZERO</strong></p>
<p><strong>2) FND AS1115 SHIELD BOARD</strong></p>
<p><strong>3) Case from 3D Printer</strong></p>
<p>FND AS1115 SHIELD Board is custom board from leehands.</p>
<br>if want shield board, will buy through my shop.
<p>&nbsp;</p>
<h2><span style="color: #3366ff;">GENERAL USAGE</span></h2>
<br>Armbian image can be download : Armbian_20.02.3_Bananapim2zero_buster_current_5.4.18_desktop
<br>you can download below link : <a href ="https://drive.leehands.com/d/f/668800049513282149">Download</a>
<br>
<br>Basic Update
<br><code>sudo apt-get update</code>
<br><code>sudo apt-get upgrade -y</code>
<br><code>sudo apt-get install i2c-tools</code>
<br><code>sudo apt-get install python3-pip</code>
<br><code>sudo apt-get install build-essential python3-dev python3-smbus</code>
<br> https://github.com/leehands-society/RPi.GPIO
<br><code>sudo pip3 install smbus </code>
<br>
<br>Enable I2C Interface by using <code>armbian-config</code>
<img src="https://www.leehands.com/wp-content/uploads/2022/02/20220208_Rpi.GPIO_3.jpg" alt="SmartwallClock" width="499" height="275" />
<br>should check i2c0 and w1-gpio
<br>
<br><code>ls /dev/*i2c*</code>
<br><code>i2cdetect -y -a 1</code>
<br>
<br>Clone repository
<br><code>git clone https://github.com/leehands-society/smartwallclock.git </code>
<br>
<br>Excute
<br><code>python3 main.py</code>
<br>
<br>Set Auto Start program
<br><code>sudo python3 /home/pi/smartwallclock/main.py &</code>
<br>
<h2>Binaries and Sources</h2>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 dir="auto">Docs</h2>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 dir="auto">Thanks</h2>
<p>&nbsp;</p>

