import argparse
import webbrowser

parser = argparse.ArgumentParser(description='Open profiles in webbrowser.')
parser.add_argument('filename', default='profiles.org',
                   help='add filename to read from')
args = parser.parse_args()
print(args.filename)


searchstring = "http://profile.keralamatrimony.com/profiledetail/viewprofile.php?id={}&gaact=SID&gasrc=SRCH"

f = open(args.filename)
count = 0
for x in f:
    count += 1
    ss = searchstring.format(x)
    webbrowser.open_new_tab(ss)
    if count % 5 == 0:
        input("press enter")
