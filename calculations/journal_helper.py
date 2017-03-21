import datetime


a = datetime.datetime.today()
b = datetime.datetime(2017, 12, 31)


def get_all_dates(begin, end):
    current = begin
    while current <= end:
        yield current
        current = current + datetime.timedelta(days=1)


# get_all_dates(datetime.datetime(2017, 03, 18), b)


def generate_journal_data(begin, end):
    month = begin.month
    yield begin.strftime('** %Y-%m %B')
    for date in get_all_dates(begin, end):
        if month == date.month:
            new_month = False
        else:
            new_month = True
        if new_month:
            yield date.strftime('** %Y-%m %B')
        month = date.month
        yield date.strftime('*** %Y-%m-%d %A')


for x in generate_journal_data(a, b):
    print x
