#!/usr/bin/sh
file=/tmp/videodownload.pid

if [ ! -f $file ]
then
    #echo "Starting download"
    #cd /mnt/win7/topics && ./videodownload.py >> /tmp/videodownload.log 2>&1 &
    sleep 1
    pid=$(ps -ef|grep [n]ew.py|awk '{print $2}')
    echo $pid > $file
    python send_public_ip.py
else
    cat $file
    echo "Doing nothing because pid already exist"
fi
