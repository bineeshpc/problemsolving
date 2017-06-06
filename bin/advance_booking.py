#! /usr/bin/env python2
import datetime
import argparse


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("days_ahead",
                        help="First chance to book in on this day",
                        type=int)
    args = parser.parse_args()
    return args.days_ahead


def get_final_day(num_days_ahead):
    today = datetime.datetime.today()
    finalday = today + datetime.timedelta(days=num_days_ahead)
    return finalday.strftime('%Y %B %d %A')


print get_final_day(parse_commandline())
