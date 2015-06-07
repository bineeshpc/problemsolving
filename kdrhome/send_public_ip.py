#!/usr/bin/env python

import smtplib
import json
import dns.resolver # $ pip install dnspython

def get_public_ip():
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ["208.67.222.222", "208.67.220.220"]
    return resolver.query('myip.opendns.com')[0]


passwordfile= '.passwords'
host = 'smtp.gmail.com'
port = '587'
jsonobj = json.load(open(passwordfile))['gmail']
user = jsonobj['username']
passw = jsonobj['password']

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(user,passw)

#server = smtplib.SMTP()
#server.connect(host, port)
#server.ehlo()
#server.starttls()
#server.login(user, passw)

tolist = ["bineeshpc@gmail.com"]
fromaddr = '"kdrhome" '
subject = 'Notification'
message = '''

My IP address is %s

''' % get_public_ip()

hdr = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (fromaddr, tolist, subject)
server.sendmail(user, tolist, hdr+message)
server.quit
