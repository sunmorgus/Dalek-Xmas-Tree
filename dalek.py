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
import pyaudio
import mad
import audioop
from subprocess import call
from random import randrange

#-- end imports

#-- utility functions

#// Wii Remote Connect Function
def connectWiiRemote():
    wiimote = None
    attempts = 1
    
    while not wiimote:
        call("clear")
        status = "Waiting for Wii Remote to Connect..."
        print status
        try:
            wiimote = cwiid.Wiimote()
            # turn on wiimote led, to indicate that we've started up correctly
            wiimote.led = 1
            
            # set the report mode to button, so we can capture button events
            wiimote.rpt_mode = cwiid.RPT_BTN
            playAudio("Beep", 2, wiimote)
            
            return wiimote
        except RuntimeError:
            if attempts > 5:
                break
            
            attempts += 1
#// end Wii Remote Connect Function

#// Beep function (used for notifications)
#// This function is disabled for now...it was
#// too annoying! lol
def beep(loop):
    i = loop #when ready to re-enable, set i = 0
    mf = []
    while i < loop:
        mf.append(mad.MadFile(directory + "beep.mp3"))
        i += 1
        
    return mf
#// end beep function

#// Get Audio Function
def getAudioFile():    
    l = len(files)
    i = randrange(l + 1) # add one here when adding combined audio files
    mf = []
    
    if i <= (l - 1):
        mf.append(mad.MadFile(directory + files[i]))
    else: #combined audio files
        mf.append(mad.MadFile(directory + files[4]))
        mf.append(mad.MadFile(directory + files[0]))
        mf.append(mad.MadFile(directory + files[0]))
        mf.append(mad.MadFile(directory + files[0]))
    
    return mf
    
#// end get audio function

#// Plays the given audio file using pyaudio
#// Expects array of pymad File Objects
def playAudio(snd = "Dalek", loop = 0, wiimote = None):
    if snd == "Dalek":
        madFiles = getAudioFile()
    else:
        madFiles = beep(loop)
        if wiimote != None:
            rpt = 1
            while rpt <= loop:
                wiimote.rumble = 0
                for i in range(0, 3):
                    time.sleep(0.1)
                    wiimote.rumble = (i % 2)
                rpt += 1
        
    for mf in madFiles:
        p = pyaudio.PyAudio()
        
        #CHUNK = 1024
        
        # open stream
        stream = p.open(format = p.get_format_from_width(pyaudio.paInt32),
                        channels = 2,
                        rate = mf.samplerate(),
                        output = True)
        
        # read data
        data = mf.read()
        
        # play stream
        while data != None:
            stream.write(data)
            rms = audioop.rms(data, 2)
#            if rms > 11500:
#                print "ON"
#            else:
#                print "OFF"
            data = mf.read()
        
        stream.close()
        p.terminate()
        
        call("clear")
        print "OFF"
    
#// end play audio

#-- end utility functions

#-- main loop function

def mainLoop():
    wiimote = None
    
    playAudio("Beep", 1, wiimote)

    while True:
        call("clear")
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
                playAudio("Beep", 3, wiimote)
                wiimote.close()
                wiimote = None
            
            if buttons == (cwiid.BTN_B + cwiid.BTN_HOME):
                #print "Closing Script!"
                playAudio("Beep", 4, wiimote)
                wiimote.close()
                wiimote = None
                quit()
        try:
            time.sleep(0.2)
        except KeyboardInterrupt:
            exit()
        
#-- end main loop

#-- setup global variables

#// directory for sound files
global directory

#// array of sound files to play
global files

#// status message
global status

directory = "snd/"

files = []
files.append("riley_exterminate.mp3")
files.append("nat_exterminate.mp3")
files.append("aiden_sonic_screwdriver.mp3")
files.append("nat_doctor_who.mp3")
files.append("riley_doctor_detected.mp3")
files.append("riley_doctor_who.mp3")
files.append("riley_kill_the_doctor.mp3")
files.append("riley_tick_tock.mp3")

#-- end global variables

#-- Start Main Loop

mainLoop()

#-- end start main loop
