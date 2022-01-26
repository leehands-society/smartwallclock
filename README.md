<h1><strong>SMART WALL CLOCK</strong></h1>
<p><strong><img src="https://www.leehands.com/wp-content/uploads/2022/01/KakaoTalk_Photo_2022-01-26-12-36-17-1200x901.jpeg" alt="SmartwallClock" width="499" height="375" /></strong></p>
<h2><span style="color: #3366ff;">ENVIRONMENTS</span></h2>
<p>you need to two board is</p>
<p><strong>1) RASPBERRY PI ZERO W</strong></p>
<p><strong>2) FND AS1115 SHIELD BOARD</strong></p>
<p>FND AS1115 SHIELD Board is custom board from leehands.</p>
<p>&nbsp;</p>
<h2><span style="color: #3366ff;">GENERAL USAGE</span></h2>
<p>dd</p>

<code>
  <p>sudo apt-get update</p>
  <p>sudo apt-get upgrade -y</p>
</code>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>Binaries and Sources</h2>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 dir="auto">Docs</h2>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2 dir="auto">Thanks</h2>
<p>&nbsp;</p>


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
