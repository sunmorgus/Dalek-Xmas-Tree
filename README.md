Dalek Xmas Tree
===============

What would the holidays be without a little EXTERMINATE!!!

This repo will hold the script for running your own Dalek Christmas Tree, using python and a Rapsberry Pi!

Before getting started, there are some dependencies you need to install on your Rapsberry Pi (mostly to get sound working, plus adding the CWiid package for Wii Remote control):

	sudo apt-get install ca-certificates git binutils mpg123 python-cwiid
	
Then update the Pi's firmware:

	sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update 
	sudo rpi-update
	
Add the sound driver to /etc/modules

	snd_bcm2835
	
Reboot the Pi, then just download and run the dalek.py script:

	git clone http://
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