infile = 'ids.txt'
outfile = 'profiles.txt'

profileurl = "http://profile.keralamatrimony.com/profiledetail/viewprofile.php?id={}&gaact=SID&gasrc=SRCH"

inf = open(infile)
ouf = open(outfile, 'a')

for line in inf:
    fullid = 'E{}'.format(line.strip())
    purl = profileurl.format(fullid)
    outline = "{},{},\n".format(fullid, purl)
    print(outline)
    ouf.write(outline)
