#!/usr/bin/env python
import time
import random
import os

class Prob:
    def __init__(self):
        self.followdistribution()

    def connect(self, wifi):
        cmd = 'connect.py -w {}'.format(wifi)
        os.system(cmd)

    def followdistribution(self):
        oldwifi = ''
        while True:
            r = random.random()
            if r < .45:
                wifi = 'LoadDown2'
            elif r < .65:
                wifi = 'loaddown1'
            elif r < .85:
                wifi = 'loaddown3'
            else:
                wifi = '8'
            if wifi != oldwifi:
                self.connect(wifi)
                oldwifi = wifi
            print("Waiting in distribution", time.ctime(), r)
            time.sleep(2400)
            

p = Prob()