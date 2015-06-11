#! /usr/bin/env python2
import datetime

today = datetime.datetime.today()
finalday = today + datetime.timedelta(days=120)

print finalday
