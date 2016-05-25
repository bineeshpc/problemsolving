lsblk -f
echo "read which hard disk to mount"
#read harddisk
harddisk=/dev/sdb1
mountpoint=/mnt/transcend
echo $harddisk
sudo umount $harddisk
ls /mnt
echo "read the mountpoint: select from above directories if necessary eg:/mnt/transcend"
#read mountpoint
echo $mountpoint
sudo mount $harddisk $mountpoint
ls $mountpoint
