#! /usr/bin/env python2

import commands
import os
import time
import argparse
import sys

def getwifinames():
    wifinames_cmd = "connmanctl scan wifi && connmanctl services|grep -P 'loaddown|HomeNearPark|LoadDown|Furious'"
    wifis = {}
    for line in commands.getoutput(wifinames_cmd).split('\n')[1:]:
        try:
            ssidname, ssid = line.split()[-2:]
            wifis[ssidname] =  ssid
        except ValueError:
            #line did not have enough values to unpack
            pass
    return wifis

#getwifinames()

def is_connected():
    cmd = 'ping -c 4 google.com'
    count = 3
    #print 'checking connectivity'
    while count > 0:
        status, output = commands.getstatusoutput(cmd)
        if status == 0:
            return True
        else:
            count -= 1
            time.sleep(5)
    return False

def connect_to_specific(wifi):
    try:
        print "Trying to connect to", wifi
        connect_cmd = 'connmanctl connect {} && connmanctl state'.format(wifis[wifi])
        os.system(connect_cmd)
        if is_connected():
            print "connected to", wifi
            os.system('connmanctl services;ip addr')
            return True
    except KeyError:
        print wifi, "is not broadcasting now"
    return False
    
def connect(reversed=False, choice=False):
    preferred_order = ['LoadDown2', 'loaddown1', '8', 'loaddown3', 'HomeNearPark1']
    if reversed:
        preferred_order = preferred_order[::-1]
    if choice:
        for n, v in enumerate(preferred_order):
            print n, v 
        num = int(raw_input("Enter choice: "))
        preferred_order = [preferred_order[num]]
    wifis = getwifinames()
    print wifis
    for wifi in preferred_order:
        if connect_to_specific(wifi):
            return True
            
    return False
            



"""    
connmanctl scan wifi
connmanctl services
connmanctl connect wifi_9439e53b957f_486f6d654e6561725061726b31_managed_psk
connmanctl state
ip addr
ping -c 4 8.8.8.8
ping -c 4 google.com
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--reversed", help="mount all partitions",
                                            action="store_true")
    parser.add_argument("-c", "--choice", help="choose between the choices displayed",
                        action="store_true")
    parser.add_argument("-w", "--wifi", help="LoadDown2, loaddown1, loaddown3, HomeNearPark1")
    args = parser.parse_args()
    connected = False
    global wifis
    wifis = getwifinames()
    if args.wifi:
        connect_to_specific(args.wifi)
        sys.exit(0)
    count = 0
    if args.choice:
        connect(args.reversed, args.choice)

