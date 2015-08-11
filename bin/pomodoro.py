#! /usr/bin/env python
import easygui
import time

interval = 25
waittime = interval * 60
waittime_mins = waittime / 60
workinghours = 10000
numiters = int(workinghours * 60 / interval)
for i in range(numiters):
    timeslice = 10
    while waittime > 0:
        minutes = waittime / 60
        seconds = waittime - minutes * 60
        print "time remaining is {} minutes {} seconds".format(minutes, seconds)
        time.sleep(timeslice)
        waittime -= timeslice 
    easygui.msgbox('Time up {}.'.format(waittime_mins), 'Help Poor Bini')
