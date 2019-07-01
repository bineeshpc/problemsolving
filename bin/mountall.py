#! /usr/bin/env python3
""" Originaly written for the dell laptop to run on arch linux platform
Modifying this for the vmware in the lg laptop for doing nfs mount
"""
import subprocess
import re
import argparse
import os


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mount", help="mount all partitions",
                        action="store_true", default=False)
    parser.add_argument("-u", "--umount", help="unmount all partitions",
                        action="store_true", default=False)
    args = parser.parse_args()
    return args

"""
commented out old code which might never be used again

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
"""



# Tried this in fstab
# did not work
# fstab mounts

#192.168.0.216:/mnt/westerndigital-2017/others/agile    /home/bineesh/remote/agile    nfs    defaults    0 0
#
#192.168.0.216:/mnt/transcend-2015/media/personal    /home/bineesh/remote/personal    nfs    defaults    0 0
#
#192.168.0.216:/mnt/seagate-2013/media/education    /home/bineesh/remote/education    nfs    defaults    0 0
#
#192.168.0.216:/mnt/seagate-2013/media/entertainment/Music    /home/bineesh/remote/music    nfs    defaults    0 0
#
#192.168.0.216:/mnt/seagate-2013/media/entertainment/Movies    /home/bineesh/remote/movies_seagate    nfs    defaults    0 0
#
#192.168.0.216:/mnt/transcend-2010/media/entertainment/Movies    /home/bineesh/remote/movies_transcend    nfs    defaults    0 0
#

def get_nfs_dirs():
    dirs = []
    try:
        data = subprocess.check_output(['showmount', '-e', '10.47.47.10'], timeout=5).decode("utf-8")
    except subprocess.TimeoutExpired:
        return dirs
    
    data = data.split('\n')
    for data in data:
        line = data.split()
        if len(line) == 2:
            dirs.append(line[0])
    return dirs


def infer_mount_dirs(dirs):
    home = os.environ['HOME']
    mount_dirs = []
    for dir_ in dirs:
        year = dir_.split('/')[2].split('-')[1]
        basename = os.path.basename(dir_)
        if basename == 'agile':
            basename = basename + '_remote'
        dirname = '{basename}_{year}'.format(year=year, basename=basename)
        dirname = os.path.join(home, 'remote', dirname).lower()
        mount_dirs.append(dirname)
    return mount_dirs
        

def mount(dirs):
    """ Mount all nfs directories """
    for original_dir, mount_dir in zip(dirs, infer_mount_dirs(dirs)):
        if not os.path.exists(mount_dir):
            os.mkdir(mount_dir)
        cmd = 'sudo mount -F 10.47.47.10:{original_dir} {mount_dir}'.format(original_dir=original_dir, mount_dir=mount_dir)
        print(cmd)
        os.system(cmd)
    

def umount(dirs):
    """ Mount all nfs directories """
    for mount_dir in infer_mount_dirs(dirs):
        if not os.path.exists(mount_dir):
            os.mkdir(mount_dir)
        
        cmd = 'sudo umount {mount_dir}'.format(mount_dir=mount_dir)
        print(cmd)
        os.system(cmd)

    

if __name__ == '__main__':
    args = parse_cmdline()
    nfs_dirs = get_nfs_dirs()
    if len(nfs_dirs) > 0:
        if args.mount:
            mount(nfs_dirs)
        if args.umount:
            umount(nfs_dirs)
