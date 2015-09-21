#! /bin/python
import subprocess
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mount", help="mount all partitions",
                    action="store_true", default="True")
parser.add_argument("-u", "--umount", help="unmount all partitions",
                    action="store_true")
args = parser.parse_args()

#proc = subprocess.Popen(['lsblk', '-f'], stdout=subprocess.PIPE)

#print(proc.communicate()[0])

blocks = subprocess.check_output(['lsblk', '-f'])

#print(type(blocks))
#print(blocks.decode("utf-8"))
#for line in blocks.split('\n'):
#    print(line.rstrip('\n'))

def get_device_directory_mapping():
    devices = []
    for line in blocks.decode("utf-8").split('\n'):
        oneline = line.split()
#        print(oneline)
        try:
            if oneline[1] == 'swap': continue
            devices.append((re.search("(?P<device>sda[0-9]*)", oneline[0]).groupdict()['device'], oneline[2]))
        except (IndexError, AttributeError):
            pass

    #print(devices)
    for a, b in devices:
        b = b.lower()
        a, b = "/dev/{}".format(a), "/mnt/{}".format(b)
        yield a, b

def mount(device, directory):
    if subprocess.getstatusoutput('grep {} /proc/mounts'.format(device))[0] == 1:
        print("mounting {} in {}".format(device, directory))
        subprocess.call("sudo mount {} {}".format(device, directory), shell=True)
    else:
        print('{} is already mounted'.format(device))

def umount(directory):
    try:
        grepout = subprocess.getstatusoutput(
    'grep {} /proc/mounts'.format(directory))[0] 
    except IndexError:
        print("{} is not mounted".format(directory))
        return 1
    if grepout == 0:
        print("unmounting {}".format(directory))
        subprocess.call("sudo umount {}".format(directory), shell=True)

for device, directory in get_device_directory_mapping():
 #   print(device, directory)
    if args.mount:
        mount(device, directory)
    if args.umount:
        umount(directory)
