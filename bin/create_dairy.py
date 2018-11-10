""" Create org mode calendar for given year
"""
import argparse
import datetime

parser = argparse.ArgumentParser(description="This is a tool for creating dairy in org mode format for any given year")
parser.add_argument('year', type=int,
                    help="""Year to make the dairy for.""")
args = parser.parse_args()

year = args.year
filename = '/tmp/journal_{}.org'.format(year)

def create_dairy(year, filename):
    """ Create dairy for year and filename """
    fileobj = open(filename, 'w')
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    timedelta = datetime.timedelta(days=1)
    date_var = start
    while date_var <= end:
        if date_var.day == 1:
            month_line = '* {}-{} {}\n'.format(date_var.year, date_var.strftime('%d'), date_var.strftime('%B'))
            fileobj.write(month_line)
        day_line = '** {}-{}-{} {}\n'.format(date_var.year, date_var.strftime('%m'), date_var.strftime('%d'), date_var.strftime('%A'))
        fileobj.write(day_line)

        date_var += timedelta

    fileobj.close()
    print "created diary for year {} at {}".format(year, filename)

create_dairy(year, filename)
