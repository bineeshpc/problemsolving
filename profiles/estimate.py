#! /usr/bin/env python2
'''
Program for printing out the estimated addition time for a profile
'''
import datetime

biniid = 3018953
bini = datetime.datetime.strptime('2015-03-20', '%Y-%m-%d')
#print bini

def get_additions_perday():
    
    latest = datetime.datetime.strptime('2015-12-06', '%Y-%m-%d')
    latestid = 3271292
    totaladditions = latestid - biniid
    #print totaladditions
    population = 34.8 * 10**6
    totaladditions / population
    totaladditions / population  * 100
    numdaysforadditions = latest - bini
    numdays  = float(numdaysforadditions.days)
    #print numdays
    additionsperday = totaladditions / numdays
    #print additionsperday
    return additionsperday

def get_estimated_addition_date(anuid, additionsperday):
    diffid = biniid - anuid
    difffrombini = diffid / additionsperday
    #print difffrombini
    difffrombinitimedelta = datetime.timedelta(int(difffrombini))
    anuaddeddate = bini - difffrombinitimedelta
    print '{} was added on {}'.format(anuid, anuaddeddate)
    return anuaddeddate

def main():
    anuid = int(args.anuid)
    additionsperday = get_additions_perday()
    get_estimated_addition_date(anuid, additionsperday)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("anuid", help="Give the id of the profile which you want to check addition date")
    args = parser.parse_args()
    #print args.anuid
    main()