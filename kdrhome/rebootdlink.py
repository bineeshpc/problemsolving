#!/usr/bin/python
import pexpect
import sys
import json

passwordfile = '.passwords'
jsonobj = json.load(open(passwordfile))['dlink']
ip = jsonobj['ip']
password = jsonobj['password']
child = pexpect.spawn('telnet {}'.format(ip))

child.expect('ssword:')
child.sendline(password)
child.expect('D-Link>')
child.sendline('set reboot')
print(child.after)
#sys.stdout.flush()
#child.interact() # Escape character defaults to ^]

