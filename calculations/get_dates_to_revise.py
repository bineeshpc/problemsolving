#! /usr/bin/env python
import datetime

def get_delta(days=1):
    return datetime.timedelta(days=days)

def get_days():
    for day in [1, 3, 7, 30, 90, 180]:
        yield day
    while True:
        day = day + day
        yield day

def find_date(day):
    today = datetime.datetime.today()
    old_day = today - get_delta(day)
    if old_day < datetime.datetime(1982, 9, 26):
        return None
    return old_day

for day in get_days():
    date = find_date(day)
    if not date:
        break
    print(date.strftime('%B %d %Y %A'), day)