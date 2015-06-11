from threading import Timer, Thread
from Queue import Queue
import commands
import datetime
import os
import psutil
import time
import pdb
import logging

# create logger with 'profiler_application'
logger = logging.getLogger('profiler_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('profiler.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def runone(s):
    os.system(s)

def kill(cmd):
    count = 1
    if cmd[0:2] == "./":
        cmd = cmd[2:]
    while commands.getoutput("ps -ef | grep %s | grep -v grep| awk '{print $2}'" % cmd) != '':
        commands.getoutput("ps -ef | grep %s | awk '{print $2}' | xargs kill" % cmd)
        print "killing", cmd, count
        logger.info("killing %s %s" % (cmd, count))
        count += 1

def getprocessstatus(outq, process_string):
    time.sleep(5)
    lst = []
    pids = [1]
    while len(pids) != 0:
        pids = [int(i) for i in 
                commands.getoutput(
                "ps -ef|grep %s|grep -v grep|awk '{print $2}'|xargs" 
                % process_string).split()]
        d = {}
        for pid in pids:
           p = psutil.Process(pid)
           d[pid] = p.memory_info()
        lst.append(d)
        print d
        logger.info("%s" % d)
        time.sleep(60)
    outq.put(lst)

def process_data(cmd, nums):
    inq = Queue()
    tokill = [cmd, 'bpan']
    th = [Timer(nums, kill, args=[c]) for c in tokill]
    for x in th:
        x.start()
    t = Thread(target=getprocessstatus, args=(inq, 'bpan'))
    t.start()
    runone(cmd)
    for x in th:
        x.join()
    t.join()
    lst = inq.get()
    inq.task_done()
    print lst
    logger.info("%s" % lst)
    rss = []
    vms = []
    for item in lst:
        for k, v in item.iteritems():
            rss.append(v.rss)
            vms.append(v.vms)
    a, b = float(sum(rss)) / len(rss), float(sum(vms)) / len(vms)
    logger.info("%s, %s" % (a, b))
    print a, b
    return a, b

def setnum_argument(script, key, value):
    logger.info("setting num %s of %s to %s" % (key, script, value))
    os.system('sed -i s/{key}=[0-9]*/{key}={value}/ {script}'.format(key=key, script=script, value=value))

if __name__ == '__main__':
    for n in range(23, 24):
        script1 = './zicluster.sh'
        script2 = './xicluster.sh'
        setnum_argument(script1, 'processes', n)
        setnum_argument(script2, 'processes', n)
        a, b = process_data(script1, 600)
        c, d = process_data(script2, 600)
        logger.info("%s %s %s %s %s %s %s %s"  %(a < c, b < d, a, b, c, d, c / a * 100, d / b * 100))
        print a < c, b < d, a, b, c, d
