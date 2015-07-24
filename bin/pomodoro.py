#! /usr/bin/env python
import easygui
import time

interval = 25
waittime = interval * 60
waittime_mins = waittime / 60
workinghours = 10000
numiters = workinghours * 60 / interval
for i in range(numiters):
    time.sleep(waittime)
    easygui.msgbox('Time up {}.'.format(waittime_mins), 'Help Poor Bini')
