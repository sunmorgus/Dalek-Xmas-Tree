#! /usr/bin/python
#-------------------------------------------------------------------------------
# Name:        Dalek Control
# Purpose:     This script will be used to control firs the Dalek Xmas tree,
#              then, in the future, the Dalek Robot. It will allow the dalek
#              to be connected to a wiimote for activation, and will produce
#              sounds (as well as other future activities) depending on button
#              presses from the wiimote (and perhaps other external interfaces
#              in the future).
#
# Author:      Nicklas DeMayo
#
# Created:     12/06/2012
# Copyright:   (c) Nicklas 2012
#-------------------------------------------------------------------------------

#-- imports
import cwiid
import time
import os
from subprocess import call
from random import randrange

#-- end imports

#-- setup global variables
#// CWiid Wiimote Object
global wiimote

#// directory for sound files
global directory

#// array of sound files to play
global files

#// status message
global status

#-- end global variables

#-- utility functions

#// Wii Remote Connect Function
def connectWiiRemote():
    wiimote = None
    attempts = 1
    
    while not wiimote:
        os.system("clear")
        status = "Waiting for Wii Remote to Connect..."
        print status
        try:
            wiimote = cwiid.Wiimote()
            # turn on wiimote led, to indicate that we've started up correctly
            #print "Wii Remote Connected!"
            wiimote.led = 1
            
            # set the report mode to button, so we can capture button events
            wiimote.rpt_mode = cwiid.RPT_BTN
            beep(2)
            
            return wiimote
        except RuntimeError:
            if attempts > 5:
                #print "Cannot create connection to Wiimote"
                break
            #print "Error creating connection to wiimote"
            #print "Attempt(s): {0}".format(attempts)
            attempts += 1
#// end Wii Remote Connect Function

#// Beep function (used for notifications)
#// This function is disabled for now...it was
#// too annoying! lol
def beep(loop):
    i = loop
    while i < loop:
        call(["mpg123", "-q", "beep.mp3"])
        i += 1
#// end beep function

#// Play Audio Function
def playAudio():
    #print "Playing Audio File"
    
    l = len(files)
    i = randrange(l + 1) # add one here when adding combined audio files
    #print "Length: {0} - i: {1}".format(l, i)
    
    if i <= (l - 1):
        #print "Single"
        call(["mpg123", "-q", files[i]])
    else: #combined audio files
        #print "Combined"
        call(["mpg123", "-q", files[4], files[0], files[0], files[0]])
#// end play function

#-- end utility functions


#-- main loop function

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
    
    #run(webApp, host='localhost', port=8080)
    
    beep(1)
    
    while True:
        os.system("clear")
        if wiimote == None:
            wiimote = connectWiiRemote()
        else:
            status = "Wii Remote Connected, Waiting for Commands..."
            print status
            buttons = wiimote.state["buttons"]
    
            if buttons == cwiid.BTN_A:
                #play random sound
                playAudio()
                #print "Button A Pressed!"

            if buttons == cwiid.BTN_HOME:
                #print "Shutting Wii Remote Off!"
                wiimote.close()
                wiimote = None
                beep(3)
            
            if buttons == (cwiid.BTN_B + cwiid.BTN_HOME):
                #print "Closing Script!"
                wiimote.close()
                wiimote = None
                beep(4)
                quit()
            
        time.sleep(0.2)
        
#-- end main loop


#-- Start Main Loop

mainLoop()

#-- end start main loop
