"""
Different companies gives discounted subscription rates on annual payments, 6 months payments etc.
Compare the relative benefits of this kind of payment mathematically.
Example:
The hindu subscription rates
1 month - 175
3 months - 500
6 - 950
12 - 1800
"""

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "subscription_rate",
     help="Subscription rate for the lowest period",
    type=float)
parser.add_argument("num_periods",
    help="Total number of periods",
    type=int)
args = parser.parse_args()

offers = {1: 175, 3: 500, 6: 950, 12: 1800}


def calculate_without_offers(num_periods, one_period_rate=args.subscription_rate):
    return num_periods * one_period_rate


def calculate_with_offers(num_periods):
    return offers[num_periods]


def calculate_interest(principal, months=1,
                       interest_rate=10. / 100):
    return principal * months * interest_rate


def compare_scenarios(total_money, n, payment_per_period=100, interest_rate=10. / 100):
    """ I have money in hand. I should know which strategy is better.
    Example: time t0, Pay 100, keep 200, interest = 200 * interest_rate * 1 / 12 (for one month)
    time t1, Pay 100, keep 100, interest = 100 * interest_rate * 1 / 12 ( for one month
    remaining_money * interest_rate * 1. / 12)
    for t0 to tn-1 interest gained = sum of remaining_money * interest_rate * 1 / 12.
    In other words
    remaining_money = total_money - (x + 1) * payment_per_period
    sigma x = 0 to n-1 (remaining_money * interest_rate * 1. / 12)
    sigma x = 0 to n-1 (total_money - (x+1) * payment_per_period) * interest rate * 1. / 12
    """
    interest = []
    for x in range(n):
        remaining_money = total_money - (x + 1) * payment_per_period
        interest_gained = remaining_money * interest_rate * 1. / 12
        interest.append(interest_gained)
    total_interest_gained = sum(interest)
    return total_interest_gained


def calculate():
    message1 = "rate without offers for period {months}"
    message2 = " is {without_offers} "
    message3 = "rate with offers is {offer_rate} "
    message4 = "and the difference is {difference}."
    for num_months in [1, 3, 6, 12]:
        rate_without_offers = calculate_without_offers(num_months)
        offered_rate = calculate_with_offers(num_months)
        difference = rate_without_offers - offered_rate
        message = ''.join([message1, message2, message3, message4])
        print((message.format(months=num_months,
                             without_offers=rate_without_offers,
                             difference=difference,
                             offer_rate=offered_rate)))
        print(("interest gained during this period", compare_scenarios(175 * num_months, num_months, 175, 10. / 100)))

calculate()