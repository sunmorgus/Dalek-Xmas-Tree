Dalek Xmas Tree
===============

What would the holidays be without a little EXTERMINATE!!!

This repo will hold the script for running your own Dalek Christmas Tree, using python and a Rapsberry Pi! More information about this project can be found here: http://dev.csbctech.com/dalek/wordpress

Before getting started, there are some dependencies you need to install on your Rapsberry Pi (mostly to get sound working, plus adding the CWiid package for Wii Remote control):

	sudo apt-get install ca-certificates git binutils mpg123 python-cwiid
	
Then update the Pi's firmware:

	sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update 
	sudo rpi-update
	
Add the sound driver to /etc/modules

	snd_bcm2835
	
Reboot the Pi, then just download and run the dalek.py script:

	git clone git://github.com/sunmorgus/Dalek-Xmas-Tree.git
	chmod u+x dalek.py
	./dalek.py
	
I've included some sound files in the snd directory; feel free to delete them and add your own. If you do, just update the files array with the appropriate file names. Also, make sure you update the directory variable if you didn't check out to the pi user's home directory:

	def mainLoop():
	    wiimote = None
	    directory = "/home/pi/snd/"
	
	    files = []
	    files.append("riley_exterminate.mp3")
	    files.append("nat_exterminate.mp3")
	    files.append("aiden_sonic_screwdriver.mp3")
	    files.append("nat_doctor_who.mp3")
	    files.append("riley_doctor_detected.mp3")
	    files.append("riley_doctor_who.mp3")
	    files.append("riley_kill_the_doctor.mp3")
	    files.append("riley_tick_tock.mp3")

NOTE: If you are running this script via ssh, it's helpful to launch it in a screen first, so the script will continue to run after you've closed the ssh connection. After starting the script, just hit ctrl-A + D to detach from the screen, then you can exit the ssh connection and the script will continue on. More info on using screen can be found here https://help.ubuntu.com/community/Screen.

I have plans to convert this script to run as a daemon, which will hopefully negate the need to use screen.